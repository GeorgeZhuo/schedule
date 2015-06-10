#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'



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



        