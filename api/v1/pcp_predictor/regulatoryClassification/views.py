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
            RegulatoryClassification_Model = WpcpredictorConfig.RegulatoryClassification_Model

            models = [RegulatoryClassification_Model]

            inputJson = json.loads(request.body)
            inputText = (inputJson['profileName'] + ' is ' + inputJson[
                'processGeneratingWaste'] + ' with those compositions ' + inputJson[
                             'chemicalPhysicalComposition'])

            predictions = []
            for model in models:
                predictions.append(model.predict(np.array([inputText]))[0])

            output_columns = ['RegulatoryClassification']

            responses = []
            for i in range(len(output_columns)):
                mlb = pickle.loads(open('api/WPCPredictor/models/PCP_Models/mlb/regulatory_classification_mlb.pkl', "rb").read())
                argmax = np.argsort(predictions[i])[::-1]
                for (t, j) in enumerate(argmax):
                    response = dict()
                    response[mlb.classes_[j]] = f"{predictions[i][j] * 100:.2f}%"
                    responses.append(response)

            return HttpResponse(json.dumps(responses))
