import array
import json

from rest_framework.response import Response

from api.WPCPredictor.apps import WpcpredictorConfig
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
import numpy as np
import pandas as pd
from tabulate import tabulate


class call_model(APIView):
    def post(self, request):
        if request.method == 'POST':
            # PCP Models
            PCPViscosity_Model = WpcpredictorConfig.PCPViscosity_Model
            PCPBTUValue_Model = WpcpredictorConfig.PCPBTUValue_Model
            PCpH_Model = WpcpredictorConfig.PCpH_Model
            PCFlashPoint_Model = WpcpredictorConfig.PCFlashPoint_Model
            PCFlashPoint_Method_Model = WpcpredictorConfig.PCFlashPoint_Method_Model
            models = [PCPViscosity_Model, PCPBTUValue_Model, PCpH_Model, PCFlashPoint_Model, PCFlashPoint_Method_Model]

            inputJson = json.loads(request.body)
            inputText = np.array(inputJson['processGeneratingWaste'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['PCPViscosity', 'PCPBTUValue', 'PCpH', 'PCFlashPoint', 'PCFlashPoint_Method']
            label_data_map = dict
            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                if output_column_name == 'PCPViscosity':
                    label_data_map = {'Other': 0, '1 - 100': 1, '101 - 500': 2, '501 - 10000': 3, '> 10000': 4}
                elif output_column_name == 'PCPBTUValue':
                    label_data_map = {'Other': 0, '0 - 4999': 1, '5000 - 10000': 2, '> 10000': 3}
                elif output_column_name == 'PCpH':
                    label_data_map = {'Custom': 0, '2': 1, '> 2 to 5': 2, '> 5 to 10': 3, '>10 to <12.5': 4, '12.5': 5,
                                      'N/A': 6}
                elif output_column_name == 'PCFlashPoint':
                    label_data_map = {'Other': 0, '< 73°F': 1, '73°F to < 100°F': 2, '100°F to < 140°F': 3,
                                      '140°F to < 150°F': 4,
                                      '150°F to < 200°F': 5, '200°F': 6, 'N/A': 7}
                elif output_column_name == 'PCFlashPoint_Method':
                    label_data_map = {'Closed Cup': 0, 'Open Cup': 1}
                for z in range(len(label_data_map)):
                    print(f"{list(label_data_map.keys())[z]}: {predictions[i][z] * 100:.2f}%")

                response = dict()
                response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                responses.append(response)

            return HttpResponse(json.dumps(responses))
