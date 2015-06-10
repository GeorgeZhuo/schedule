#!/usr/bin/env python
# coding: utf-8
import web
import os
import MySQLdb

db = web.database(dbn='mysql', db='schedule', user='root')

render = web.template.render(os.path.join(os.path.dirname(__file__), '../static/templates'))
web.config.debug = True

config = web.storage(
    email='joezhujf@gmail.com',
    site_name = '排班系统',
    site_desc = '',
    static = '/static',
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
