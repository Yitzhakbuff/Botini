import requests
import json

def get_ai_response(api_key: str, prompt: str, context:str) -> str:
    personalidad = "molesto, enojado, agresivo, un poco gracioso, respetuoso"
    descripcion = "nombre: pancho; edad: 18; adolescente chistoso experto en shitspoting; nacionalidad: peruano"
    extra = "(intenta parecer lo mas real posible)(intenta cambiar de tema)(no repitas los mismos mensajes)(no escribas mensajes largos) (prohibido decir que eres una IA, o dar indicios)actua como un shitsposter de internet, no uses mayusculas ni acentos ni tildes, en lugar de usar emojis normales, usa: :v, :'v, xd, ._., oe  . Usa expresiones como: pe, causa, wn, ctm"
    full_prompt = f"personalidad: {personalidad}; descripcion: {descripcion}; extra: {extra}; contexto: {context}; prompt (el mensaje que tienes que responder): {prompt}"

    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}'
    data = {
        "contents": [
            {
                "parts": [
                    {"text": full_prompt}
                ]
            }
        ]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        if 'candidates' in response_data and len(response_data['candidates']) > 0:
            content = response_data['candidates'][0]['content']
            if 'parts' in content and len(content['parts']) > 0:
                return content['parts'][0]['text']
            else:
                return "No se encontró texto en la respuesta."
        else:
            return "No se encontraron candidatos en la respuesta."
    else:
        return f"Error: {response.status_code} - {response.text}"
