from django.contrib import admin
from django.urls import path
from .views import KeywordBasedInvestigation,KeywordBasedCBIInvestigation



urlpatterns = [
    path('investigation/', KeywordBasedInvestigation.as_view(), name="KeywordBasedInvestigation"),
    path('cbi_investigation/', KeywordBasedCBIInvestigation.as_view(), name="KeywordBasedCBIInvestigation"),
]
