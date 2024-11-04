from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters

firstNum, operation, secondNum = range(3)

async def start(update: Update, context):
    await update.message.reply_text('first num:')
    return firstNum

async def first_number(update: Update, context):
    try:
        context.user_data['first_number'] = float(update.message.text)
        keyboard = [
            [
                InlineKeyboardButton("сложение", callback_data='add'),
                InlineKeyboardButton("вычитание", callback_data='subtract'),
                InlineKeyboardButton("умножение", callback_data='multiply'),
                InlineKeyboardButton("деление", callback_data='divide'),
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('операция:', reply_markup=reply_markup)
        return operation
    except ValueError:
        await update.message.reply_text('число введи, балда')
        return firstNum

async def operation(update: Update, context):
    query = update.callback_query
    await query.answer()
    context.user_data['operation'] = query.data
    await query.edit_message_text(text='second num:')
    return secondNum

async def second_number(update: Update, context):
    try:
        second_number = float(update.message.text)
        first_number = context.user_data['first_number']
        operation = context.user_data['operation']

        if operation == 'add':
            result = first_number + second_number
            op_symbol = '+'
        elif operation == 'subtract':
            result = first_number - second_number
            op_symbol = '-'
        elif operation == 'multiply':
            result = first_number * second_number
            op_symbol = '*'
        elif operation == 'divide':
            result = first_number / second_number
            op_symbol = '/'

        await update.message.reply_text(f'{first_number} {op_symbol} {second_number} = {result}')
        return ConversationHandler.END
    except ValueError:
        await update.message.reply_text('enter correct num.')
        return secondNum

async def cancel(update: Update, context):
    await update.message.reply_text('Operation canceled.')
    return ConversationHandler.END

def main():
    application = ApplicationBuilder().token('токенчик').build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            firstNum: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_number)],
            operation: [CallbackQueryHandler(operation)],
            secondNum: [MessageHandler(filters.TEXT & ~filters.COMMAND, second_number)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(conv_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
