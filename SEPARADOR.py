import telegram
import os
import re
import asyncio
from telegram.constants import ParseMode
from telegram import (
    Update,

    Chat,
    Bot,
    ChatMemberUpdated,
    ChatMember,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    User,
    CallbackQuery,
    MessageEntity,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InputFile,
)
from telegram.ext import (
    Updater,
    CallbackContext,
    CallbackQueryHandler,
    ChosenInlineResultHandler,
    ChatMemberHandler,
    CommandHandler,
    ConversationHandler,
    InlineQueryHandler,
    MessageHandler,
    PollAnswerHandler,
    PollHandler,
    PreCheckoutQueryHandler,
    PrefixHandler,
    ShippingQueryHandler,
    StringCommandHandler,
    StringRegexHandler,
    TypeHandler,
    Application,
    ContextTypes,
    filters
)


os.system(f"title SEPARADOR CC BY MARTIN")
bot_token="COLOQUE SEU TOKEN AQUI"
bot_emergency = telegram.Bot(token=bot_token)

async def Mensagens_qualquer(update: Update, context: CallbackContext) -> None:

    if update.effective_message.text.find('/separador===') != -1 and update.effective_chat.type == Chat.PRIVATE:
        Div_Igual = update.effective_message.text.split("===")
        # expressão regular com grupos de captura para extrair as informações desejadas
        pattern = r"(\d{15})\|(\d{2})\|(\d{4}|\d{2})\|(\d{3})"

        # encontra todos os padrões no texto
        matches = re.findall(pattern, Div_Igual[1])

        # imprime os padrões encontrados
        patterns_list = []
        for match in matches:
            # junta as informações em um formato comum
            pattern_string = "{}|{}|{}|{}".format(match[0], match[1], match[2], match[3])
            patterns_list.append(pattern_string)
        await bot_emergency.send_message(update.effective_chat.id,"\n".join(patterns_list))   
        return    



def main() -> None:


    
    print(f"SEPARADOR INICIADO!")
    

    application = Application.builder().token(bot_token).build()

    application.add_handler(MessageHandler(filters.ALL, Mensagens_qualquer))

    application.run_polling()
    
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main())  
    loop.run_forever()
