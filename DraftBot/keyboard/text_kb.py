from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Ясно, понятно',
                               keyboard=[
                                   [
                                       KeyboardButton(text='Отправить свой контакт', request_contact=True),
                                       KeyboardButton(text='Отправить свое местоположение', request_location=True),
                                       KeyboardButton(text='Кнопка 3'),
                                       KeyboardButton(text='Кнопка 4'),

                                   ],
                                   [
                                       KeyboardButton(text='Отдельная кнопка')
                                   ]
                               ]

                               )
