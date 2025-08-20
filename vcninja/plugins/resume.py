from vcninja.core.module_injector import *

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.resume"))
async def resume(event):
    global queue
    chat_id = await get_chat_id()
    if not chat_id:
        return await event.edit("Please give me chat id in saved message.")
    if not queue:
        return await event.edit("Userbot not playing..")
    try:
        await Call.resume(chat_id)
        await event.edit("Resumed Successfully.")
    except Exeception as e:
        print(f"Error: {str(e)}")
        await event.edit("Already Resumed.")