from vcninja.core.module_injector import *

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"^\.show"))
async def show(event):
    folder = "files"
    if not os.path.exists(folder):
        return await event.edit("Please create folder first.")
    files = os.listdir(folder)
    if not files:
        return await event.edit("Folder are empty.")
    result = "\n".join([f"{i}: {file}" for i, file in enumerate(files, start=1)])
    await event.edit(result)