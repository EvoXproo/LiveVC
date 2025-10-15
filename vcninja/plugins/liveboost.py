from vcninja.core.module_injector import *
from vcninja.core import state

@vcninja.on(events.NewMessage(outgoing=True, pattern=r"\.lboost(?:\s+(.*))?$"))
async def LiveBoost(event):
    msg = event.pattern_match.group(1)
    if not msg:
        return await event.edit("On or Off?")
    if msg.lower() == "off":
        state.liveboost = False
        await event.edit("Live boost successfully disable")
    elif msg.lower() == "on":
        state.liveboost = True
        await event.edit("Live boost successfully enabled")
    else:
        await event.edit("On or Off?")