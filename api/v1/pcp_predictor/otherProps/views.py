import array
import json
import pickle

from rest_framework.response import Response

from api.WPCPredictor.apps import WpcpredictorConfig
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
import numpy as np


class call_model(APIView):
    def post(self, request):
        if request.method == 'POST':
            NumberOfPhasesLayer_Model = WpcpredictorConfig.NumberOfPhasesLayer_Model
            OtherProps_Model = WpcpredictorConfig.OtherProps_Model

            models = [NumberOfPhasesLayer_Model, OtherProps_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['NumberOfPhases_Layer', 'Other_props']

            responses = []
            for i in range(len(output_columns)):
                output_column_name = output_columns[i]
                response = dict()
                if output_column_name == 'NumberOfPhases_Layer':
                    label_data_map = {1: 0, 2: 1, 3: 2}
                    response[output_column_name] = list(label_data_map.keys())[np.argmax(predictions[i])]
                    responses.append(response)
                else:
                    mlb = pickle.loads(open('api/WPCPredictor/models/PCP_Models/mlb/other_props_mlb.pkl', "rb").read())
                    argmax = np.argsort(predictions[i])[::-1]
                    for (t, j) in enumerate(argmax):
                        response = dict()
                        response[mlb.classes_[j]] = f"{predictions[i][j] * 100:.2f}%"
                        responses.append(response)

            return HttpResponse(json.dumps(responses))
