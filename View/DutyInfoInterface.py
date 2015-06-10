#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'

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