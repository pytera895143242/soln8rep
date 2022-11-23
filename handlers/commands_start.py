import asyncio
from misc import dp,bot
from .sqlit import reg_user
from aiogram import types
channel1 = -1001863985247
content_id = -1001165606914
print(1)

markup = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='🔑 UNLOCK', url = 'https://t.me/share/url?url=https%3A%2F%2Ft.me%2F%2Bhs-KRYbsMV4zNDky')
bat_b = types.InlineKeyboardButton(text='🔑 SECOND STAGE UNLOCK', url = 'https://t.me/share/url?url=https%3A%2F%2Ft.me%2F%2Bhs-KRYbsMV4zNDky')
bat_c = types.InlineKeyboardButton(text='🔑 STEGE THREE UNLOCK', url = 'https://t.me/share/url?url=https%3A%2F%2Ft.me%2F%2Bhs-KRYbsMV4zNDky')
markup.add(bat_a)



async def posting():
    while True:
        q = await bot.copy_message(chat_id=channel1,from_chat_id=content_id,message_id=10,reply_markup=markup)
        await asyncio.sleep(45)
        await bot.delete_message(chat_id=channel1,message_id=q.message_id)


@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    reg_user(update.from_user.id,1)
    await bot.copy_message(chat_id=update.from_user.id, from_chat_id=content_id, message_id=9, reply_markup=markup)
    try:
        await update.approve()
    except:
        pass


@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    reg_user(message.chat.id,ref=1)
    print(2)
    await bot.copy_message(chat_id=message.chat.id, from_chat_id=content_id, message_id=9, reply_markup=markup)