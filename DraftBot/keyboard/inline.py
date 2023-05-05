from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

kb_confirm = InlineKeyboardMarkup(inline_keyboard=[
                             [
                                 InlineKeyboardButton(
                                     text='Подтвердить',
                                     callback_data='confirm'
                                 ),
                                 InlineKeyboardButton(
                                     text='Отмена',
                                     callback_data='cancel'
                                 )
                             ],
                             [
                                 InlineKeyboardButton(
                                     text='Го на сайт',
                                     url='https://www.youtube.com/'
                                 )
                             ]
                         ])
