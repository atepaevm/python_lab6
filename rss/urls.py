from rss.views import RSS

from django.urls import path

urlpatterns = [
    path('', RSS.as_view()),
]
