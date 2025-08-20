from vcninja.core.module_injector import *

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.download(?:\s+(.*))?$"))
async def download(event):
    if event.is_reply:
        file_name = event.pattern_match.group(1)
        if not file_name:
            await event.edit("please give me file name.")
            return
        reply_message = await event.get_reply_message()
        if not reply_message.media:
            return await event.edit("This is not audio file. Please Reply audio file.")
        mime_type = reply_message.file.mime_type if reply_message.file else None
        if not mime_type:
            return await event.edit("i Guess this file was cruppted.")
        if mime_type.startswith("audio/"):
            await event.edit("downloading..")
            download_file = await reply_message.download_media(file=f"files/{file_name}")
            await event.edit("Download Successfully.")
        else:
            return await event.reply("This is not audio file. Please Reply audio file.")
    else:
        await event.edit("Please reply audio file.")
        return
