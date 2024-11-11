import requests
import json
from discord_bot import load_config

def get_ai_response(api_key: str, prompt: str, context: str) -> str:
    # Cargar la configuración desde el archivo
    config = load_config()
    personalidad = config.get('personalidad', '')
    descripcion = config.get('descripcion', '')
    extra = config.get('extra', '')
    comandos = config.get('comandos', '')
    temperature = config.get('temperature', '')
    topK = config.get('topK', '')
    topP =config.get('topP', '')

    # Construir el 'full_prompt' con la información completa
    full_prompt = f" descripcion: {descripcion}; extra: {extra}; comandos: {comandos}; contexto: {context}; prompt (el mensaje que tienes que responder): {prompt}"

    # Definir la URL y el cuerpo de la solicitud
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}'

    data = {
        "contents": [
            {
                "role": "user", 
                "parts": [
                    {
                        "text": full_prompt
                    }
                ]
            }
        ],
        "systemInstruction": {
            "role": "model", 
            "parts": [
                {
                    "text": personalidad
                }
            ]
        },
        "generationConfig": {
            "temperature": temperature,
            "topK": topK,
            "topP": topP,
            "maxOutputTokens": 8192,
            "responseMimeType": "text/plain"
        }
    }

    # Configurar los encabezados
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Realizar la solicitud POST
    response = requests.post(url, headers=headers, json=data)
    
    # Comprobar la respuesta
    if response.status_code == 200:
        try:
            response_data = response.json()
            if 'candidates' in response_data and len(response_data['candidates']) > 0:
                content = response_data['candidates'][0].get('content', {})
                if 'parts' in content and len(content['parts']) > 0:
                    return content['parts'][0]['text']
                else:
                    return "No se encontró texto en la respuesta."
            else:
                print(response.content)
                return "No se encontraron candidatos en la respuesta."
        except Exception as e:
            return f"Error al procesar la respuesta: {str(e)}"
    else:
        return f"Error: {response.status_code} - {response.text}"

