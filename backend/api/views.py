from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DiagnosisSerializer, DrugSerializer

@api_view(['GET'])
def chatbot_diagnosis(request):
    # In a real application, you would process the diagnosis here
    diagnosis_data = {"diagnosis": "This is a preliminary diagnosis based on symptoms."}
    serializer = DiagnosisSerializer(diagnosis_data)
    return Response(serializer.data)

@api_view(['GET'])
def drug_identification(request):
    # In a real application, you would process the drug identification here
    drug_data = {"drug_info": "This is the identified drug information."}
    serializer = DrugSerializer(drug_data)
    return Response(serializer.data)