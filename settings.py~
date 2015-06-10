#!/usr/bin/env python
# coding: utf-8
import web
import os
import MySQLdb
#import sae.const
#MYSQL_DB = sae.const.MYSQL_DB 
#MYSQL_USER = sae.const.MYSQL_USER 
#MYSQL_PASS = sae.const.MYSQL_PASS 
#MYSQL_HOST_M = sae.const.MYSQL_HOST 
#MYSQL_HOST_S = sae.const.MYSQL_HOST_S 
#MYSQL_PORT = int(sae.const.MYSQL_PORT)

db = web.database(dbn='mysql', db='schedule', user='root')
# db = MySQLdb.connection(host=MYSQL_HOST_M,port=MYSQL_PORT,user=MYSQL_USER,passwd=MYSQL_PASS)
# db.select_db(MYSQL_DB)

#db = web.database(dbn='mysql', port=int(sae.const.MYSQL_PORT), host=sae.const.MYSQL_HOST, db=sae.const.MYSQL_DB, user=sae.const.MYSQL_USER, pw=sae.const.MYSQL_PASS)

render = web.template.render(os.path.join(os.path.dirname(__file__), 'templates'))
web.config.debug = True

config = web.storage(
    email='joezhujf@gmail.com',
    site_name = '排班系统',
    site_desc = '',
    static = '/static',
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render
