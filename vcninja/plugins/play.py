from vcninja.core.module_injector import *

is_playing = False
queue = []
current_index = 0

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.play(?:\s+(.*))?$"))
async def play(event):
    global is_playing
    global queue
    file_name = event.pattern_match.group(1)
    if not file_name:
        return await event.edit("Please give me file name.")
    file = f"files/{file_name}"
    if not os.path.exists(file):
        return await event.edit(f"{file_name} was not found.")
    chat_id = await get_chat_id()
    if not chat_id:
        return await event.edit("Please give me chat id in saved message.")
    try:
        await Call.play(chat_id, file)
        if file not in queue:
            queue.append(file)
        await event.edit("successfully playing..")
        is_playing = True
    except Exception as e:
        print(f"Error: {str(e)}")