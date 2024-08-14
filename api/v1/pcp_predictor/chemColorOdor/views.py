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
            Color_Model = WpcpredictorConfig.Color_Model
            Odor_Model = WpcpredictorConfig.Odor_Model
            BoilingPoint_Model = WpcpredictorConfig.BoilingPoint_Model
            TotalOrganicCarbon_Model = WpcpredictorConfig.TotalOrganicCarbon_Model
            Viscosity_Model = WpcpredictorConfig.Viscosity_Model
            SpecificGravity_Model = WpcpredictorConfig.SpecificGravity_Model

            models = [Color_Model, Odor_Model, BoilingPoint_Model, TotalOrganicCarbon_Model,
                      Viscosity_Model, SpecificGravity_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['Color', 'Odor', 'Boiling Point', 'Total Organic Carbon', 'Viscosity', 'Specific Gravity']

            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                response = dict()
                if output_column_name == 'Color':
                    label_data_map = {'varies': 0, 'colorless': 1, 'white': 2, 'brown': 3, 'yellow': 4, 'N/A': 5,
                                      'grey': 6, 'black': 7,
                                      'green': 8, 'cloudy': 9, 'red': 10, 'silver': 11, 'blue': 12}
                    response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                elif output_column_name == 'Odor':
                    label_data_map = {'Other': 0, 'None': 1, 'Mild': 2, 'Strong': 3}
                    response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                elif output_column_name == 'Boiling Point':
                    label_data_map = {'≤95F': 0, '>95F': 1, 'N/A': 2}
                    response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                elif output_column_name == 'Total Organic Carbon':
                    label_data_map = {'<1%': 0, '1-9%': 1, '>10%': 2, 'N/A': 3}
                    response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                elif output_column_name == 'Viscosity':
                    label_data_map = {'Other': 0, '1 - 100': 1, '101 - 500': 2, '501 - 10000': 3, '> 10000': 4}
                    response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                else:
                    response[output_column_name] = f"{predictions[i][0]:.2f}"

                responses.append(response)

            return HttpResponse(json.dumps(responses))
