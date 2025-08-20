from vcninja.core.module_injector import *

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.qremove(?:\s+(.*))?$"))
async def remove_to_queue(event):
    global queue
    file_name = event.pattern_match.group(1)
    if not file_name:
        return await event.edit("Please give me file name.")
    path = f"files/{file_name}"
    if path in queue:
        queue.remove(path)
        return await event.edit(f"**{file_name}** successfully removed to queue.")
    else:
        return await event.edit(f"**{file_name}** was not found in queue.")