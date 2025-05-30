from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from telegram.constants import ChatAction
import asyncio
from fastapi import FastAPI
import uvicorn
import threading

# FastAPI server setup
app_fastapi = FastAPI()

@app_fastapi.get("/")
def home():
    return {"message": "TA Telegram Bot is running successfully!"}

def run_fastapi():
    uvicorn.run(app_fastapi, host="0.0.0.0", port=8000)

# Bot Token
BOT_TOKEN = '7952761769:AAE6gGZidtJcspccoSSGcQcJr5HTy_-7ca4'

# FAQ dictionary
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
    "investment": "✅ Shuruaat mein aapko *koi bhi investment karne ki zarurat nahi hai.*\n\n🎯 Pehle aap thoda bahut kamao, phir wahi paisa system mein laga kar apna kaam expand karo.",
    "refund": "✅ Agar system work na kare to aapko refund ka option milta hai.",
    "course": "✅ Yeh koi course nahi, yeh ek business partner model hai.",
    "future": "✅ Isme aap apna khud ka business build kar sakte ho.",
    "language": "✅ Hindi mein training aur communication hoti hai.",
    "age": "✅ 12+ age wale log bhi isme shuruaat kar sakte hain.",
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
    "join": "✅ Aap website ke through form bhar ke join kar sakte ho.",
    
    # New commands with WhatsApp links & community messages
    "help": "🤝 Madad chahiye? WhatsApp par message karo: [Click Here](https://wa.me/917703940672)",
    "projects": "📢 Available projects ke details community mein milenge. TA community join karo!",
    "contact": "📞 WhatsApp pe baat karein: [Click Here](https://wa.me/917703940672)",
    "community": "👥 Hamari TA community ki link milegi, usko join karo aur usmein jo 7 groups hain unko bhi join karo."
}

# /start command with new motivational message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.chat.send_action(action=ChatAction.TYPING)
    await update.message.reply_text(
        "🌟 *Dost*, zindagi ek anmol tohfa hai jo humein sirf ek baar milta hai. Iska har pal soch samajh kar jiyo!\n\n"
        "🔥 Sapne wahi sach hote hain, jinke liye hum apni jaan laga dete hain. Ab waqt hai apne sapno ko haqeeqat mein badalne ka!\n\n"
        "💪 Thoda hausla, thodi mehnat aur zindagi badal dene wali lagan chahiye — tu iske liye tayaar hai.\n\n"
        "❤️ Teri mehnat tera maqsad, aur main tere saath hoon har kadam par.\n\n"
        "👉 Abhi /start likh, apna safar shuru kar aur apni zindagi ka hero ban!",
        parse_mode="Markdown"
    )
    # Show YES / NO buttons after message
    keyboard = [
        [InlineKeyboardButton("YES ✅", callback_data='yes')],
        [InlineKeyboardButton("NO ❌", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👇 Shuru karne ke liye kisi bhi option par click karein:", reply_markup=reply_markup)

# Button handler for all button clicks
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == 'yes':
        keyboard = [[InlineKeyboardButton("NEXT ▶️", callback_data='next1')]]
        await query.edit_message_text(
            "🎉 Zabardast! Aapne ek sahi decision liya hai – Welcome to *TA Online Business Agency*!\n\n"
            "✅ Ab aap ek nayi journey ki shuruaat karne ja rahe hain jisme aap:\n"
            "🎯 Kaam ke saath kamaana bhi seekhenge\n"
            "🎯 Naye skills sikhoge jo demand mein hain:\n"
            "- Video Editing\n"
            "- Graphic Designing\n"
            "- Social Media Marketing\n"
            "- Affiliate Marketing\n"
            "- Aur bhi bahut kuch...\n\n"
            "💼 Aapko milega:\n"
            "✔️ Training + Projects\n"
            "✔️ Business Partner ka role\n"
            "✔️ Earning ke kai options\n\n"
            "👇 Aage badhne ke liye \"Next\" pe click karo:",
            parse_mode='Markdown',
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == 'no':
        keyboard = [
            [InlineKeyboardButton("YES ✅", callback_data='yes')],
            [InlineKeyboardButton("NO ❌", callback_data='no')]
        ]
        await query.edit_message_text(
            "💔 Shayad aap is moka ki value nahi samajh pa rahe ho...\n\n"
            "🌟 Jab tak life mein naya try nahi karoge, naye results nahi milenge.\n"
            "👉 Kya aap hamesha sirf scroll hi karte rahoge? Ab action lene ka time hai!\n\n"
            "👇 Soch samajh ke wapas try karo:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == 'next1':
        keyboard = [[InlineKeyboardButton("NEXT ▶️", callback_data='next2')]]
        await query.edit_message_text(
            "🌐 Step 1: Sabse pehle hamari website par jao:\n"
            "👉 https://taonlinebusinessag.wixsite.com/my-site-2\n\n"
            "📌 Website ke andar har chij ko read karo – images dekho, har text padho.\n"
            "🚫 Koi bhi form ya detail skip mat karo.\n"
            "📄 Pura form bharo, bina skip kiye.\n"
            "⚠️ Pehle detail bharo, fir WhatsApp button pe click karo.\n\n"
            "👇 Jab samajh aa jaaye to ‘Next’ pe click karo:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == 'next2':
        keyboard = [[InlineKeyboardButton("NEXT ▶️", callback_data='next3')]]
        await query.edit_message_text(
            "🟢 Step 2: Form bharne ke baad niche scroll karo – aapko WhatsApp button milega.\n\n"
            "👉 Agar samajh nahi aa raha ki kya bhejna hai to, button ke upar ek “Copy Message” ka option milega. Uspe click karo.\n"
            "📲 WhatsApp pe click karke message paste karo aur bhej do.\n"
            "🗣️ Leader se kam se kam 10 minute baat karo, unse apna doubt clear karo.\n\n"
            "👇 Jab yeh ho jaaye to ‘Next’ dabao:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == 'next3':
        await query.edit_message_text(
            "🥳 Aap ab hamare partner ban chuke ho – *TA Online Business Agency* mein welcome hai!\n\n"
            "📘 Aapko milega:\n"
            "✅ TA Partner ID\n"
            "✅ Ek Free eBook jisme aapko guide milegi kaise projects lene hain\n"
            "✅ Aur milega hamari TA community ka link – usko join karo aur usmein jo 7 groups hain unko bhi join karo.\n\n"
            "🎯 Sab kuch dhyan se padho. Contact form mein koi bhi chiz skip na
