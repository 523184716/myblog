#!/usr/bin/env python
#coding:utf-8
import  hashlib
def usersecret(passwd):
    passwdexample = hashlib.md5()
    passwdexample.update(passwd)
    result = passwdexample.hexdigest()
    return  result