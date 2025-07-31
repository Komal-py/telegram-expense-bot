from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

class ExpenseBot:
    def __init__(self):
        self.budget = 0
        self.expenses = []

    def set_budget(self, amount):
        self.budget = amount

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))

    def remaining_balance(self):
        return self.budget - sum(a for _, a in self.expenses)

    def summary(self):
        text = "📊 Expense Summary:\n"
        for desc, amt in self.expenses:
            text += f"• {desc}: ₹{amt}\n"
        text += f"\n🧾 Total: ₹{sum(a for _, a in self.expenses)}\n"
        text += f"💰 Remaining: ₹{self.remaining_balance()}"
        return text

# Initialize bot logic
expense_bot = ExpenseBot()

# Telegram Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to Trip Expense Bot!\nUse /setbudget, /add, /summary")

async def setbudget(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(context.args[0])
        expense_bot.set_budget(amount)
        await update.message.reply_text(f"✅ Budget set to ₹{amount}")
    except:
        await update.message.reply_text("❗ Usage: /setbudget 5000")

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        description = context.args[0]
        amount = float(context.args[1])
        expense_bot.add_expense(description, amount)
        await update.message.reply_text(
            f"✅ Added '{description}' - ₹{amount}\n💰 Remaining: ₹{expense_bot.remaining_balance()}"
        )
    except:
        await update.message.reply_text("❗ Usage: /add Food 200")

async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(expense_bot.summary())

# Run the bot
if __name__ == "__main__":
    import os
    TOKEN = os.environ["BOT_TOKEN"]  # ✅ Use environment variable

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("setbudget", setbudget))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(CommandHandler("summary", summary))

    print("🚀 Bot is running...")
    app.run_polling()
