from vcninja.core.module_injector import *

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.remove(?:\s+(.*))?$"))
async def remove(event):
    file_name = event.pattern_match.group(1)
    if not file_name:
        return await event.edit("Please give me file name.")
    file = f"files/{file_name}"
    if os.path.exists(file):
        os.remove(file)
        await event.edit(f"**{file}** Successfully removed.")
    else:
        return await event.edit(f"**{file}** is Not exists.")
        