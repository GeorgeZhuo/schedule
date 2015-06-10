#!/usr/bin/env python
# coding: utf-8
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'

def login(sid, pw):
     data = db.select('user_data', where='s_id=$sid', vars=locals())

     user = []
     for i in data:
         user.append(i)
        
     if not user:
         return 'NotExist'

     if pw != user[0].s_pass:
         return 'PWFalse'

     else:
         return user[0].s_name
    
    