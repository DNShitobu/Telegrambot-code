from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext 

TOKEN:  Final = "Enter your token here"
BOT_USERNAME: Final = '@ni_a_paabu_na_bot'

# commands

async def start_command (update: Update, context: CallbackContext, DEFAULT_Types):
    await update.message.reply_text('M puhiya ka paɣi ni a ni yɛn dima alizama ŋɔ. Kawula n nyɛli?')

async def help_command (update: Update, context: CallbackContext, DEFAULT_Types):
    await update.message.reply_text('A yi mali la yɛlimuɣisirili shɛli, nyin bohimi ma ka n gba dihi doli nya n nyaa ni nyɛ sɔŋsim n taa intanɛɛti zuɣu bee')

async def custom_command (update: Update, context: CallbackContext, DEFAULT_Types):
    await update.message.reply_text('wuhimi ma a ni bɔri yɛltɔɣa shɛli')
			

# Responses
    def handle_response(text: str) -> str:
        processed: str = text.lower()

    if 'hello' in processed:
        return 'Haloo! ka di bewula?'
    
    if 'sɔŋsim' in processed:
        return 'Dimisuɣulo, vihimi Dagbanli Wikipedia zuɣu, dag.wikipedia.org'
    
    return 'M baye! Dimisuɣulo n be baŋ a ni bɔri shɛli ŋɔ maa. A ni tooi bohi so sɔɣiyeli dundɔŋ bili ŋɔ ni?'
    
    async def handle_message (update: Update, context: CallbackContext.DEFAULT_Types):
        message_type: str = update.message.chat.type
        text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print ('Bot:', response)
    await update.message.reply_text(response)

    async def error(update: Update, context: CallbackContext.DEFAULT_Types):
        print(f'Update {update} caused error {context.error}')

    
    if __name__ == '__main__':
        print('starting bot...')
        app = Application.builder().token(TOKEN).build()

    # commands
        app.add_handler(CommandHandler('start', start_command))
        app.add_handler(CommandHandler('help', help_command))
        app.add_handler(CommandHandler('custom', custom_command))

    # Messages
        
        app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
        app.add_error_handler(error)

    # polls the bot
        print('polling...')
        app.run_polling(poll_interval=3)
