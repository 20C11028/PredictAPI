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
            EPASourceCode_Model = WpcpredictorConfig.EPASourceCode_Model
            OriginCode_Model = WpcpredictorConfig.OriginCode_Model
            EPAFormCode_Model = WpcpredictorConfig.EPAFormCode_Model

            models = [EPASourceCode_Model, OriginCode_Model, EPAFormCode_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['EPASourceCode', 'OriginCode', 'EPAFormCode']
            label_data_map = dict
            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                if output_column_name == 'EPASourceCode':
                    label_data_map = {'G01': 0, 'G02': 1, 'G03': 2, 'G04': 3, 'G05': 4, 'G06': 5, 'G07': 6, 'G08': 7,
                                      'G09': 8,
                                      'G11': 9,
                                      'G12': 10,
                                      'G13': 11, 'G14': 12, 'G15': 13, 'G16': 14, 'G17': 15, 'G19': 16, 'G21': 17,
                                      'G22': 18,
                                      'G23': 19,
                                      'G24': 20,
                                      'G25': 21, 'G27': 22, 'G31': 23, 'G32': 24, 'G33': 25, 'G39': 26, 'G43': 27,
                                      'G44': 28,
                                      'G45': 29,
                                      'G49': 30,
                                      'G61': 31, 'N/A': 32}
                elif output_column_name == 'OriginCode':
                    label_data_map = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, 'N/A': 7}
                elif output_column_name == 'EPAFormCode':
                    label_data_map = {'W001': 0, 'W002': 1, 'W004': 2, 'W005': 3, 'W101': 4, 'W103': 5, 'W105': 6,
                                      'W107': 7,
                                      'W110': 8,
                                      'W113': 9,
                                      'W117': 10, 'W119': 11, 'W200': 12, 'W202': 13, 'W203': 14, 'W204': 15,
                                      'W205': 16,
                                      'W206': 17,
                                      'W209': 18,
                                      'W210': 19, 'W211': 20, 'W219': 21, 'W301': 22, 'W303': 23, 'W304': 24,
                                      'W307': 25,
                                      'W309': 26,
                                      'W310': 27,
                                      'W312': 28, 'W316': 29, 'W319': 30, 'W320': 31, 'W401': 32, 'W403': 33,
                                      'W405': 34,
                                      'W406': 35,
                                      'W409': 36,
                                      'W501': 37, 'W503': 38, 'W504': 39, 'W505': 40, 'W506': 41, 'W512': 42,
                                      'W519': 43,
                                      'W603': 44,
                                      'W604': 45,
                                      'W606': 46, 'W609': 47, 'W801': 48, 'N/A': 49}

                response = dict()
                response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                responses.append(response)

            return HttpResponse(json.dumps(responses))
