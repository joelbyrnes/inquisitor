# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Campaign(BaseModel):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Response(BaseModel):
    campaign = models.ForeignKey(Campaign, null=False, on_delete=models.PROTECT)
    ref = models.CharField(max_length=200)                                 # reference ID (what this query is about)
    ref_name = models.CharField(max_length=200, blank=True)                # reference nice name
    user = models.CharField(max_length=200)                                # user ID
    user_name = models.CharField(max_length=200, blank=True)               # user's name for email
    user_email = models.CharField(max_length=200, blank=True)              # user's email address
    text = models.CharField(max_length=200, blank=True)                    # short text response, generally an enum
    datetime = models.DateTimeField('date responded', null=True, blank=True)  # when the user last responded
    comment = models.TextField(blank=True, null=True)                      # free text comment
    last_contact_date = models.DateTimeField(null=True, blank=True)        # when last contact with user attempted
    enabled = models.BooleanField(default=True)                            # is a response still required?
    source = models.CharField(max_length=100, null=True, blank=True)       # source of record, or reason for existence

    # TODO unique ref and campaign

    def __str__(self):
        return self.ref
