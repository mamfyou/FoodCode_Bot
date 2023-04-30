from telethon import TelegramClient, events
from decouple import config

# Fill in your own values here
api_id = config('API_ID')
api_hash = config('API_HASH')
phone_number = config('PHONE_NUMBER')  # your phone number
session_name = 'food_is_the_best'

client = TelegramClient(session_name, api_id, api_hash).start(phone_number)


@client.on(events.NewMessage(chats=config('FOOD_GROUP_ID'), pattern='کد دارم'))
async def handle_message(event):
    await client.send_message(event.chat_id, 'استفاده میکنم')
    client.remove_event_handler(handle_message)


@client.on(events.NewMessage(chats=config('TEST_GROUP_ID'), pattern='کد دارم'))
async def handle_message(event):
    await client.send_message(event.chat_id, 'استفاده میکنم')


client.run_until_disconnected()
