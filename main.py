from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import logging

# Logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(message)s')
logger = logging.getLogger(__name__)

# TODO: refactor, create class Bot, use it for different games
# TODO: move token to config
# t.me/made_games_bot.
# token : 1794408127:AAFn19tXFkCuhn7eaPaa2xqAm7woqai7GF0

LAST_CHAR = 'Р'
WRONG_MESSAGE = 'Тебе на Р'
# TODO: complete answers
ANSWERS = {'а': 'Ахуеть ты пидар', 'б': 'бля, ну ты и пидар',
           'в': 'вот жеж ты пидар', 'г': 'Галя, глянь какой пидар',
           'д': 'друг, извини, но ты пидар', 'е': 'ебать пидар',
           'ё': 'ёмае ну и пидар', 'ж': 'жаль, но ты пидар',
           'з': 'заяйка, прости, но ты пидар', 'и': 'и опять же, ты пидар',
           'к': 'какой же пидар', 'л': 'лох, пидар',
           'м': 'мне желаь, но ты пидар', 'н': 'ну и пидар',
           'о': 'охуеть, мисье, но вы пидар', 'п': 'ПИДАР',
           'р': 'румяный пидар', 'с': 'сука, да ты же пидар',
           'т': 'тьфу ты пидар', 'у': 'ух сука, да ты же пидар',
           'ф': 'фу ты пидар', 'х': 'хуясе ты пидар',
           'ц': 'ц.. не придумал, но ты пидар', 'ш': 'шо сука, ты пидар',
           'щ': 'що сука, ти пiдор', 'э': 'эээ да ты же пидар',
           'ю': 'Юра не пидар, а ты пидар', 'я': 'я хуею с того, какой ты пидар',
           'ь': 'не выебывайся', 'ъ': 'не выебывайся',
           'ы': 'не выебывайся'}


def start(update: Update, _: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        f'Здарова {user.mention_markdown_v2()}\. Играем в слова\(или предложения\)\. Начинай\.',
        reply_markup=ForceReply(selective=True),
    )


def words(update: Update, _: CallbackContext) -> None:
    first_char = update.message.text[0]
    if first_char.lower() != LAST_CHAR.lower():
        update.message.reply_text(WRONG_MESSAGE)
    else:
        last_char = update.message.text[-1]
        update.message.reply_text(ANSWERS[last_char.lower()])


def main() -> None:
    updater = Updater("1794408127:AAFn19tXFkCuhn7eaPaa2xqAm7woqai7GF0")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, words))

    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
