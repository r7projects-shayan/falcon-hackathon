from django.http import JsonResponse

def chatbot_diagnosis(request):
    # Dummy response for AI chatbot diagnosis
    data = {"diagnosis": "This is a preliminary diagnosis based on symptoms."}
    return JsonResponse(data)

def drug_identification(request):
    # Dummy response for drug identification
    data = {"drug_info": "This is the identified drug information."}
    return JsonResponse(data)
