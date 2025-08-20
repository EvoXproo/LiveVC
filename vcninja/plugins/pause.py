from vcninja.core.module_injector import *
from vcninja.core import state

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.pause"))
async def pause(event):
    chat_id = await get_chat_id()
    if not chat_id:
        return await event.edit("Please give me chat id in saved message.")
    if not state.queue:
        return await event.edit("Userbot not playing..")
    try:
        await Call.pause(chat_id)
        await event.edit("Paused Successfully.")
    except Exeception as e:
        print(f"Error: {str(e)}")
        await event.edit("Already Paused.")