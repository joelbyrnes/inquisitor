# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from inquisitor.models import Campaign, Response


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'id', 'created_date', 'modified_date')
    search_fields = ['name', 'description']


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'ref', 'ref_name', 'user', 'datetime', 'text', 'comment', 'last_contact_date',
                    'enabled', 'source', 'created_date', 'modified_date')
    search_fields = ['campaign', 'ref', 'text', 'comment']
