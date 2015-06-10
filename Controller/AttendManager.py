#!/usr/bin/env python
# coding: utf-8
import web
from Config import settings
from Config.url import urls

render = settings.render
db = settings.db
tb = 'schedule'

def attend(sid):
    schedule = db.select('finalschedule', where='id=$sid', vars=locals())
    name = schedule[0].s_name
    user = db.select('finaluser_data', where='s_name=$name', vars=locals())
    actual = user[0].time_actual + 1
    db.update('finaluser_data', where='s_name=$name', time_actual=actual, vars=locals())
    db.update('finalschedule', where='id="'+sid+'"', finish='1', vars=locals())

def undo(sid):
    schedule = db.select('finalschedule', where='id=$sid', vars=locals())
    myschedule = schedule[0]
    change = myschedule.ischange
    if not change:
        name = myschedule.s_name

    else:
        name = myschedule.person

    user = db.select('finaluser_data', where='s_name=$name', vars=locals())
    actual = user[0].time_actual - 1
    db.update('finaluser_data', where='s_name=$name', time_actual=actual, vars=locals())
    db.update('finalschedule', where='id=$sid', finish='0', ischange='0', vars=locals())

def cover(sid):
    db.update('finalschedule', where='id=$sid', ischange='1', vars=locals())

def coverUndo(sid):
    db.update('finalschedule', where='id=$sid', ischange='0', vars=locals())

def coverPerson(sid):
    myperson = web.input().get('person')

    result = db.select('finaluser_data', where='s_name=$myperson', vars=locals())
    if not result:
        return False

    db.update('finalschedule', where='id=$sid', person=myperson, finish='1', vars=locals())
    schedule = db.select('finalschedule', where='id=$sid', vars=locals())
    user = db.select('finaluser_data', where='s_name=$myperson', vars=locals())
    actual = user[0].time_actual + 1
    db.update('finaluser_data', where='s_name=$myperson', time_actual=actual, vars=locals())
    return True