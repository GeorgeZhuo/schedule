#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls
from Controller import ArrangeManager

render = settings.render
db = settings.db
tb = 'schedule'

class Strike:

    def GET(self, sid):
        ArrangeManager.strike(sid)
        raise web.seeother('/schedule/data')

class Strikeundo:

    def GET(self, sid):
        ArrangeManager.strikeUndo(sid)
        raise web.seeother('/schedule/data')

class Launch:
    
    def GET(self):
        ArrangeManager.launch()
        raise web.seeother('/schedule/data')

class Userdelete:

    def GET(self, sid):
        ArrangeManager.userDelete(sid)
        raise web.seeother('/schedule/data')
