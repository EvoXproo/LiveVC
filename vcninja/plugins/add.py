from vcninja.core.module_injector import *
from vcninja.core import state

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.add(?:\s+(.*))?$"))
async def add_to_queue(event):
    file_name = event.pattern_match.group(1)
    if not file_name:
        return await event.edit("Please give me file name.")
    path = f"files/{file_name}"
    if not os.path.exists(path):
        return await event.edit(f"**{file_name}** Was not found.")
    if not path in state.queue:
        state.queue.append(path)
        return await event.edit(f"**{file_name}** successfully added to queue.")
    else:
        return await event.edit(f"**{file_name}** was already in queue.")