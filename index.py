#!/usr/bin/env python
# coding: utf-8
import sys, os
sys.path.append(os.path.dirname(__file__))

from Config.url import urls
import web
from Config import settings

app = web.application(urls, globals())

db = settings.db
store = web.session.DBStore(db, 'sessions')
session = web.session.Session(app, store, initializer={'loginned':0, 's_name':'jim'})


#session = web.session.Session(app, web.session.DiskStore(os.path.dirname(__file__)+'/sessions'),
#initializer={'loginned':"0", 's_name':'jim'})

rootpath = os.path.dirname(__file__)
web.template.Template.globals['rootpath'] = rootpath

def session_hook():
    web.ctx.session = session
    web.template.Template.globals['session'] = session
app.add_processor(web.loadhook(session_hook))

if __name__ == "__main__":
    app.run()
