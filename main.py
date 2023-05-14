from decouple import config
from telethon import TelegramClient, events

# Fill in your own values here
api_id = config('API_ID')
api_hash = config('API_HASH')
phone_number = config('PHONE_NUMBER')
session_name = 'messages'

client = TelegramClient(session_name, api_id, api_hash).start(phone_number)


@client.on(events.NewMessage(chats=int(config('FOOD_GROUP_ID')), pattern='کد دارم'))
async def send_I_use(event):
    global food_is_running
    if food_is_running:
        await client.send_message(event.chat_id, 'استفاده میکنم')

        sender = await event.get_sender()
        user_id = sender.id

        await client.send_message(user_id, 'سلام وقتتون بخیر')
        await client.send_message(user_id, 'کد رو بفرستین لطفا🙏')
        await client.send_message(int(config('MY_ID')), 'سلام بلیط گرفتم برات')
        food_is_running = False


@client.on(events.NewMessage(chats=int(config('TEST_FOOD_GROUP_ID')), pattern='کد دارم'))
async def test_send_I_use(event):
    global food_is_running
    if food_is_running:
        await client.send_message(event.chat_id, 'استفاده میکنم')

        sender = await event.get_sender()
        user_id = sender.id

        await client.send_message(user_id, 'سلام وقتتون بخیر')
        await client.send_message(user_id, 'کد رو بفرستین لطفا🙏')
        await client.send_message(int(config('MY_ID')), 'سلام کد گرفتم برات')
        food_is_running = False


@client.on(events.NewMessage(pattern='/start_food'))
async def start_food(event):
    global food_is_running
    if not food_is_running:
        food_is_running = True


@client.on(events.NewMessage(chats=int(config('TICKET_GROUP_ONE'))))
async def handle_message_taghat(event):
    global ticket_is_running
    if ticket_is_running:
        if '#فروشی' in event.raw_text and \
                (
                        'قم تهران' in event.raw_text or 'قم به تهران' in event.raw_text or 'قم‌تهران' in event.raw_text) and \
                ('سه شنبه' in event.raw_text or 'سه‌شنبه' in event.raw_text) and \
                ('9' in event.raw_text or '۹' in event.raw_text):
            sender = await event.get_sender()
            user_id = sender.id
            await client.send_message(user_id, 'سلام وقتتون بخیر من بلیط رو میخواستم')
            await client.send_message(int(config('MY_ID')), 'سلام بلیط گرفتم برات')
            ticket_is_running = False


@client.on(events.NewMessage(chats=int(config('TICKET_GROUP_TWO'))))
async def handle_message_kheft(event):
    global ticket_is_running
    if ticket_is_running:
        if '#فروشی' in event.raw_text and \
                (
                        'قم تهران' in event.raw_text or 'قم به تهران' in event.raw_text or 'قم‌تهران' in event.raw_text) and \
                ('سه شنبه' in event.raw_text or 'سه‌شنبه' in event.raw_text) and \
                ('9' in event.raw_text or '۹' in event.raw_text):
            sender = await event.get_sender()
            user_id = sender.id
            await client.send_message(user_id, 'سلام وقتتون بخیر من بلیط رو میخواستم')
            await client.send_message(int(config('MY_ID')), 'سلام بلیط گرفتم برات')
            ticket_is_running = False


@client.on(events.NewMessage(chats=int(config('TEST_FOOD_GROUP_ID'))))
async def handle_message_test(event):
    if '#فروشی' in event.raw_text and \
            (
                    'قم تهران' in event.raw_text or 'قم به تهران' in event.raw_text or 'قم‌تهران' in event.raw_text) and \
            ('سه شنبه' in event.raw_text or 'سه‌شنبه' in event.raw_text) and \
            ('9' in event.raw_text or '۹' in event.raw_text):
        sender = await event.get_sender()
        user_id = sender.id
        await client.send_message(user_id, 'سلام وقتتون بخیر من بلیط رو میخواستم')
        await client.send_message(int(config('MY_ID')), 'سلام بلیط گرفتم برات')


@client.on(events.NewMessage(pattern='/start_ticket'))
async def start_ticket(event):
    global ticket_is_running
    if not ticket_is_running:
        ticket_is_running = True


@client.on(events.NewMessage(pattern='/stop_ticket'))
async def stop_ticket(event):
    global ticket_is_running
    if ticket_is_running:
        ticket_is_running = False
        await event.respond('بلیط قطار متوقف شد')
    else:
        await event.respond('بلیط قطار خاموشه')


@client.on(events.NewMessage(pattern='/stop_food'))
async def stop_food(event):
    global food_is_running
    if food_is_running:
        food_is_running = False
        await event.respond('کد غذا متوقف شد')
    else:
        await event.respond('کد غذا خاموشه')


client.run_until_disconnected()
