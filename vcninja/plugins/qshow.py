from vcninja.core.module_injector import *
from vcninja.core import state

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.qshow"))
async def qshow(event):
    if not state.queue:
        return await event.edit("Queue is empty")
    else:
        return await event.edit(f"{queue}")