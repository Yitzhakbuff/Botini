import requests
import time
from discord_bot import DiscordBot, load_config
import ai
import random
import debug
import re


def start_bot():
    config = load_config()
    bot = DiscordBot(config.get('token'), config.get('channel_id'))
    api = debug.prompt("Escribe la API: ")

    exceptuser = bot.get_username()
    #bot.kick_user(userId="1211468961623965727", serverId="1305226403247030382")
    lastmessage = ""
    bot.set_state(state="WgoKCAoGb25saW5l", sexit=False)
    inServer = bool(config.get('server_id'))
    while True:
        messages = bot.get_messages(limit=1)
        context_messages = bot.get_messages(limit=3)
        context = ""
        if context_messages:
            for author_id, user, content in reversed(context_messages):  # Ahora recibe los tres valores
                if user == exceptuser:
                    context += f"Tu escribiste: {content}\n"
                else:
                    context += f"(Otro usuario) (ID del Usuario: {author_id}){user}: {content}\n"
        if messages:
            for author_id,user, content in messages:
                if user == exceptuser:
                    continue
                content = content.replace('\n', ' ')

                if content != lastmessage:
                    print(f"\x1b[38;5;46m▀ - \x1b[38;5;56m{user}: \x1b[38;5;254m{content} (\x1b[38;5;206mID: {author_id}\x1b[38;5;254m)")
                    #time.sleep(random.uniform(0.5, 1.5))
                    bot.typing()
                    ai_response = ai.get_ai_response(api, content, context)
                    ai_response = ai_response.replace('\n', ' ')
                    char_delay = 0.015
                    typing_time = len(ai_response) * char_delay
                    time.sleep(typing_time)
                    bot.send_message(ai_response)
                    if "/inactk" in ai_response: #to add friends commands, but its patched
                        bot.set_state(state="Wg0KCwoJaW52aXNpYmxl", sexit=True)
                        ai_response = ai_response.replace("/inactk", "")
                    if (inServer):
                        if "/kick" in ai_response:
                            # Intenta extraer el ID usando una expresión regular después de "/kick"
                            match = re.search(r"/kick (\d+)", ai_response)
                            if match:
                                user_id = match.group(1)
                                bot.kick_user(userId=user_id, serverId=config.get('server_id'))

                        if "/ban" in ai_response:
                            # Intenta extraer el ID usando una expresión regular después de "/ban"
                            match = re.search(r"/ban (\d+)", ai_response)
                            if match:
                                user_id = match.group(1)
                                bot.ban_user(userId=user_id, serverId=config.get('server_id'))

                    lastmessage = content
                    debug.info("\x1b[38;5;242mLast history:")
                    print(context)
                else:
                    debug.warn("el mensaje es repetido")
        time.sleep(0.4)
def main():
    debug.clear()
    debug.title()
    print("\n\n\t\t\t\t\t\x1b[38;5;23m1. \x1b[38;5;130mEmpezar bot")
    print("\t\t\t\t\t\x1b[38;5;23m2. \x1b[38;5;130mConfigurar bot")
    
    print("\t\t\t\t\t\x1b[38;5;23m3. \x1b[38;5;130mSalir\n")
    select = debug.prompt(">> \x1b[38;5;23m")
    if select == "1":
        start_bot()
if __name__ == "__main__":
    main()