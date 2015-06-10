#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

class Logout:

    def GET(self):
        web.ctx.session.kill()
        raise web.seeother('/')