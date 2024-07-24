from django.urls import path
from .views import chatbot_diagnosis, drug_identification

urlpatterns = [
    path('diagnosis/', chatbot_diagnosis, name='chatbot_diagnosis'),
    path('drug/', drug_identification, name='drug_identification'),
]
