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
            WCHazardousF_Model = WpcpredictorConfig.WCHazardousF_Model
            WCHazardousK_Model = WpcpredictorConfig.WCHazardousK_Model
            WCHazardousP_Model = WpcpredictorConfig.WCHazardousP_Model
            WCHazardousU_Model = WpcpredictorConfig.WCHazardousU_Model
            WCHazardousIgnitable_Model = WpcpredictorConfig.WCHazardousIgnitable_Model
            WCHazardousCorrosive_Model = WpcpredictorConfig.WCHazardousCorrosive_Model
            WCHazardousReactive_Model = WpcpredictorConfig.WCHazardousReactive_Model
            WCHazardousToxic_Model = WpcpredictorConfig.WCHazardousToxic_Model

            models = [WCHazardousF_Model, WCHazardousK_Model, WCHazardousP_Model, WCHazardousU_Model,
                      WCHazardousIgnitable_Model, WCHazardousCorrosive_Model, WCHazardousReactive_Model,
                      WCHazardousToxic_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['WCHazardousF', 'WCHazardousK', 'WCHazardousP', 'WCHazardousU',
                                         'WCHazardousIgnitable', 'WCHazardousCorrosive', 'WCHazardousReactive',
                                         'WCHazardousToxic']
            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                label_data_map = {'No': 0, 'Yes': 1}
                response = dict()
                response[output_column_name] = list(label_data_map.keys())[predictions[i][0].round().astype(int)]
                responses.append(response)

            return HttpResponse(json.dumps(responses))
