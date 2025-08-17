from telethon import events
from telethon import TelegramClient
from telethon.sessions import StringSession
from pytgcalls import PyTgCalls
from dotenv import load_dotenv
import os

load_dotenv()

api_id = int(os.environ["api_id"])
api_hash = os.environ["api_hash"]
string_session = os.environ["session"]

client = TelegramClient(StringSession(string_session), api_id, api_hash)
Call = PyTgCalls(client)
Call2 = PyTgCalls(client)
client.start()
Call.start()
glitch = False


@client.on(events.NewMessage(outgoing=True, pattern=r"^\.play(?:\s+(.*))?$"))
async def play(event):
    file_name = event.pattern_match.group(1)
    if not file_name:
        return await event.edit("Please give me file name.")
    if not os.path.exists(f"files/{file_name}"):
        return await event.edit(f"{file_name} was not found.")
    chat_id = await get_chat_id()
    if not chat_id:
        return await event.edit("Please give me chat id in saved message.")
    try:
        await Call.play(chat_id, file_name)
    except Exception as e:
        print(f"Error: {str(e)}")

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.glitch(?:\s+(.*))?$"))
async def glitch(event):
    status = event.pattern_match.group(1)
    if not status:
        return await event.edit("on or off?")
    if status == "on":
        glitch = True
        await Call2.start()
        return await event.edit("glitch turned on.")
    if status == "off":
        glitch = False
        return await event.edit("glitch turned off")
    else:
        return await event.edit("on or off?")

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.boost(?:\s+(.*))?$"))
async def boost(event):
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
            await event.edit("Downloading...")
            download_file = await reply_message.download_media(file=f"{file_name}")
            await event.edit("Boosting..")
            output_file = f"files/{file_name}.wav"
            os.system(f"ffmpeg -i {download_file} -af \"volume=20.0,highpass=f=200,treble=g=5\" -ar 44100 -ac 2 \"{output_file}\" -y")
            os.remove(download_file)
            await event.edit("boosted successfully.")
            await client.send_file(event.chat_id, file=output_file)
        else:
            return await event.reply("This is not audio file. Please Reply audio file.")
    else:
        await event.edit("Please reply audio file.")
        return
    
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
            download_file = await reply_message.download_media(file=f"files/{file_name}")
        else:
            return await event.reply("This is not audio file. Please Reply audio file.")
    else:
        await event.edit("Please reply audio file.")
        return

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
        
@client.on(events.NewMessage(outgoing=True, pattern=r"^\.show"))
async def show(event):
    folder = "files"
    if not os.path.exists(folder):
        return await event.edit("Please create folder first.")
    files = os.listdir(folder)
    if not files:
        return await event.edit("Folder are empty.")
    result = "\n".join([f"{i}: {file}" for i, file in enumerate(files, start=1)])
    await event.edit(result)
    
async def get_chat_id():
    async for msg in client.iter_messages("me", limit=1):
        if msg and msg.text:
            try:
                chat_id = int(msg.text.strip())
                return chat_id
            except ValueError:
                return None
    return None
    
client.run_until_disconnected()