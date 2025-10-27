from vcninja.core.module_injector import *
from vcninja.core import state
from pytgcalls import filters
from pytgcalls.types import Update
from pytgcalls.types import GroupCallParticipant

@Call.on_update(filters.stream_end())
async def stream_end(_, update: Update):
    chat_id = update.chat_id
    state.current_index += 1
    if state.current_index >= len(state.queue):
        state.current_index = 0
    await Call.play(chat_id, state.queue[state.current_index])
    
"""
@Call.on_update(filters.call_participant())
async def chat_update(_, update: Update):
    chat_id, my_chat_id = await get_chat_id()
    if not chat_id:
        return
    if chat_id != update.chat_id:
        return
    user_id = update.participant.user_id
    action = update.participant.action
    if user_id == 7872695556:
        if action == GroupCallParticipant.Action.JOINED:
            await Call.leave_call(chat_id)
            state.queue.clear()
            state.is_playing = False
            
"""            
@Call.on_update(filters.call_participant())
async def mute_update(_, update: Update):
    me = await vcninja.get_me()
    user_id = int(update.participant.user_id)
    chat_id, my_chat_id = await get_chat_id()
    chat_id = int(chat_id)
    if not chat_id:
        return
    if chat_id != int(update.chat_id) :
        return
    action = update.participant.muted
    if user_id == me.id:
        if action:
            await Call.mute(chat_id)