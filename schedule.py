#!/usr/bin/env python
# coding: utf-8
import web
#import sys, os
#sys.path.append(os.path.dirname(__file__))
#from datetime import datetime

import settings
render = settings.render
db = settings.db
tb = 'schedule'
from config.url import urls



db = settings.db
store = web.session.DBStore(db, 'sessions')
session = web.session.Session(app, store, initializer={'loginned':0, 's_name':'jim'})

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

def get_by_id(id):
    s = db.select(tb, where='id=$id', vars=locals())
    if not s:
        return False
    return s[0]


class New:

    def POST(self):
        new_time = web.input(s_time=[])
        user = db.select('user_data', where='s_name="'+web.ctx.session.s_name+'"')
        duty = user[0].time_duty + len(new_time.s_time)
        db.update('user_data', where='s_name="'+web.ctx.session.s_name+'"', time_duty=duty)
        #if not new_id.s_id:
            #return render.error('学号是必须的', None)
        for k in range(0, len(new_time.s_time)):
            db.insert(tb, s_name=web.ctx.session.s_name, s_time=new_time.s_time[k])
        raise web.seeother('/schedule/data')

class SuperNew:
    def POST(self):
        new_name = web.input().get('s_name')
        new_time = web.input(s_time=[])

        if not new_time:
            return render.error('请选择时间', None)

        user = db.select('user_data', where='s_name="'+new_name+'"')

        if user:
            duty = user[0].time_duty + len(new_time.s_time)
            db.update('user_data', where='s_name="'+new_name+'"', time_duty=duty)
            for k in range(0, len(new_time.s_time)):
                db.insert(tb, s_name=new_name, s_time=new_time.s_time[k])
            raise web.seeother('/schedule/data')

        else:
            return render.error('名字不存在', None)

        

class Delete:

    def GET(self, id):
        schedule = get_by_id(id)
        if not schedule:
            return render.error('没找到这条记录', None)
        user = db.select('user_data', where='s_name="'+schedule.s_name+'"')
        duty = user[0].time_duty - 1
        db.update('user_data', where='s_name="'+schedule.s_name+'"', time_duty=duty)
        db.delete(tb, where='id=$id', vars=locals())
        raise web.seeother('/schedule/data')
        #return render.error('删除成功！', '/')


class Data:

    def GET(self):
        #session = web.config._session
        if web.ctx.session.loginned == 1:
        #schedules = db.select(tb, where='s_id="'+session.s_id+'"', order='s_time asc')
            user = db.select('user_data', where='s_name="'+web.ctx.session.s_name+'"')
            my_type = user[0].s_type
            if my_type == 0:
                schedules = db.select(tb, where='s_name="'+web.ctx.session.s_name+'"', order='s_time asc')
                return render.user(schedules)
            elif my_type == 1:
                schedules = db.select(tb, order='s_time asc')
                users = db.select('user_data', order='s_id asc')
                return render.superuser(schedules, users)
            elif my_type == 2:
                schedules = db.select('finalschedule', order='s_time asc')
                users = db.select('finaluser_data', order='s_name asc')
                return render.manage(schedules, users)
        raise web.seeother('/')


class Index:
    
    def GET(self):
        return render.index()

class Login:
    
    def POST(self):
        i = web.input()
        my_id = i.get('s_id')
        my_pass = i.get('s_pass')

        data=db.select('user_data',where='s_id=$my_id', vars=locals())

        user = []
        for i in data:
            user.append(i)
        
        if not user:
            return render.error('用户名不存在', None)

        if my_pass != user[0].s_pass:
            return render.error('密码错误,若密码超过10位，请输入密码的前10位', None)
        else:
            web.ctx.session.loginned = 1
            web.ctx.session.s_name = user[0].s_name
            raise web.seeother('/schedule/data')

class Register:

    def GET(self):
        return render.register()

    def POST(self):
        i = web.input()
        my_id = i.get('s_id')
        my_name = i.get('s_name')
        my_pass = i.get('s_pass')
        test_pass = i.get('test_pass')

        if(test_pass != my_pass):
            return render.error('两次输入的密码不一致', None)

        result = db.select('user_data', where='s_id=$my_id', vars=locals())
        if result:
            return render.error('用户已存在', None)
        
        db.insert('user_data', s_id=my_id, s_name=my_name, s_pass=my_pass)
        return render.error('注册成功', '/')


class Logout:

    def GET(self):
        web.ctx.session.kill()
        raise web.seeother('/')

