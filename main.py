#Importaciones
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from flask import Flask, jsonify, render_template
import matplotlib.pyplot as plt
import io
import base64

# Inicializar la aplicación Flask
app = Flask(__name__)

# Función para cargar y procesar el dataset
def load_and_process_data():
    # Leer el dataset
    df = pd.read_csv("datasets/TotalFeatures-ISCXFlowMeter.csv")

    # Dividir el DataSet en entrenamiento, validación y test
    def train_val_test_split(df, rstate=42, shuffle=True, stratify=None):
        strat = df[stratify] if stratify else None
        train_set, test_set = train_test_split(
            df, test_size=0.4, random_state=rstate, shuffle=shuffle, stratify=strat)
        strat = test_set[stratify] if stratify else None
        val_set, test_set = train_test_split(
            test_set, test_size=0.5, random_state=rstate, shuffle=shuffle, stratify=strat)
        return train_set, val_set, test_set

    train_set, val_set, test_set = train_val_test_split(df)
    X_train, y_train = train_set.drop('calss', axis=1), train_set['calss']
    X_val, y_val = val_set.drop('calss', axis=1), val_set['calss']
    X_test, y_test = test_set.drop('calss', axis=1), test_set['calss']

    # Codificación de las etiquetas
    label_encoder = LabelEncoder()
    y_train_encoded = label_encoder.fit_transform(y_train)
    y_val_encoded = label_encoder.transform(y_val)
    y_test_encoded = label_encoder.transform(y_test)

    # Escalado de los datos
    scaler = RobustScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_val_scaled = scaler.transform(X_val)
    X_test_scaled = scaler.transform(X_test)
