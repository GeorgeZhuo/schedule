#!/usr/bin/env python
# coding: utf-8
import web
from Controller import AttendManager
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'

class Attend:

    def GET(self, sid):
        AttendManager.attend(sid)
        raise web.seeother('/schedule/data')

class Undo:

    def GET(self, sid):
        AttendManager.undo(sid)
        raise web.seeother('/schedule/data')

class Cover:
    
    def GET(self, sid):
        AttendManager.cover(sid)
        raise web.seeother('/schedule/data')

class Coverundo:
    
    def GET(self, sid):
        AttendManager.coverUndo(sid)
        raise web.seeother('/schedule/data')

class Coverperson:

    def POST(self, sid):
        result = AttendManager.coverPerson(sid)
        if result:
            raise web.seeother('/schedule/data')
        else:
            return render.error('用户名不存在', None)