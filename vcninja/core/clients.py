from telethon import TelegramClient
from telethon.sessions import StringSession
from dotenv import load_dotenv
from pytgcalls import PyTgCalls
import os

load_dotenv()

class VCNINJA:
    def __init__(self):
        self.api_id = int(os.environ["api_id"])
        self.api_hash = os.environ["api_hash"]
        self.string_session = os.environ["session"]
        self.vcninja = TelegramClient(StringSession(self.string_session), self.api_id, self.api_hash)
        self.Call = PyTgCalls(self.vcninja)
        self.Call2 = PyTgCalls(self.vcninja)
vc = VCNINJA()
vcninja = vc.vcninja
Call = vc.Call