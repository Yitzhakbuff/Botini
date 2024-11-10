import requests
import json

# Tu clave de API para acceder a Gemini (asegúrate de configurarla correctamente)
API_KEY = 'tu_api_key_aqui'

# URL de la API de Gemini (esto podría cambiar, asegúrate de tener la URL correcta)
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?"

# Los parámetros que quieres configurar para el modelo (ajusta según lo necesario)
params = {
    "model": "gemini_latest_model",  # Nombre del modelo más reciente de Gemini
    "tokens": 2048,  # Número de tokens para el input/output
    "temperature": 0.7,  # Controla la aleatoriedad en las respuestas
    "systemIntegration": True,  # Integración del sistema, ejemplo de configuración
    "top_p": 1.0,  # Valor para nucleus sampling (para controlar diversidad)
    "frequency_penalty": 0.0,  # Penalización de frecuencia (para evitar repetición excesiva)
    "presence_penalty": 0.0,  # Penalización de presencia (para evitar respuestas poco relevantes)
}

# Encabezados de la solicitud, incluyendo el token de autorización
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Realizar la solicitud POST a la API de Gemini
response = requests.post(url, headers=headers, data=json.dumps(params))

# Verificar el estado de la solicitud y los resultados
if response.status_code == 200:
    print("Modelo configurado exitosamente:")
    print(response.json())
else:
    print(f"Error al configurar el modelo: {response.status_code}")
    print(response.text)
