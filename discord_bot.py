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
                author_id = message['author']['id']  # Obtener el ID del autor
                author_username = message['author']['username']
                content = message['content']
                messages_info.append((author_id, author_username, content))
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
    def kick_user(self, userId, serverId):
        req = requests.delete(f"https://discord.com/api/v9/guilds/{serverId}/members/{userId}", headers={"Authorization":self.token})
        return req.content
    def ban_user(self, userId, serverId):
        req = requests.put(f"https://discord.com/api/v9/guilds/{serverId}/bans/{userId}", headers={"Authorization":self.token})
        return req.content
    def set_state(self, state, sexit:False):
        req = requests.patch(f"https://discord.com/api/v9/users/@me/settings-proto/1", headers={"Authorization":self.token}, json={"settings":state})
        if sexit:
            exit()
        return req.content
def load_config():
    config = {}
    with open('config.txt', 'r') as file:
        for line in file:
            if '=' in line:
                key, value = line.strip().split('=')
                config[key] = value
    return config
 