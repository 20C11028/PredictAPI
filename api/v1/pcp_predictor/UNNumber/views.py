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
            UNNumber_Model = WpcpredictorConfig.UNNumber_Model

            models = [UNNumber_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['UN Number']
            label_data_map = dict
            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                if output_column_name == 'UN Number':
                    label_data_map = {'N/A': 0, 'NA1993': 1, 'NA3077': 2, 'NA3082': 3, 'UN1133': 4, 'UN1170': 5,
                                      'UN1203': 6, 'UN1219': 7, 'UN1230': 8, 'UN1263': 9, 'UN1268': 10, 'UN1325': 11,
                                      'UN1444': 12, 'UN1477': 13, 'UN1479': 14, 'UN1490': 15, 'UN1493': 16,
                                      'UN1687': 17, 'UN1719': 18, 'UN1744': 19,
                                      'UN1759': 20, 'UN1760': 21, 'UN1789': 22, 'UN1791': 23, 'UN1814': 24,
                                      'UN1823': 25,
                                      'UN1824': 26, 'UN1830': 27, 'UN1851': 28, 'UN1866': 29, 'UN1950': 30,
                                      'UN1987': 31,
                                      'UN1992': 32, 'UN1993': 33, 'UN2014': 34, 'UN2025': 35, 'UN2031': 36,
                                      'UN2672': 37,
                                      'UN2735': 38, 'UN2789': 39, 'UN2794': 40, 'UN2800': 41, 'UN2809': 42,
                                      'UN2810': 43,
                                      'UN2811': 44, 'UN2813': 45, 'UN2920': 46, 'UN2922': 47, 'UN2924': 48,
                                      'UN3077': 49,
                                      'UN3082': 50, 'UN3087': 51, 'UN3090': 52, 'UN3093': 53, 'UN3098': 54,
                                      'UN3099': 55,
                                      'UN3109': 56, 'UN3139': 57, 'UN3149': 58, 'UN3175': 59, 'UN3249': 60,
                                      'UN3260': 61,
                                      'UN3261': 62, 'UN3262': 63, 'UN3264': 64, 'UN3265': 65, 'UN3266': 66,
                                      'UN3267': 67,
                                      'UN3286': 68, 'UN3287': 69, 'UN3288': 70, 'UN3291': 71, 'UN3399': 72,
                                      'UN3480': 73,
                                      'UN3506': 74}

                response = dict()
                response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                responses.append(response)

            return HttpResponse(json.dumps(responses))
