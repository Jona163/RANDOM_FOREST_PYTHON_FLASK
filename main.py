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
