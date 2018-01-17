#!/usr/bin/env python
#coding:utf-8

from django import  template

register = template.Library()

@register.filter
def DataAdd(v1,v2):
    return v1+v2


@register.simple_tag
def MultiTags(v1,v2,v3):
    return v1+v2+v3
