from django.test import TestCase

from articles.models import Article
from articles.serializers import ArticleInSerializer
from articles.use_cases.create_article import create_article


class CreateArticleTestCase(TestCase):
    def test_create_article(self):
        # Given
        self.assertEqual(Article.objects.count(), 0)
        article_data = ArticleInSerializer(
            data={"title": "Title 1", "subtitle": "Subtitle 1", "summary": "Summary"}
        )
        self.assertTrue(article_data.is_valid())

        # When
        create_article(article_data)

        # Then
        self.assertEqual(Article.objects.count(), 1)

        created_article = Article.objects.first()

        self.assertEqual(created_article.title, "Title 1")
        self.assertEqual(created_article.subtitle, "Subtitle 1")
        self.assertEqual(created_article.summary, "Summary")
