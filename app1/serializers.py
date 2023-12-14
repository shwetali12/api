from rest_framework import serializers
from app1.models import Financialdata, Analytics

class FinancialdataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Financialdata
        fields = '__all__'
        

class AnalyticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analytics
        fields = '__all__'
        

        