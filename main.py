import logging
import traceback

from telegram.ext import ApplicationBuilder, CommandHandler
from command_handlers import handlers, error_handler

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def main():
    with open("token.txt", "r") as token_file:
        token = token_file.read()
    app = ApplicationBuilder().token(token).build()

    # Adding command handlers
    app.add_handlers(
        handlers=[CommandHandler(endpoint, command_handler) for endpoint, command_handler in handlers.items()])
    app.add_error_handler(error_handler)

    app.run_polling()


if __name__ == "__main__":
    try:
        main()
    except:
        print(traceback.format_exc())