class Attend:

    def GET(self, sid):
        schedule = db.select('finalschedule', where='id=$sid', vars=locals())
        name = schedule[0].s_name
        user = db.select('finaluser_data', where='s_name=$name', vars=locals())
        actual = user[0].time_actual + 1
        db.update('finaluser_data', where='s_name=$name', time_actual=actual, vars=locals())
        db.update('finalschedule', where='id="'+sid+'"', finish='1', vars=locals())
        raise web.seeother('/schedule/data')

class Undo:

    def GET(self, sid):
        schedule = db.select('finalschedule', where='id=$sid', vars=locals())
        myschedule = schedule[0]
        change = myschedule.ischange
        if not change:
            name = myschedule.s_name
            
        else:
            name = myschedule.person

        user = db.select('finaluser_data', where='s_name=$name', vars=locals())
        actual = user[0].time_actual - 1
        db.update('finaluser_data', where='s_name=$name', time_actual=actual, vars=locals())
        db.update('finalschedule', where='id=$sid', finish='0', ischange='0', vars=locals())

        raise web.seeother('/schedule/data')

class Userclear:

    def GET(self):
        users = db.select('finaluser_data')
        for user in users:
            db.update('finaluser_data', where='s_name="'+user.s_name+'"', time_actual = '0')
        raise web.seeother('/schedule/data')

class Scheduleclear:
    
    def GET(self):
        schedules = db.select('finalschedule')
        for schedule in schedules:
            sid = schedule.id
            db.update('finalschedule', where='id=$sid', finish='0', ischange='0', vars=locals())
        raise web.seeother('/schedule/data')

class Strike:

    def GET(self, sid):
        schedule = db.select('schedule', where='id="'+sid+'"')
        name = schedule[0].s_name
        user = db.select('user_data', where='s_name="'+name+'"')
        duty = user[0].time_duty - 1
        db.update('schedule', where='id="'+sid+'"', keep='0')
        db.update('user_data', where='s_name="'+name+'"', time_duty=duty)
        raise web.seeother('/schedule/data')

class Strikeundo:

    def GET(self, sid):
        schedule = db.select('schedule', where='id="'+sid+'"')
        name = schedule[0].s_name
        user = db.select('user_data', where='s_name="'+name+'"')
        duty = user[0].time_duty + 1
        db.update('schedule', where='id="'+sid+'"', keep='1')
        db.update('user_data', where='s_name="'+name+'"', time_duty=duty)
        raise web.seeother('/schedule/data')

class Launch:
    
    def GET(self):
        finalschedules = db.select('finalschedule')
        finalusers = db.select('finaluser_data')
        schedules = db.select('schedule')
        users = db.select('user_data')
        for finalschedule in finalschedules:
            db.delete('finalschedule', where='id=finalschedule.id')
        for finaluser in finalusers:
            name = finaluser.s_name
            db.delete('finaluser_data', where='s_name=$name', vars = locals())
        for schedule in schedules:
            if schedule.keep:
                db.insert('finalschedule', s_name=schedule.s_name, s_time=schedule.s_time)
            else:
                sid=schedule.id
                db.delete('schedule', where='id=$sid', vars=locals())
        for user in users:
            if user.s_type == 0:
                db.insert('finaluser_data', s_name=user.s_name, time_duty=user.time_duty)
        raise web.seeother('/schedule/data')
            

        
class Cover:
    
    def GET(self, sid):
        db.update('finalschedule', where='id=$sid', ischange='1', vars=locals())
        raise web.seeother('/schedule/data')

class Coverundo:
    
    def GET(self, sid):
        db.update('finalschedule', where='id=$sid', ischange='0', vars=locals())
        raise web.seeother('/schedule/data')

class Coverperson:

    def POST(self, sid):
        myperson = web.input().get('person')

        result = db.select('finaluser_data', where='s_name=$myperson', vars=locals())
        if not result:
            return render.error('用户名不存在', None)

        db.update('finalschedule', where='id=$sid', person=myperson, finish='1', vars=locals())
        schedule = db.select('finalschedule', where='id=$sid', vars=locals())
        user = db.select('finaluser_data', where='s_name=$myperson', vars=locals())
        actual = user[0].time_actual + 1
        db.update('finaluser_data', where='s_name=$myperson', time_actual=actual, vars=locals())

        raise web.seeother('/schedule/data')
        
class Userdelete:

    def GET(self, sid):
        user = db.select('user_data', where='s_id=$sid', vars=locals())
        name = user[0].s_name
        db.delete('user_data', where='s_id=$sid', vars=locals())
        db.delete('schedule', where='s_name=$name', vars=locals())
        raise web.seeother('/schedule/data')