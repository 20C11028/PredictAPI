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
            PhyState_Model = WpcpredictorConfig.PhyState_Model

            models = [PhyState_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['Solid', 'Liquid', 'Gas', 'Sludge', 'Ash', 'Powder']

            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                response = dict()
                response[output_column_name] = f"{predictions[0][i] * 100:.2f}%"
                responses.append(response)

            return HttpResponse(json.dumps(responses))
