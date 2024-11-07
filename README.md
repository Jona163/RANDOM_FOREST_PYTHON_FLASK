

# 🌲 RANDOM_FOREST_PYTHON_FLASK 🌲

**¡Bienvenidos a la selva del Machine Learning!** Aquí verás cómo se integra un modelo de Random Forest en Python junto con Flask para desplegar el servicio. Con este repositorio, aprenderás cómo hacer que tus árboles se alineen en el bosque del aprendizaje automático y servir resultados listos para su uso. 🌐🌳

---

## 📌 Descripción

Este proyecto combina la potencia de **Random Forest**, un algoritmo de Machine Learning para clasificación y regresión, con **Flask**, un micro-framework de Python ideal para desplegar modelos de manera rápida y sencilla. Aquí podrás:

- Entrenar un modelo de Random Forest con tus propios datos.
- Implementar el modelo y acceder a predicciones a través de una API en Flask.
- Explorar y personalizar el código para tus propios proyectos de ML en producción.

---

## 🚀 Empezando

Sigue estos pasos para poner a andar el proyecto en tu máquina local:

### 1. Clona el repositorio
```bash
git clone https://github.com/Jona163/RANDOM_FOREST_PYTHON_FLASK.git
cd RANDOM_FOREST_PYTHON_FLASK
```

### 2. Crea un entorno virtual e instala dependencias
```bash
python -m venv env
source env/bin/activate  # En Windows usa env\Scripts\activate
pip install -r requirements.txt
```

### 3. Corre el servicio de Flask
```bash
python app.py
```

¡Listo! Flask estará corriendo en `http://127.0.0.1:5000/` y podrás hacer peticiones a la API. ✨

---

## 🔧 Uso

La API recibe datos en JSON y responde con predicciones generadas por el modelo Random Forest. Ejemplo de uso:

### Request
```json
{
    "input_data": [valores, aquí]
}
```

### Response
```json
{
    "prediction": "resultado_clasificación"
}
```

---

## 📁 Estructura del Proyecto

```plaintext
RANDOM_FOREST_PYTHON_FLASK/
├── app.py                 # Código principal de Flask
├── dasets/malware         # Script para entrenar y cargar el modelo Random Forest
├── requirements.txt       # Librerías necesarias
└── README.md              # ¡Este archivo que estás leyendo ahora!
```

---

## 🛠 Tecnologías

- **Python** - Para la implementación del modelo de Machine Learning.
- **Flask** - Framework para crear la API de acceso al modelo.
- **scikit-learn** - Librería utilizada para el modelo de Random Forest.

---

## 🎯 Próximos Pasos

Algunas ideas para extender el proyecto:
- 🎨 Crear una interfaz gráfica que permita hacer predicciones desde una app web.
- 📊 Incluir visualizaciones para analizar el rendimiento del modelo.
- 🧠 Añadir más algoritmos de Machine Learning.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Abre un PR o crea una Issue si tienes alguna idea o encuentras un error.

---

## 📝 Licencia

Este proyecto se distribuye bajo la licencia MIT. 

---

¡Gracias por visitar! 🙌
