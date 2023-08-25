import os

from django.apps import AppConfig
from django.conf import settings
import tensorflow as tf
import joblib


class WpcpredictorConfig(AppConfig):
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
    name = 'api.WPCPredictor'
