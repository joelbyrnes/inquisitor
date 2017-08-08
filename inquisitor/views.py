# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework import viewsets

from models import Response, Campaign
from serializers import ResponseSerializer, CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all().order_by('-datetime')
    serializer_class = ResponseSerializer
