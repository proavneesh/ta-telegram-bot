from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters
from telegram.constants import ChatAction

from fastapi import FastAPI
import uvicorn
import threading

# ✅ FastAPI server setup for Railway
app_fastapi = FastAPI()

@app_fastapi.get("/")
def home():
    return {"message": "TA Telegram Bot is running successfully!"}

def run_fastapi():
    uvicorn.run(app_fastapi, host="0.0.0.0", port=8000)

# ✅ Your new bot token
BOT_TOKEN = '7952761769:AAE6gGZidtJcspccoSSGcQcJr5HTy_-7ca4'

# ✅ FAQ Answers dictionary (30 questions)
faq_answers = {
    "free": "✅ Yes, ham ek business model provide karte hain jisme training aur guidance hoti hai.",
    "skill": "✅ Ham sab kuch sikhate hain step-by-step.",
    "phone": "✅ Haan, phone se bhi aap kaam kar sakte ho.",
    "earning": "✅ Skill seekhne ke baad 15-20 din mein kaam mil sakta hai.",
    "time": "✅ 2-4 ghante roj doge to kaafi hai.",
    "student": "✅ Haan, students ke liye perfect hai. Part-time mein kar sakte ho.",
    "payment": "✅ Direct bank account ya UPI pe aayega.",
    "genuine": "✅ Haan, real clients ke real projects milte hain.",
    "office": "✅ Yeh online business model hai, jisme ghar se kaam hota hai.",
    "support": "✅ Haan, aapko har stage pe mentor milta hai.",
    "investment": "✅ Shuruaat mein aapko *koi bhi investment karne ki zarurat nahi hai.*\n\n🎯 Pehle aap thoda bahut kamao, phir wahi paisa system mein laga kar apna kaam expand karo. Hamari guidance ke saath aap zero se shuruaat kar sakte ho!",
    "refund": "✅ Agar system work na kare to aapko refund ka option milta hai.",
    "course": "✅ Yeh koi course nahi, yeh ek business partner model hai.",
    "future": "✅ Isme aap apna khud ka business build kar sakte ho.",
    "language": "✅ Hindi mein training aur communication hoti hai.",
    "age": "✅ 12+ age wale log bhi isme shuruaat kar sakte hain. Agar aapke paas mobile aur dedication hai, to yeh safar aapke liye perfect hai!",
    "certificate": "✅ Skills ke liye digital certification bhi milta hai.",
    "whatsapp": "✅ WhatsApp support available hai jab aap join kar lete ho.",
    "trust": "✅ 1000+ log already is model se earn kar rahe hain.",
    "mobile": "✅ Sirf ek smartphone se bhi aap shuruaat kar sakte ho.",
    "content": "✅ Aapko content, templates aur guidance sab milta hai.",
    "graphic": "✅ Graphic design ke liye tools aur tutorials milenge.",
    "video": "✅ Video editing tools aur apps sikhaye jaate hain.",
    "ads": "✅ Social media ads chalana bhi sikhaya jaata hai.",
    "clients": "✅ Aapko clients milne ke liye full support hota hai.",
    "tools": "✅ Sare tools aur platform ka access diya jaata hai.",
    "earning proof": "✅ Haan, earning proofs bhi share kiye jaate hain.",
    "english": "✅ English seekhne ki zarurat nahi, Hindi mein sab kuch milega.",
    "laptop": "✅ Laptop optional hai, lekin helpful hota hai.",
    "fake": "❌ Yeh fake nahi hai. Real logon ka real kaam hai.",
    "join": "✅ Aap website ke through form bhar ke join kar sakte ho."
}

# ✅ /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.chat.send_action(action=ChatAction.TYPING)
    keyboard = [
        [InlineKeyboardButton("YES ✅", callback_data='yes')],
        [InlineKeyboardButton("NO ❌", callback_data='no')]
    ]
    await update.message.reply_text(
        "🚀 *Safar shuru karo!*\n\n"
        "Agar aap apna time YouTube/Facebook pe waste kar rahe ho bina kisi goal ke, to ab wakt hai badlav ka!\n\n"
        "🎯 Sirf 3 Simple Steps follow karo aur apna online earning journey start karo.\n\n"
        "👇 Shuru karne ke liye ek option choose karo:",
        parse_mode='Markdown',
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ✅ /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 *Madad chahiye?*\n\n"
        "Aap niche diye gaye commands use kar sakte ho:\n\n"
        "/start – Safar shuru karo 🚀\n"
        "/projects – Available projects ke details\n"
        "/contact – WhatsApp pe baat karein\n"
        "/community – TA community join karo\n\n"
        "Kisi bhi topic par sawaal ho to poochho! 👇",
        parse_mode='Markdown'
    )

