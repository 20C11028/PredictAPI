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
            RestrictedUnderLDR_Model = WpcpredictorConfig.RestrictedUnderLDR_Model
            UHCs_Model = WpcpredictorConfig.UHCs_Model
            PPMVOC500_Model = WpcpredictorConfig.PPMVOC500_Model
            AlternativeStandardsOfSoil_Model = WpcpredictorConfig.AlternativeStandardsOfSoil_Model
            LDRSubcategory_Model = WpcpredictorConfig.LDRSubcategory_Model

            models = [RestrictedUnderLDR_Model, UHCs_Model, PPMVOC500_Model, AlternativeStandardsOfSoil_Model,
                      LDRSubcategory_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['Restricted Under LDR', 'UHCs', '< 500 PPM VOC', 'Alternative Standards of Soil',
                              'LDR Subcategory']

            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                response = dict()
                if output_column_name == 'LDR Subcategory':
                    label_data_map = {'Non Wastewater': 0, 'Wastewater': 1, 'N/A': 2}
                    response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                else:
                    label_data_map = {'No': 0, 'Yes': 1}
                    response[output_column_name] = list(label_data_map.keys())[predictions[i][0].round().astype(int)]

                responses.append(response)

            return HttpResponse(json.dumps(responses))
