from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from articles.serializers import ArticleOutSerializer, ArticleInSerializer
from articles.use_cases.create_article import create_article
from articles.use_cases.get_articles import get_articles


@api_view(["GET", "POST"])
@renderer_classes([JSONRenderer])
def articles_view(request):
    """
    GET:
        Returns all available articles

    POST:
        Create a new article
    """
    if request.method == "GET":
        articles = get_articles()
        return Response(ArticleOutSerializer(articles, many=True).data)

    elif request.method == "POST":
        data = ArticleInSerializer(data=request.data)
        if data.is_valid():
            create_article(data)
            return Response(data=None, status=status.HTTP_201_CREATED)
        else:
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
