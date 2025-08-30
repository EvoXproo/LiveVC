from vcninja.core.module_injector import *
from vcninja.core import state

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.end"))
async def end(event):
    if state.is_playing:
        chat_id = await get_chat_id()
        if not chat_id:
            return await event.edit("Please give me chat id in saved message.")
        try:
            await Call.leave_call(chat_id)
            state.queue.clear()
            state.is_playing = False
            return await event.edit("successfully stopped.")
        except Exception as e:
            return await event.edit(f"Error: {str(e)}")
    else:
        await event.edit("Vcninja is not streaming.")