import os

from django.apps import AppConfig
from django.conf import settings
import tensorflow as tf
import joblib


class WpcpredictorConfig(AppConfig):
    ohe = joblib.load(os.path.join(settings.MODELS, 'OneHotEncoder/ohe.save'))

    scaler_1 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_1.save'))
    scaler_2 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_2.save'))
    scaler_3 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_3.save'))
    scaler_4 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_4.save'))
    scaler_5 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_5.save'))
    scaler_6 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_6.save'))
    scaler_7 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_7.save'))
    scaler_8 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_8.save'))
    scaler_9 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_9.save'))
    scaler_10 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_10.save'))
    scaler_11 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_11.save'))
    scaler_12 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_12.save'))
    scaler_13 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_13.save'))
    scaler_14 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_14.save'))
    scaler_15 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_15.save'))
    scaler_16 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_16.save'))
    scaler_17 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_17.save'))
    scaler_18 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_18.save'))
    scaler_19 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_19.save'))
    scaler_20 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_20.save'))
    scaler_21 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_21.save'))
    scaler_22 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_22.save'))
    scaler_23 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_23.save'))
    scaler_24 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_24.save'))
    scaler_25 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_25.save'))
    scaler_26 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_26.save'))
    scaler_27 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_27.save'))
    scaler_28 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_28.save'))
    scaler_29 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_29.save'))
    scaler_30 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_30.save'))
    scaler_31 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_31.save'))
    scaler_32 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_32.save'))
    scaler_33 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_33.save'))
    scaler_34 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_34.save'))

    model_1 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_1'))
    model_2 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_2'))
    model_3 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_3'))
    model_4 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_4'))
    model_5 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_5'))
    model_6 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_6'))
    model_7 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_7'))
    model_8 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_8'))
    model_9 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_9'))
    model_10 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_10'))
    model_11 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_11'))
    model_12 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_12'))
    model_13 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_13'))
    model_14 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_14'))
    model_15 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_15'))
    model_16 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_16'))
    model_17 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_17'))
    model_18 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_18'))
    model_19 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_19'))
    model_20 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_20'))
    model_21 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_21'))
    model_22 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_22'))
    model_23 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_23'))
    model_24 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_24'))
    model_25 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_25'))
    model_26 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_26'))
    model_27 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_27'))
    model_28 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_28'))
    model_29 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_29'))
    model_30 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_30'))
    model_31 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_31'))
    model_32 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_32'))
    model_33 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_33'))
    model_34 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_34'))

    # PCP Models
    PCPViscosity_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/PCPViscosity_Model'))
    PCPBTUValue_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/PCPBTUValue_Model'))
    PCpH_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/PCpH_Model'))
    PCFlashPoint_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/PCFlashPoint_Model'))
    PCFlashPoint_Method_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models'
                                                                                         '/PCFlashPoint_Method_Model'))
    # regulatory
    WCHazardousF_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/WCHazardousF_Model'))
    WCHazardousK_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/WCHazardousK_Model'))
    WCHazardousP_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/WCHazardousP_Model'))
    WCHazardousU_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/WCHazardousU_Model'))
    WCHazardousIgnitable_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/WCHazardousIgnitable_Model'))
    WCHazardousCorrosive_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/WCHazardousCorrosive_Model'))
    WCHazardousReactive_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/WCHazardousReactive_Model'))
    WCHazardousToxic_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/WCHazardousToxic_Model'))

    # hazardousWaste
    HazardousWaste_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/HazardousWaste_Model'))
    RCRAExempt_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/RCRAExempt_Model'))
    WCHazardous_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/WCHazardous_Model'))

    # chemColorOdor
    Color_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/Color_Model'))
    Odor_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/Odor_Model'))
    BoilingPoint_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/Boiling Point_Model'))
    TotalOrganicCarbon_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/Total Organic Carbon_Model'))
    Viscosity_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/Viscosity_Model'))
    SpecificGravity_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/Specific Gravity_Model'))

    # chemRegulatory
    RestrictedUnderLDR_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/Restricted Under LDR_Model'))
    UHCs_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/UHCs_Model'))
    PPMVOC500_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/500 PPM VOC_Model'))
    AlternativeStandardsOfSoil_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/Alternative Standards of Soil_Model'))
    LDRSubcategory_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/LDR Subcategory_Model'))

    # phyState
    PhyState_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/PhyState_Model'))

    # other_props
    NumberOfPhasesLayer_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/NumberOfPhases_Layer_Model'))
    OtherProps_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/Other_props_Model'))\

    # regulatoryClassification
    RegulatoryClassification_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/RegulatoryClassification_Model'))

    # regulatoryEPA
    EPASourceCode_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/EPASourceCode_Model'))
    OriginCode_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/OriginCode_Model'))
    EPAFormCode_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/EPAFormCode_Model'))

    # shippingInfo
    ShippingAndPackagingFrequency_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/ShippingAndPackagingFrequency_Model'))
    ShippingAndPackagingWasteCombination_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/ShippingAndPackagingWasteCombination_Model'))
    TransportationRequirement_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/TransportationRequirement_Model'))

    # landBan
    TreatmentStandard_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/TreatmentStandard_Model'))

    # UNNumber
    UNNumber_Model = tf.keras.models.load_model(os.path.join(settings.MODELS, 'PCP_Models/UN Number_Model'))

    name = 'api.WPCPredictor'
