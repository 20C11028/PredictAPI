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
            ShippingAndPackagingFrequency_Model = WpcpredictorConfig.ShippingAndPackagingFrequency_Model
            ShippingAndPackagingWasteCombination_Model = WpcpredictorConfig.ShippingAndPackagingWasteCombination_Model
            TransportationRequirement_Model = WpcpredictorConfig.TransportationRequirement_Model

            models = [ShippingAndPackagingFrequency_Model, ShippingAndPackagingWasteCombination_Model,
                      TransportationRequirement_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['ShippingAndPackagingFrequency', 'ShippingAndPackagingWasteCombination',
                              'TransportationRequirement']
            label_data_map = dict
            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                if output_column_name == 'ShippingAndPackagingFrequency':
                    label_data_map = {'One Time': 0, 'Monthly': 1, 'Quarterly': 2, 'Annually': 3, 'Other': 4}
                elif output_column_name == 'ShippingAndPackagingWasteCombination':
                    label_data_map = {'No': 0, 'Yes': 1}
                elif output_column_name == 'TransportationRequirement':
                    label_data_map = {'Containerized': 0, 'Bulk Liquid': 1, 'Bulk Solid': 2}

                response = dict()
                if output_column_name == 'ShippingAndPackagingWasteCombination':
                    response[output_column_name] = list(label_data_map.keys())[predictions[i][0].round().astype(int)]
                else:
                    response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                responses.append(response)

            return HttpResponse(json.dumps(responses))