# ✅ /projects command
async def projects(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠 *Available Projects:*\n\n"
        "✅ Video Editing (Reels, YouTube)\n"
        "✅ Poster & Banner Design\n"
        "✅ Affiliate Marketing Projects\n"
        "✅ Business Page Promotion\n\n"
        "🎯 Har skill ke liye proper training milti hai.\n"
        "🔗 Join karo aur projects lena shuru karo!"
    )

# ✅ /contact command
async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📲 *WhatsApp Contact:*\n\n"
        "👉 Direct baat karne ke liye WhatsApp par message bhejein:\n"
        "[Click to Chat](https://wa.me/917703940672)\n\n"
        "❓ Confusion hai? WhatsApp pe message bhejein ya copy-paste se start karein.\n"
        "👥 Real mentor se baat karke har doubt clear karein.",
        parse_mode='Markdown'
    )

# ✅ /community command
async def community(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌐 *TA Community Join Karein:*\n\n"
        "👉 Hamari main community ka link milega:\n"
        "https://taonlinebusinessag.wixsite.com/my-site-2\n\n"
        "🔗 Uske andar 7 important groups hain – unhe bhi join karein!\n"
        "💬 Network banayein, seekhein, aur projects grab karein!"
    )

# ✅ Button click handler
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'yes':
        keyboard = [[InlineKeyboardButton("NEXT ▶️", callback_data='next1')]]
        await query.edit_message_text(
            "🎉 Welcome to *TA Online Business Agency*!\n\n"
            "🔥 Naye skills sikhkar earning ka safar start karo:\n"
            "- Video Editing\n- Graphic Design\n- Social Media Marketing\n- Affiliate Marketing\n\n"
            "💼 Training + Projects + Business Partnership\n\n"
            "👇 Click 'Next' to continue:",
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif data == 'no':
        keyboard = [
            [InlineKeyboardButton("YES ✅", callback_data='yes')],
            [InlineKeyboardButton("NO ❌", callback_data='no')]
        ]
        await query.edit_message_text(
            "💔 Aapne moka miss kar diya...\n\n"
            "⚠️ Action lene se hi zindagi badalti hai. Soch samajh ke wapas try karo:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif data == 'next1':
        keyboard = [[InlineKeyboardButton("NEXT ▶️", callback_data='next2')]]
        await query.edit_message_text(
            "🌐 *Step 1: Visit our website:*\n"
            "👉 https://taonlinebusinessag.wixsite.com/my-site-2\n\n"
            "📄 Form complete bharein aur har detail padhein.\n"
            "🔎 Koi bhi step skip na karein.\n\n"
            "👇 Jab complete ho jaaye to 'Next' dabayein:",
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif data == 'next2':
        keyboard = [[InlineKeyboardButton("NEXT ▶️", callback_data='next3')]]
        await query.edit_message_text(
            "🟢 *Step 2: WhatsApp se Contact karein:*\n\n"
            "📲 Scroll karke niche 'WhatsApp' button pe click karein.\n"
            "📋 Copy Message option se ready message bhejein.\n"
            "🗣 Leader se 10 minute baat karein, doubts clear karein.\n\n"
            "👇 Complete hone ke baad 'Next' dabayein:",
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    elif data == 'next3':
        await query.edit_message_text(
            "🎉 *Step 3: Ab aap hamare partner ban chuke hain!*\n\n"
            "📘 Aapko milega:\n"
            "✅ TA Partner ID\n"
            "✅ Free eBook guide\n"
            "✅ Community ka link – usmein 7 groups hain, unko bhi join karein.\n\n"
            "🔔 Ab apna sawal likhein – bot ya team turant madad karegi!",
            parse_mode='Markdown'
        )

# ✅ Message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    for keyword, answer in faq_answers.items():
        if keyword in user_message:
            await update.message.reply_text(answer)
            return
    await update.message.reply_text("🤖 Kripya apna sawal clearly likhein – hum madad karne ke liye ready hain!")

# ✅ Main function
def main():
    threading.Thread(target=run_fastapi).start()
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("projects", projects))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("community", community))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot is running...")
    app.run_polling()

if __name__ == '__main__':
    main()

