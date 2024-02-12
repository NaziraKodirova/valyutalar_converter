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
    s = "Bugungi valyuta kurslari:\n"
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
async def cmd_eur(message: Message):
    s = f"1 EURO = {courses['EUR']} so`m"
    await message.reply(s)

@cmd_router.message(Command('rubl'))
async def cmd_rub(message: Message):
    s = f"1 Rossiya rubli = {courses['RUB']} so`m"
    await message.reply(s)


@cmd_router.message(Command('dollar'))
async def cmd_usd(message: Message):
    s = f"1 AQSH dollari = {courses['USD']} so`m"
    await message.reply(s)

@cmd_router.message(Command('yevro'))
async def cmd_eur(message: Message):
    s = f"1 EURO = {courses['EUR']} so`m"
    await message.reply(s)

@cmd_router.message(Command('rubl'))
async def cmd_rub(message: Message):
    s = f"1 Rossiya rubli = {courses['RUB']} so`m"
    await message.reply(s)

@cmd_router.message()
async def handle_currency(message: Message):
    try:
        text = message.text
        amount_str = text[:-1]  # Remove the currency symbol at the end
        symbol = text[-1]  # Get the last character as the currency symbol

        if not amount_str.replace('.', '').isdigit():
            raise ValueError("Invalid number")  # Raise an error if the remaining string is not a valid number

        amount = float(amount_str)

        if symbol == '$':
            rate = courses.get('USD', 0.0)
            currency_name = 'dollar'

        elif symbol == '€':
            rate = courses.get('EUR', 0.0)
            currency_name = 'yevro'

        elif symbol == '₽':
            rate = courses.get('RUB', 0.0)
            currency_name = 'rubl'

        else:
            await message.reply("Noto'g'ri valyuta belgisi! Qo'shimcha belgini o'rnating.")
            return

        if rate:
            converted_amount = amount * rate
            reply_message = f"{amount} {currency_name} = {converted_amount} so'm"
            await message.reply(reply_message)
        else:
            await message.reply(f"{currency_name.capitalize()} kursi topilmadi.")
    except ValueError as e:
        await message.reply(f"Xatolik! {e}. Iltimos, raqamli miqdorni kiriting.")

@cmd_router.message(Command('dollar'))
async def cmd_usd(message: Message):
    s = f"1 AQSH dollari = {courses['USD']} so`m"
    await message.reply(s)

@cmd_router.message(Command('yevro'))
async def cmd_eur(message: Message):
    s = f"1 EURO = {courses['EUR']} so`m"
    await message.reply(s)

@cmd_router.message(Command('rubl'))
async def cmd_rub(message: Message):
    s = f"1 Rossiya rubli = {courses['RUB']} so`m"
    await message.reply(s)


@cmd_router.message(Command('dollar'))
async def cmd_usd(message: Message):
    s = f"1 AQSH dollari = {courses['USD']} so`m"
    await message.reply(s)

@cmd_router.message(Command('yevro'))
async def cmd_eur(message: Message):
    s = f"1 EURO = {courses['EUR']} so`m"
    await message.reply(s)

@cmd_router.message(Command('rubl'))
async def cmd_rub(message: Message):
    s = f"1 Rossiya rubli = {courses['RUB']} so`m"
    await message.reply(s)