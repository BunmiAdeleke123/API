from rest_framework import serializers
from .models import Articles, Register

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields=["Topic","memoryverse","writing","month","Date"]

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields=["username","gmail","Date"]