from vcninja.core.module_injector import *

my_chat_id_link = "https://t.me/vcninja_logger/3"
chat_id_link = "https://t.me/vcninja_logger/5"

async def get_chat_id():
    username = "vcninja_logger"
    try:
        channel = await vcninja.get_entity(username)
    except: 
        return await vcninja.send_message("me", f"I am not in @{username}")
    try:    
        msg = await vcninja.get_messages(channel, ids=5)
        chat_id = msg.text
        msg = await vcninja.get_messages(channel, ids=3)
        my_chat_id = msg.text
        return [chat_id, my_chat_id]
    except Exception as e:
        print(e)
        return [None, None]