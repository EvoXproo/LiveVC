from vcninja.core.module_injector import *

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.qshow"))
async def qshow(event):
    global queue
    if not queue:
        return await event.edit("Queue is empty")
    else:
        return await event.edit(f"{queue}")