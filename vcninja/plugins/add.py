from vcninja.core.module_injector import *

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.add(?:\s+(.*))?$"))
async def add_to_queue(event):
    global queue
    file_name = event.pattern_match.group(1)
    if not file_name:
        return await event.edit("Please give me file name.")
    path = f"files/{file_name}"
    if not os.path.exists(path):
        return await event.edit(f"**{file_name}** Was not found.")
    if not path in queue:
        queue.append(path)
        return await event.edit(f"**{file_name}** successfully added to queue.")
    else:
        return await event.edit(f"**{file_name}** was already in queue.")