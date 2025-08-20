from vcninja.core.module_injector import *
from vcninja.core import state

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.glitch(?:\s+(.*))?$"))
async def play(event):
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
        await Call.play(chat_id, "files/blank.mp3")
        await Call2.play(chat_id, "files/blank.mp3")
        await Call2.mute(chat_id)
        await Call.play(chat_id, file)
        if file not in state.queue:
            state.queue.append(file)
        await event.edit("glitch successfully..")
        state.is_playing = True
    except Exception as e:
        print(f"Error: {str(e)}")