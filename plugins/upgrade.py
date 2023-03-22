"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price ₹10 / per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price ₹25 / per Month 
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price ₹40  ind / per Month
	
	
	Pay Using Upi I'd ```srinisathyasabarish@okaxis```
	
	After Payment Send Screenshots Of 
        Payment To Admin @Ownerofsparkmovirs"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Ownerofsparkmovirs")], 
        			[InlineKeyboardButton("UPI",url = "@Ownerofsparkmovirs"),
        			InlineKeyboardButton("UPI",url = "@Ownerofsparkmovirs")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price ₹10 / per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price ₹25 / per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price ₹40 / per Month
	
	
	Pay Using Upi I'd ```srinisathyasabarish@okaxis```
	
	After Payment Send Screenshots Of 
        Payment To Admin @Ownerofsparkmovirs"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Ownerofsparkmovirs")], 
        			[InlineKeyboardButton("UPI",url = "srinisathyasabarish@okaxis"),
        			InlineKeyboardButton("UPI",url = "srinisathyasabarish@okaxis")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
