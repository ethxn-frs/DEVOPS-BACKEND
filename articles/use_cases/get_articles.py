from django.db.models import QuerySet
from articles.models import Article


def get_articles() -> QuerySet:
    return Article.objects.all()
