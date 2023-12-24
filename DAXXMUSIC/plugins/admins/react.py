from DAXXMUSIC import app
from pyrogram import Client, filters
import random




reactions = ["😄", "😊", "👍", "🎉", "👏", "😎", "🔥"]


@app.on_message(filters.command("react", prefixes="/"))
async def react_command(_, message):
    # Send a random reaction
    random_reaction = random.choice(reactions)
    await message.reply_text(random_reaction)
