import requests
from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import courses

cmd_router = Router()


@cmd_router.message(CommandStart())
async def cmd_start(message: Message):
    s = ("Assalomu alaykum!\nValyuta kurslari haqida ma`lumot beruvchi botimizga xush kelibsiz!\nYordam uchun /help "
          "buyrug`ini bosing!")
    await message.answer(text=s)


@cmd_router.message(Command('help'))
async def cmd_help(message: Message):
    s = "Quyidagi komandalar yordamida botdan samarali foydalanishingiz mumkin:\n\n"
    s += "\t/start - botni qayta ishga tushirish\n"
    s += "\t/help -  botdan foydalanish yo'riqnomasi\n"
    s += "\t/kurslar - valyuta kurslari\n" 
    s += "\t/dollar - dollar kursi\n"
    s += "\t/yevro - yevro kursi\n"
    s += "\t/rubl - rubl kursi\n\n"
    s += "Agar biror summani  yuborsangiz, bot uni turli valyutalardagi qiymatini qaytaradi.(Masalan: 100000)"
    await message.answer(text=s)

@cmd_router.message(Command('kurslar'))
async def cmd_kurslar(message: Message):
    response = requests.get("https://cbu.uz/ru/arkhiv-kursov-valyut/json/")
    s ="Bugungi valyuta kurslari:\n"
    for kurs in response.json():
        if kurs['Ccy'] in ['USD', 'EUR', 'RUB']:
            courses[kurs['Ccy']] = float(kurs['Rate'])
            s += f"1 {kurs['CcyNm_UZ']} - {kurs['Rate']} so`m\n"
    await message.answer(text=s)


@cmd_router.message(Command('dollar'))
async def cmd_usd(message: Message):
    s = f"1 AQSH dollari = {courses['USD']} so`m"
    await message.reply(s)


@cmd_router.message(Command('yevro'))
async def cmd_usd(message: Message):
    s = f"1 EURO = {courses['EUR']} so`m"
    await message.reply(s)


@cmd_router.message(Command('rubl'))
async def cmd_usd(message: Message):
    s = f"1 Rossiya rubli = {courses['RUB']} so`m"
    await message.reply(s)
