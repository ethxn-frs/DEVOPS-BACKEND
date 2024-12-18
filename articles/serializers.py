from rest_framework import serializers

from articles.models import Article


class ArticleInSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=True)
    subtitle = serializers.CharField(max_length=255, required=True)
    summary = serializers.CharField(required=True)


class ArticleOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ["id", "title", "subtitle", "summary"]
