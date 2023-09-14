import array
import json

from rest_framework.response import Response

from api.WPCPredictor.apps import WpcpredictorConfig
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
import numpy as np


cluster_2 = [2008, 2118, 2119]
cluster_3 = [2109, 7004]
cluster_4 = [2006, 2110]  # 2111
cluster_5 = [2910, 2901, 2911, 2912, 2913, 3020, 3021, 2107]  # 3078
cluster_6 = [2001, 2051, 2052, 2053, 3015]  # 3960, 3959, 3958
cluster_7 = [3020, 2121, 3622, 3615, 3616]  # 2108
cluster_8 = [3003, 3004, 3009]  # 3005, 3052, 3095, 3096
cluster_9 = [7500, 7042]
cluster_10 = [2001, 2051, 2052, 2053, 2002, 3016]
cluster_11 = [3000, 3001, 3002, 3025, 3031, 3032, 3101, 3102, 3103, 3600, 3601, 3603, 3604, 3617, 3620, 3621]
cluster_12 = [2005, 6700]
cluster_13 = [3050, 3012, 3608]
cluster_14 = [3051, 3012, 3607]
cluster_15 = [2000, 6700, 3094]
cluster_16 = [7005, 2005, 7002, 5100, 7000, 7030, 7001, 7003]
cluster_17 = [3104, 3105, 3619]
cluster_18 = [3006, 3007, 3008, 2002]
cluster_19 = [3015, 3016, 3017, 3018, 3093, 3609, 3820, 3821, 3822, 3823, 3825, 3826]  # 3824, 3827
cluster_20 = [3802, 3092]
cluster_21 = [3801, 3091]
cluster_22 = [2003, 2004, 2102]
cluster_23 = [3800, 3090]
cluster_24 = [2101, 2106, 3019, 2150, 2151, 6700]
cluster_25 = [2118, 2119, 2008]
cluster_26 = [2110, 2006]  # 2111
cluster_27 = [2009, 2010]
cluster_28 = [2109, 7004]
cluster_29 = [7200, 7201]
cluster_30 = [7200, 7201, 7203, 7204, 7205, 7206]


