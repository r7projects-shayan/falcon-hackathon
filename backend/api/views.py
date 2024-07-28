from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DiagnosisSerializer, DrugSerializer

from rest_framework.views import APIView
from rest_framework import status

from rest_framework.parsers import FormParser, MultiPartParser

from .serializers import FileUploadSerializer
from .models import DrugPrescriptionFileUpload

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


class upload_drug_prescription_view(APIView):

    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser)


    def post(self, request):
        serialiser = self.serializer_class(data=request.data)
       
        if serialiser.is_valid():
            serialiser.save()
            return Response(
                serialiser.data,
                status=status.HTTP_201_CREATED
                )
        
        return Response(
            serialiser.errors,
            status=status.HTTP_400_BAD_REQUEST
            )



