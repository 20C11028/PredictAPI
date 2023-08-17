import array
import json

from rest_framework.response import Response

from api.WPCPredictor.apps import WpcpredictorConfig
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
import numpy as np


class call_model(APIView):
    def post(self, request):
        global scaler, model
        if request.method == 'POST':
            input = json.loads(request.body)
            WPCs = np.array(input['wpc'])
            qa = input['qa']
            cluster = 0
            if ('2008' in WPCs) & ('2118' in WPCs) & ('2119' in WPCs):
                cluster = 2
            elif ('2109' in WPCs) & ('7004' in WPCs):
                cluster = 3
            elif ('2006' in WPCs) & ('2110' in WPCs):
                cluster = 4
            elif ('2910' in WPCs) & ('2901' in WPCs) & ('2911' in WPCs) & ('2912' in WPCs) & ('2913' in WPCs) \
                    & ('3020' in WPCs) & ('3021' in WPCs) & ('2107' in WPCs):
                cluster = 5
            elif ('2001' in WPCs) & ('2051' in WPCs) & ('2052' in WPCs) & ('2053' in WPCs):
                cluster = 6
            features = ['PCPDensity', 'PCPhysicalStateSolid2', 'PCPPhysicalStateLiquid2', 'PCPPhysicalStateSludge2',
                            'PCPPhysicalStateGas2', 'PCPPhysicalStateAsh2', 'PCPPhysicalStatePowder2',
                            'PCPPhysicalStateSolidPercent', 'PCPPhysicalStateLiquidPercent',
                            'PCPPhysicalStateSludgePercent', 'PCPPhysicalStateGasPercent', 'PCPPhysicalStateAshPercent',
                            'PCPPhysicalStatePowderPercent', 'PCPOtherPropertiesExplosive',
                            'PCPOtherPropertiesRadioactive', 'PCPOtherPropertiesThermallyUnstable',
                            'PCPOtherPropertiesShockSensitive',
                            'PCPOtherPropertiesPyrophoric', 'PCPOtherPropertiesOxidizer',
                            'PCPOtherPropertiesWaterReactive',
                            'PCPOtherPropertiesAirReactive', 'PCPOtherPropertiesReactiveCyanides',
                            'PCPOtherPropertiesReactiveSulfides', 'PCPOtherPropertiesPolymerizable',
                            'PCPOtherPropertiesPolymerizableInhibited', 'PCPOtherPropertiesAbestosFriable',
                            'PCPOtherPropertiesAbestosNonFriable', 'PCPOtherPropertiesMetalFines',
                            'PCPOtherPropertiesOrganaicPeroxides', 'PCPOtherPropertiesDioxins',
                            'PCPOtherPropertiesFurans',
                            'PCPOtherPropertiesNORM', 'PCPOtherPropertiesBiohazard', 'PCPOtherPropertiesNONE',
                            'RegulatoryRestrictedUnderLDR', 'RegulatoryUHCs', 'Regulatory500PPMVOC',
                            'RegulatoryAlternativeStandardsofSoil', 'PCPPhysicalStateSemiSolid2',
                            'PCPPhysicalStateSemiSolidPercent', 'PCNumberOfPhases_Layer', 'PCNumberOfPhases_Layer_Mid',
                            'PCPOtherPropertiesPesticides', 'subfield_for_copy', 'Min', 'Max',
                            'ShippingAndPackagingUSDOT',
                            'GenericFlag', 'RQFlag', 'MixtureFlag', 'SolutionFlag',
                            'ShippingAndPackagingWasteCombination',
                            'TransBulkType_Other', 'TransBulkType_Railcar', 'TransBulkType_RollOff',
                            'TransBulkType_TankTruck', 'TransBulkType_VacBox', 'TransContainer_BoxCartonCase',
                            'TransContainer_CubicYardBox', 'TransContainer_Drum', 'TransContainer_Other',
                            'TransContainer_PortableToteTank', 'WCHazardous', 'WCHazardousF', 'WCHazardousK',
                            'WCHazardousP', 'WCHazardousU', 'WCHazardousIgnitable', 'WCHazardousCorrosive',
                            'WCHazardousReactive', 'WCHazardousToxic', 'UniversalWaste', 'UsedOil',
                            'TSCARegulatedPCBWaste',
                            'HazardousWaste', 'RCRAExempt', 'CERCLARegulatedWaste', 'BenzeneNESHAPWaste',
                            'HalogenatedOrganicCompound', 'WasteDeterminationBasedOn',
                            'WasteDetermination_GenKnowledge',
                            'WasteDetermination_SDS', 'WasteDetermination_WasteAnylysis', 'CaliforniaStateWasteCode',
                            'IsNoSampleTaken', 'Is_US_EPA40_CFR26120', 'StateUniversalWaste', 'product_or_coproduct',
                            'recycle_or_reuse', 'OneTimeNumberNeeded', 'MedicalWaste',
                            'regulatory_information_edited_fields']
            if cluster == 2:
                scaler = WpcpredictorConfig.scaler_2
                model = WpcpredictorConfig.model_2

            elif cluster == 3:
                scaler = WpcpredictorConfig.scaler_3
                model = WpcpredictorConfig.model_3

            elif cluster == 4:
                scaler = WpcpredictorConfig.scaler_4
                model = WpcpredictorConfig.model_4

            elif cluster == 5:
                scaler = WpcpredictorConfig.scaler_5
                model = WpcpredictorConfig.model_5

            elif cluster == 6:
                scaler = WpcpredictorConfig.scaler_6
                model = WpcpredictorConfig.model_6

            inputQA = np.array([])
            for f in features:
                f = qa[f]
                if (f == 'Yes') | (f == 'True'):
                    f = 1
                elif (f == 'No') | (f == 'False'):
                    f = 0
                elif f == '':
                    f = 0
                inputQA = np.append(inputQA, f)
            inputQA = inputQA.astype(float)
            vector = scaler.transform([inputQA])
            prediction = model.predict(vector)
            responses = []
            if cluster == 2:
                cluster_wpcs = [2008, 2118, 2119]
                for i in range(len(cluster_wpcs)):
                    # response[cluster_wpcs[i]] = f'{prediction[0][i] * 100:.2f}%'
                    response = dict()
                    response["wpc"] = cluster_wpcs[i]
                    response["percentage"] = f'{prediction[0][i] * 100:.2f}'
                    responses.append(response)
            elif cluster == 3:
                cluster_wpcs = [2109, 7004]
                for i in range(len(cluster_wpcs)):
                    # response[cluster_wpcs[i]] = f'{prediction[0][i] * 100:.2f}%'
                    response = dict()
                    response["wpc"] = cluster_wpcs[i]
                    response["percentage"] = f'{prediction[0][i] * 100:.2f}'
                    responses.append(response)
            elif cluster == 4:
                cluster_wpcs = [2006, 2110]
                for i in range(len(cluster_wpcs)):
                    # response[cluster_wpcs[i]] = f'{prediction[0][i] * 100:.2f}%'
                    response = dict()
                    response["wpc"] = cluster_wpcs[i]
                    response["percentage"] = f'{prediction[0][i] * 100:.2f}'
                    responses.append(response)
            elif cluster == 5:
                cluster_wpcs = [2910, 2901, 2911, 2912, 2913, 3020, 3021, 2107]
                for i in range(len(cluster_wpcs)):
                    # response[cluster_wpcs[i]] = f'{prediction[0][i] * 100:.2f}%'
                    response = dict()
                    response["wpc"] = cluster_wpcs[i]
                    response["percentage"] = f'{prediction[0][i] * 100:.2f}'
                    responses.append(response)
            elif cluster == 6:
                cluster_wpcs = [2001, 2051, 2052, 2053]
                for i in range(len(cluster_wpcs)):
                    # response[cluster_wpcs[i]] = f'{prediction[0][i] * 100:.2f}%'
                    response = dict()
                    response["wpc"] = cluster_wpcs[i]
                    response["percentage"] = f'{prediction[0][i] * 100:.2f}'
                    responses.append(response)

            return HttpResponse(json.dumps(responses))