class call_model(APIView):
    def post(self, request):
        global scaler, model, clusterWPCs
        if request.method == 'POST':
            inputJson = json.loads(request.body)
            WPCs = np.array(inputJson['wpc'])
            qa = inputJson['qa']
            if set(map(str, cluster_2)).issubset(set(WPCs)):
                clusterWPCs = cluster_2
                scaler = WpcpredictorConfig.scaler_2
                model = WpcpredictorConfig.model_2
            elif set(map(str, cluster_3)).issubset(set(WPCs)):
                clusterWPCs = cluster_3
                scaler = WpcpredictorConfig.scaler_3
                model = WpcpredictorConfig.model_3
            elif set(map(str, cluster_4)).issubset(set(WPCs)):
                clusterWPCs = cluster_4
                scaler = WpcpredictorConfig.scaler_4
                model = WpcpredictorConfig.model_4
            elif set(map(str, cluster_5)).issubset(set(WPCs)):
                clusterWPCs = cluster_5
                scaler = WpcpredictorConfig.scaler_5
                model = WpcpredictorConfig.model_5
            elif set(map(str, cluster_6)).issubset(set(WPCs)):
                clusterWPCs = cluster_6
                scaler = WpcpredictorConfig.scaler_6
                model = WpcpredictorConfig.model_6
            elif set(map(str, cluster_7)).issubset(set(WPCs)):
                clusterWPCs = cluster_7
                scaler = WpcpredictorConfig.scaler_7
                model = WpcpredictorConfig.model_7
            elif set(map(str, cluster_8)).issubset(set(WPCs)):
                clusterWPCs = cluster_8
                scaler = WpcpredictorConfig.scaler_8
                model = WpcpredictorConfig.model_8
            elif set(map(str, cluster_9)).issubset(set(WPCs)):
                clusterWPCs = cluster_9
                scaler = WpcpredictorConfig.scaler_9
                model = WpcpredictorConfig.model_9
            elif set(map(str, cluster_10)).issubset(set(WPCs)):
                clusterWPCs = cluster_10
                scaler = WpcpredictorConfig.scaler_10
                model = WpcpredictorConfig.model_10
            elif set(map(str, cluster_11)).issubset(set(WPCs)):
                clusterWPCs = cluster_11
                scaler = WpcpredictorConfig.scaler_11
                model = WpcpredictorConfig.model_11
            elif set(map(str, cluster_12)).issubset(set(WPCs)):
                clusterWPCs = cluster_12
                scaler = WpcpredictorConfig.scaler_12
                model = WpcpredictorConfig.model_12
            elif set(map(str, cluster_13)).issubset(set(WPCs)):
                clusterWPCs = cluster_13
                scaler = WpcpredictorConfig.scaler_13
                model = WpcpredictorConfig.model_13
            elif set(map(str, cluster_14)).issubset(set(WPCs)):
                clusterWPCs = cluster_14
                scaler = WpcpredictorConfig.scaler_14
                model = WpcpredictorConfig.model_14
            elif set(map(str, cluster_15)).issubset(set(WPCs)):
                clusterWPCs = cluster_15
                scaler = WpcpredictorConfig.scaler_15
                model = WpcpredictorConfig.model_15
            elif set(map(str, cluster_16)).issubset(set(WPCs)):
                clusterWPCs = cluster_16
                scaler = WpcpredictorConfig.scaler_16
                model = WpcpredictorConfig.model_16
            elif set(map(str, cluster_17)).issubset(set(WPCs)):
                clusterWPCs = cluster_17
                scaler = WpcpredictorConfig.scaler_17
                model = WpcpredictorConfig.model_17
            elif set(map(str, cluster_18)).issubset(set(WPCs)):
                clusterWPCs = cluster_18
                scaler = WpcpredictorConfig.scaler_18
                model = WpcpredictorConfig.model_18
            elif set(map(str, cluster_19)).issubset(set(WPCs)):
                clusterWPCs = cluster_19
                scaler = WpcpredictorConfig.scaler_19
                model = WpcpredictorConfig.model_19
            elif set(map(str, cluster_20)).issubset(set(WPCs)):
                clusterWPCs = cluster_20
                scaler = WpcpredictorConfig.scaler_20
                model = WpcpredictorConfig.model_20
            elif set(map(str, cluster_21)).issubset(set(WPCs)):
                clusterWPCs = cluster_21
                scaler = WpcpredictorConfig.scaler_21
                model = WpcpredictorConfig.model_21
            elif set(map(str, cluster_22)).issubset(set(WPCs)):
                clusterWPCs = cluster_22
                scaler = WpcpredictorConfig.scaler_22
                model = WpcpredictorConfig.model_22
            elif set(map(str, cluster_23)).issubset(set(WPCs)):
                clusterWPCs = cluster_23
                scaler = WpcpredictorConfig.scaler_23
                model = WpcpredictorConfig.model_23
            elif set(map(str, cluster_24)).issubset(set(WPCs)):
                clusterWPCs = cluster_24
                scaler = WpcpredictorConfig.scaler_24
                model = WpcpredictorConfig.model_24
            elif set(map(str, cluster_25)).issubset(set(WPCs)):
                clusterWPCs = cluster_25
                scaler = WpcpredictorConfig.scaler_25
                model = WpcpredictorConfig.model_25
            elif set(map(str, cluster_26)).issubset(set(WPCs)):
                clusterWPCs = cluster_26
                scaler = WpcpredictorConfig.scaler_26
                model = WpcpredictorConfig.model_26
            elif set(map(str, cluster_27)).issubset(set(WPCs)):
                clusterWPCs = cluster_27
                scaler = WpcpredictorConfig.scaler_27
                model = WpcpredictorConfig.model_27
            elif set(map(str, cluster_28)).issubset(set(WPCs)):
                clusterWPCs = cluster_28
                scaler = WpcpredictorConfig.scaler_28
                model = WpcpredictorConfig.model_28
            elif set(map(str, cluster_29)).issubset(set(WPCs)):
                clusterWPCs = cluster_29
                scaler = WpcpredictorConfig.scaler_29
                model = WpcpredictorConfig.model_29
            elif set(map(str, cluster_30)).issubset(set(WPCs)):
                clusterWPCs = cluster_30
                scaler = WpcpredictorConfig.scaler_30
                model = WpcpredictorConfig.model_30

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
            for i in range(len(clusterWPCs)):
                response = dict()
                response["wpc"] = clusterWPCs[i]
                response["percentage"] = f'{prediction[0][i] * 100:.2f}'
                responses.append(response)

            return HttpResponse(json.dumps(responses))
