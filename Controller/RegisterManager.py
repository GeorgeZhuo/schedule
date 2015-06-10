#!/usr/bin/env python
# coding: utf-8
import web
from config import settings
from config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'

class Register:

    def GET(self):
        return render.register()

    def POST(self):
        i = web.input()
        my_id = i.get('s_id')
        my_name = i.get('s_name')
        my_pass = i.get('s_pass')
        test_pass = i.get('test_pass')

        if(test_pass != my_pass):
            return render.error('两次输入的密码不一致', None)

        result = db.select('user_data', where='s_id=$my_id', vars=locals())
        if result:
            return render.error('用户已存在', None)
        
        db.insert('user_data', s_id=my_id, s_name=my_name, s_pass=my_pass)
        return render.error('注册成功', '/')