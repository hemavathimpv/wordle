from django.urls import path

from .views import WordleNamesViews

urlpatterns = [
    path('wordle_names/', WordleNamesViews.as_view()),
]