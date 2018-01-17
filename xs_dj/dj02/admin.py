# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("name","price","pub_date")
    search_fields = ("name","price","pub_date")
    list_filter = ("pub_date",)
    list_per_page = 4
    list_display_links = ("pub_date",   )
    list_max_show_all = 6
    list_editable = ("name",)
admin.site.register(Book,BookAdmin)