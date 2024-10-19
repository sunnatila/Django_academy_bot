from aiogram.utils.keyboard import ReplyKeyboardBuilder, KeyboardButton


admin_menu = ReplyKeyboardBuilder(
    markup=[
        [
            KeyboardButton(text="➕👨‍🎓 Oquvchi qoshish"),
            KeyboardButton(text="👥 Guruh yaratish"),
            KeyboardButton(text="📖 Mavzu yaratish"),
            KeyboardButton(text="📝 Test qoshish"),
            KeyboardButton(text="🎥 Darsga vidio qoshish"),
            KeyboardButton(text="📤 Vidio jonatish"),
            KeyboardButton(text="📊 Natijalarni ko'rish"),
        ]
    ]
).adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=True)

