from rest_framework import serializers

from inquisitor.models import Response, Campaign


class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'name', 'description', 'created_date', 'modified_date')


class ResponseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Response
        fields = ('id', 'campaign', 'created_date', 'ref', 'ref_name', 'user', 'user_name', 'user_email',
                  'text', 'datetime', 'comment', 'last_contact_date', 'enabled', 'source')

