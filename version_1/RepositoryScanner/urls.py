from django.contrib import admin
from django.urls import path
from .views import KeywordBasedInvestigation



urlpatterns = [
    path('', KeywordBasedInvestigation.as_view(), name="KeywordBasedInvestigation"),
]
