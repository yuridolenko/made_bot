from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from decouple import config
from setup_logger import logger
from words_game import WordsGame


class Bot:
    words = WordsGame()

    def start(self):
        updater = Updater(config("TOKEN"))

        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", self.greetings))

        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.on_message))

        logger.info("Starting bot...")

        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()

    def on_message(self, update: Update, _: CallbackContext) -> None:
        logger.info(
            f'WORDS: Message received from {update.effective_user.mention_markdown_v2()}, :  {update.message.text}')
        answer = self.words.get_answer(update.message.text)
        update.message.reply_text(answer)

    def greetings(self, update: Update, _: CallbackContext) -> None:
        user = update.effective_user
        update.message.reply_markdown_v2(
            f'Здарова {user.mention_markdown_v2()}\. Играем в слова\(или предложения\)\. Начинай\.',
            reply_markup=ForceReply(selective=True),
        )
