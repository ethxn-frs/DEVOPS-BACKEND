from django.db.transaction import atomic

from articles.models import Article
from articles.serializers import ArticleInSerializer


@atomic
def create_article(data: ArticleInSerializer) -> None:
    Article.objects.create(
        title=data.validated_data["title"],
        subtitle=data.validated_data["subtitle"],
        summary=data.validated_data["summary"],
    )
