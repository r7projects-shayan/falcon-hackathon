from django.urls import path
from .views import chatbot_diagnosis, drug_identification, upload_drug_prescription_view

urlpatterns = [
    path('diagnosis/', chatbot_diagnosis, name='chatbot_diagnosis'),
    path('drug/', drug_identification, name='drug_identification'),
    path('upload_drug_prescription/', upload_drug_prescription_view.as_view(), name="upload_drug_prescription"),
]
