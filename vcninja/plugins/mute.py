from vcninja.core.module_injector import *
from vcninja.core import state

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.mute"))
async def pause(event):
    chat_id, my_chat_id = await get_chat_id()
    if not chat_id:
        return await event.edit("Please give me chat id in saved message.")
    try:
        await Call.mute(chat_id)
        await event.edit("Mute Successfully.")
    except Exeception as e:
        print(f"Error: {str(e)}")
        await event.edit("Already Muted.")
        
        
@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.unmute"))
async def pause(event):
    chat_id, my_chat_id = await get_chat_id()
    if not chat_id:
        return await event.edit("Please give me chat id in saved message.")
    try:
        await Call.unmute(chat_id)
        await event.edit("UnMute Successfully.")
    except Exeception as e:
        print(f"Error: {str(e)}")
        await event.edit("Already Muted.")
        
        
        