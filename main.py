from telethon import events
from telethon import TelegramClient
from telethon.sessions import StringSession
#from pytgcalls import PyTgCalls
from dotenv import load_dotenv
from os import environ

load_dotenv()

api_id = int(environ["api_id"])
api_hash = environ["api_hash"]
string_session = environ["session"]

client = TelegramClient(StringSession(string_session), api_id, api_hash)
#Call = PyTgCalls(client)
#Call2 = PyTgCalls(client_2)
client.start()

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.boost\s+(.*)"))
async def boost(event):
    if event.is_reply:
        file_name = event.pattern_match.group(1)
        if not file_name:
            await event.edit("please give me file name.")
            return
    else:
        await event.edit("Please reply audio file.")
        return
        
        
client.run_until_disconnected()