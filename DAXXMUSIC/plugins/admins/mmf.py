from DAXXMUSIC import app
from pyrogram import Client, filters
import random



# Command handler for memify
@app.on_message(filters.command("mmf", prefixes="/"))
async def memify_command(_, message):
    # Extract text after the command
    text_to_memify = " ".join(message.command[1:])
    
    # Memify logic (you can customize this based on your requirements)
    memified_text = ""
    for char in text_to_memify:
        if random.choice([True, False]):
            memified_text += char.upper()
        else:
            memified_text += char.lower()

    # Send the memified text as a reply
    await message.reply_text(memified_text)
