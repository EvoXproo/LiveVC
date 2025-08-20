from vcninja.core.module_injector import *
from pytgcalls import filters
from pytgcalls.types impirt Update

@Call.on_update(filters.stream_end())
async def stream_end(_, update: Update):
    global current_index
    global queue
    chat_id = update.chat_id
    current_index += 1
    if current_index >= len(queue):
        current_index = 0
    await Call.play(chat_id, queue[current_index])