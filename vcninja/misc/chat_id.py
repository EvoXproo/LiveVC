async def get_chat_id():
    async for msg in client.iter_messages("me", limit=1):
        if msg and msg.text:
            try:
                chat_id = int(msg.text.strip())
                return chat_id
            except ValueError:
                return None
    return None
    
    