import os

from django.apps import AppConfig
from django.conf import settings
import tensorflow as tf
import joblib


class WpcpredictorConfig(AppConfig):
    scaler_2 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_2.save'))
    scaler_3 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_3.save'))
    scaler_6 = joblib.load(os.path.join(settings.MODELS, 'scalers/cluster_6.save'))

    model_2 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_2'))
    model_3 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_3'))
    model_6 = tf.keras.models.load_model(os.path.join(settings.MODELS, 'cluster_6'))
    name = 'api.WPCPredictor'
