from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# Create your tests here.


from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
    def setUp(self):
        someUser_random_user = User.objects.create(username='random_test_user')

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user= User.objects.first(),
            content='Some random content'
            )
        self.assertEqual(obj.content, "Some random content")
        self.assertEqual(obj.id, 1)
        absolute_url = reverse("tweets:detail", kwargs={"pk":1})
        self.assertEqual(obj.get_absolute_url(), absolute_url)

    def test_tweet_url(self):
        obj = Tweet.objects.create(
            user= User.objects.first(),
            content='Some random content'
            )
        absolute_url = reverse("tweets:detail", kwargs={"pk":obj.pk})
        self.assertEqual(obj.get_absolute_url(), absolute_url)
