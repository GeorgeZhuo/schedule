#!/usr/bin/env python
# coding: utf-8
import web
from Controller import LoginManager
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'

class Index:
    
    def GET(self):
        return render.index()

'''
class Login:
    
    def POST(self):
        i = web.input()
        my_id = i.get('s_id')
        my_pass = i.get('s_pass')

        data=db.select('user_data',where='s_id=$my_id', vars=locals())

        user = []
        for i in data:
            user.append(i)
        
        if not user:
            return render.error('用户名不存在', None)

        if my_pass != user[0].s_pass:
            return render.error('密码错误,若密码超过10位，请输入密码的前10位', None)
        else:
            web.ctx.session.loginned = 1
            web.ctx.session.s_name = user[0].s_name
            raise web.seeother('/schedule/data')
'''

class Login:
    
    def POST(self):
        i = web.input()
        my_id = i.get('s_id')
        my_pass = i.get('s_pass')

        result = LoginManager.login(my_id, my_pass)
        
        if result == 'NotExist':
            return render.error('用户名不存在', None)
        elif result == 'PWFalse':
            return render.error('密码错误,若密码超过10位，请输入密码的前10位', None)
        else:
            web.ctx.session.loginned = 1
            web.ctx.session.s_name = result
            raise web.seeother('/schedule/data')