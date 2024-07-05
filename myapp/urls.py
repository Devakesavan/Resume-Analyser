from django.urls import path
from .views import streamlit_view

urlpatterns = [
    
    path('', streamlit_view, name='streamlit-view'),
]


