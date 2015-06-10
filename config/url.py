#!/usr/bin/env python
# coding: utf-8

pre_fix = 'controllers.'

urls = (
    '/',                               pre_fix + 'schedule.Index',
    '/schedule/data',                  pre_fix + 'schedule.Data',
    '/schedule/new',                   pre_fix + 'schedule.New',
    '/schedule/superusernew',          pre_fix + 'schedule.SuperNew',
    '/schedule/login',                 pre_fix + 'schedule.Login',
    '/schedule/logout',                pre_fix + 'schedule.Logout',
    '/schedule/register',              pre_fix + 'schedule.Register',
    '/schedule/(\d+)/delete',          pre_fix + 'schedule.Delete',
    '/schedule/(\d+)/attend',          pre_fix + 'schedule.Attend',
    '/schedule/(\d+)/undo',            pre_fix + 'schedule.Undo',
    '/schedule/(\d+)/cover',           pre_fix + 'schedule.Cover',
    '/schedule/(\d+)/coverundo',       pre_fix + 'schedule.Coverundo',
    '/schedule/userclear',             pre_fix + 'schedule.Userclear',
    '/schedule/scheduleclear',         pre_fix + 'schedule.Scheduleclear',
    '/schedule/(\d+)/strike',          pre_fix + 'schedule.Strike',
    '/schedule/(\d+)/strikeundo',      pre_fix + 'schedule.Strikeundo',
    '/schedule/launch',                pre_fix + 'schedule.Launch',
    '/schedule/(\d+)/coverperson',     pre_fix + 'schedule.Coverperson',
    '/schedule/(\d+)/userdelete',      pre_fix + 'schedule.Userdelete',
)
