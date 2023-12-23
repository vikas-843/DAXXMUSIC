from DAXXMUSIC import app
from pyrogram import filters
import random




reactions = ["😄", "😊", "👍", "🎉", "👏", "😎", "🔥"]


@app.on_message(filters.command("react", prefixes="/"))
def react_command(_, message):
 random_reaction = random.choice(reactions)
 await message.reply_text(random_reaction)
