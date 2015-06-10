#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'

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

        