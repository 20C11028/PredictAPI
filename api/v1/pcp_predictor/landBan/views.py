import array
import json

from rest_framework.response import Response

from api.WPCPredictor.apps import WpcpredictorConfig
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
import numpy as np


class call_model(APIView):
    def post(self, request):
        if request.method == 'POST':
            TreatmentStandard_Model = WpcpredictorConfig.TreatmentStandard_Model

            models = [TreatmentStandard_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['TreatmentStandard']
            label_data_map = dict
            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                if output_column_name == 'TreatmentStandard':
                    label_data_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'Not': 8}

                response = dict()
                response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                responses.append(response)

            return HttpResponse(json.dumps(responses))
