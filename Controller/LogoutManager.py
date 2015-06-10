#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from config.url import urls

class Logout:

    def GET(self):
        web.ctx.session.kill()
        raise web.seeother('/')