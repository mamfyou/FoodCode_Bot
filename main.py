import time

from telethon import TelegramClient, events
from decouple import config

# Fill in your own values here
api_id = config('API_ID')
api_hash = config('API_HASH')
phone_number = config('PHONE_NUMBER')
session_name = 'messages'

client = TelegramClient(session_name, api_id, api_hash).start(phone_number)


@client.on(events.NewMessage(chats=int(config('FOOD_GROUP_ID')), pattern='کد دارم'))
async def send_I_use(event):
    await client.send_message(event.chat_id, 'استفاده میکنم')

    sender = await event.get_sender()
    user_id = sender.id

    await client.send_message(user_id, 'سلام وقتتون بخیر')
    await client.send_message(user_id, 'کد رو بفرستین لطفا🙏')

    client.remove_event_handler(send_I_use)


@client.on(events.NewMessage(chats=int(config('TEST_FOOD_GROUP_ID')), pattern='کد دارم'))
async def test_send_I_use(event):
    await client.send_message(event.chat_id, 'استفاده میکنم')

    sender = await event.get_sender()
    user_id = sender.id

    await client.send_message(user_id, 'سلام وقتتون بخیر')
    await client.send_message(user_id, 'کد رو بفرستین لطفا🙏')


@client.on(events.NewMessage(chats=int(config('TICKET_GROUP_ONE'))))
async def handle_message_taghat(event):
    if '#فروشی' in event.raw_text and \
            ('قم تهران' in event.raw_text or 'قم به تهران' in event.raw_text or 'قم‌تهران' in event.raw_text) and \
            ('سه شنبه' in event.raw_text or 'سه‌شنبه' in event.raw_text) and \
            ('9' in event.raw_text or '۹' in event.raw_text):
        sender = await event.get_sender()
        user_id = sender.id
        await client.send_message(user_id, 'سلام وقتتون بخیر من بلیط رو میخواستم')
    client.remove_event_handler(handle_message_taghat)
    client.remove_event_handler(handle_message_kheft)


@client.on(events.NewMessage(chats=int(config('TICKET_GROUP_TWO'))))
async def handle_message_kheft(event):
    if '#فروشی' in event.raw_text and \
            ('قم تهران' in event.raw_text or 'قم به تهران' in event.raw_text or 'قم‌تهران' in event.raw_text) and \
            ('سه شنبه' in event.raw_text or 'سه‌شنبه' in event.raw_text) and \
            ('9' in event.raw_text or '۹' in event.raw_text):
        sender = await event.get_sender()
        user_id = sender.id
        await client.send_message(user_id, 'سلام وقتتون بخیر من بلیط رو میخواستم')
    client.remove_event_handler(handle_message_taghat)
    client.remove_event_handler(handle_message_kheft)


@client.on(events.NewMessage(chats=int(config('TEST_FOOD_GROUP_ID'))))
async def handle_message_kheft(event):
    if '#فروشی' in event.raw_text and \
            ('قم تهران' in event.raw_text or 'قم به تهران' in event.raw_text or 'قم‌تهران' in event.raw_text) and \
            ('سه شنبه' in event.raw_text or 'سه‌شنبه' in event.raw_text) and \
            ('9' in event.raw_text or '۹' in event.raw_text):
        sender = await event.get_sender()
        user_id = sender.id
        await client.send_message(user_id, 'سلام وقتتون بخیر من بلیط رو میخواستم')


async def print_hello():
    while True:
        print('ببین ساعت چند شده!!! ', time.time())
        time.sleep(60)


client.run_until_disconnected()
