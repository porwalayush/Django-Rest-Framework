from rest_framework import serializers
from webapp.models import DRFPost
class DRFPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFPost
        fields = '__all__'