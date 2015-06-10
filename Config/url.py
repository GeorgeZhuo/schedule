#!/usr/bin/env python
# coding: utf-8

login = 'View.LoginInterface.'
logout = 'View.LogoutInterface.'
register = 'View.RegisterInterface.'
arrange = 'View.ArrangeInterface.'
attend = 'View.AttendInterface.'
dutyinfo = 'View.DutyInfoInterface.'
select = 'View.SelectInterface.'

urls = (
    '/schedule/register',               register    + 'Register',

    '/schedule/logout',                 logout 	    + 'Logout',

    '/',				login 	    + 'Index',
    '/schedule/login',                  login 	    + 'Login',

    '/schedule/data',                   dutyinfo    + 'Data',
    '/schedule/userclear',              dutyinfo    + 'Userclear',
    '/schedule/scheduleclear',          dutyinfo    + 'Scheduleclear',

    '/schedule/(\d+)/strike',           select      + 'Strike',
    '/schedule/(\d+)/strikeundo',       select      + 'Strikeundo',
    '/schedule/launch',                 select      + 'Launch',

    '/schedule/new',                    arrange     + 'New',
    '/schedule/superusernew',           arrange     + 'SuperNew',
    '/schedule/(\d+)/delete',           arrange     + 'Delete',
    '/schedule/(\d+)/userdelete',       arrange     + 'Userdelete',

    '/schedule/(\d+)/attend',           attend      + 'Attend',
    '/schedule/(\d+)/undo',             attend      + 'Undo',
    '/schedule/(\d+)/coverperson',      attend      + 'Coverperson',
    '/schedule/(\d+)/cover',            attend      + 'Cover',
    '/schedule/(\d+)/coverundo',        attend      + 'Coverundo',
)
