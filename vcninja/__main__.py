print("loading core system.")
from vcninja.core.module_injector import *
from vcninja.misc import loop
from asyncio import run

print("core system loaded.")

async def main():
    print("Starting pytgcalls clients.")
    await Call.start()
    await Call2.start()
    print("pytgcalls clients successfully started.")
    print("Starting telethon client.")
    await vcninja.start()
    print("telethon client successfully started.")
    print("loading plugins")
    import_plugins()
    print("plugins loaded successfully")
    print("VCNINJA STARTED.")
    
def import_plugins():
    path = "vcninja/plugins"
    for file in os.listdir(path):
        if file.endswith(".py") and not file.startswith("__"):
            importlib.import_module(f"zhunehra.plugins.{file[:-3]}")
            print(f"{file[:-3]} plugin loaded succesfully.")
    
run(main())