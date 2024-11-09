# discord_methods.py
import requests
import json
import time

class DiscordBot:
    def __init__(self, token: str, channel_id: str):
        self.token = token
        self.channel_id = channel_id

    def send_message(self, text: str):
        url = f"https://discord.com/api/v9/channels/{self.channel_id}/messages"
        headers = {
            "Authorization": f"{self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "content": text
        }
        re = requests.post(url, headers=headers, data=json.dumps(data))

    def get_messages(self, limit):
        url = f"https://discord.com/api/v9/channels/{self.channel_id}/messages?limit={limit}"
        headers = {
            "Authorization": f"{self.token}", 
            "Content-Type": "application/json"
        }
        re = requests.get(url, headers=headers)

        if re.status_code == 200:
            messages = re.json()
            messages_info = []
            for message in messages:
                messages_info.append((message['author']['username'], message['content']))
            return messages_info
        else:
            print(f"Error al obtener mensajes: {re.status_code}")
            return None  
    def typing(self):
        requests.post(f"https://discord.com/api/v9/channels/{self.channel_id}/typing", headers={"Authorization":f"{self.token}"})
    def start_message_loop(self, interval: int = 1):
        while True:
            messages = self.get_messages()
            if messages:
                for user, content in messages:
                    print(f"Mensaje de {user}: {content}")
            time.sleep(interval)
    def get_username(self):
        req = requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization":self.token})
        return req.json().get("username")
def load_config():
    config = {}
    with open('config.txt', 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                config[key] = value
    return config
 