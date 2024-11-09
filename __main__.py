import requests
import time
from discord_bot import DiscordBot, load_config
import ai
import random
import debug


def start_bot():
    config = load_config()
    bot = DiscordBot(config.get('token'), config.get('channel_id'))
    api = debug.prompt("Escribe la API: ")

    exceptuser = bot.get_username()
    lastmessage = ""

    while True:
        messages = bot.get_messages(limit=1)
        context_messages = bot.get_messages(limit=3)
        context = ""
        if context_messages:
            for user, content in reversed(context_messages):
                if user == exceptuser:
                    context += f"Tu escribiste: {content}\n"
                else:
                    context += f"(Otro usuario){user}: {content}\n"
        if messages:
            for user, content in messages:
                if user == exceptuser:
                    continue
                content = content.replace('\n', ' ')

                if content != lastmessage:
                    print(f"Nuevo mensaje de {user}: {content}")
                    time.sleep(random.uniform(0.5, 1.5))
                    bot.typing()
                    ai_response = ai.get_ai_response(api, content, context)
                    ai_response = ai_response.replace('\n', ' ')

                    char_delay = 0.045
                    typing_time = len(ai_response) * char_delay
                    time.sleep(typing_time)

                    bot.send_message(ai_response)
                    lastmessage = content
                    print(context)
        time.sleep(0.4)
def main():
    debug.clear()
    debug.title()
    print("\n\n\t\t\t\t\x1b[38;5;23m1. \x1b[38;5;130mEmpezar bot")
    print("\t\t\t\t\x1b[38;5;23m2. \x1b[38;5;130mConfigurar bot")
    
    print("\t\t\t\t\x1b[38;5;23m3. \x1b[38;5;130mSalir\n")
    select = debug.prompt(">> \x1b[38;5;23m")
    if select == "1":
        start_bot()
if __name__ == "__main__":
    main()