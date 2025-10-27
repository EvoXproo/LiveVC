from vcninja.core.module_injector import *
from pytgcalls.types import Device, Direction, ExternalMedia, MediaStream, RecordStream, StreamFrames
from pytgcalls.types.raw import AudioParameters
from pytgcalls import filters, PyTgCalls
from vcninja.core import state
import numpy as np

chat_ids = []

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"\.live"))
async def Live(event):
    global chat_ids, my_chat_id, chat_id
    chat_id, my_chat_id = await get_chat_id()
    chat_id = int(chat_id)
    my_chat_id = int(my_chat_id)
    AUDIO_PARAMETERS = AudioParameters(bitrate=48000, channels=2)

    if not chat_id:
        return await event.edit("Please give me target chat_id in channel")
    elif not my_chat_id:
        return await event.edit("Please give me My Chat Id in channel")

    await event.edit("processing...")

    await Call.play(
        my_chat_id,
        MediaStream(ExternalMedia.AUDIO, AUDIO_PARAMETERS),
    )
    await Call.record(
        my_chat_id,
        RecordStream(True, AUDIO_PARAMETERS),
    )

    await Call.play(
        chat_id,
        MediaStream(ExternalMedia.AUDIO, AUDIO_PARAMETERS),
    )
    await Call.record(
        chat_id,
        RecordStream(True, AUDIO_PARAMETERS),
    )

    chat_ids = [my_chat_id, chat_id]
    state.is_playing = True
    await event.edit("🎙️ Live started.")


@Call.on_update(filters.stream_frame(Direction.INCOMING, Device.MICROPHONE))
async def audio_data(_: PyTgCalls, update: StreamFrames):
    global my_chat_id, chat_id

    mixed_output = np.zeros(len(update.frames[0].frame) // 2, dtype=np.int16)

    for frame_data in update.frames:
        samples = np.frombuffer(frame_data.frame, dtype=np.int16)
        mixed_output[:len(samples)] += samples

    if state.liveboost and update.chat_id == my_chat_id:
        gain = 200.0
        mixed_output = mixed_output.astype(np.float32) * gain
        mixed_output = np.clip(mixed_output, -32768, 32767)
        mixed_output = mixed_output.astype(np.int16)

    if update.chat_id == my_chat_id:
        await Call.send_frame(
            chat_id,
            Device.MICROPHONE,
            mixed_output.tobytes(),
        )

    elif update.chat_id == chat_id:
        pass