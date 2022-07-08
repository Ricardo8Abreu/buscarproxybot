from pyrogram import Client
from pyrogram.types import Message
import random
from config import *
import search_pr
import threading

bot = Client("bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
cfg = {}
data_pr = []

@bot.on_message()
async def messages_control(c: Client, m: Message):
	username = m.from_user.username
	msg = m.text
	
	if msg is None:
		msg = ''
		
	if username == useradm:
		pass
	else:
		await m.reply('❌Usted no tiene acceso al bot contacta a @diago8888❌')
		return
	
	if msg == '/start':
		await m.reply('👋Bienvenido '+username+'\nSoy un bot para buscar 🛰️proxys🛰️\n👾Code By: @diago8888 | 🛠️1.0')
		return
			
	if msg.startswith('/myuser'):
		await m.reply('👤Usuario: @'+username+'\n➖Ran_Min: '+cfg[username]['range_min']+'\n➕R_Max: '+cfg[username]['range_max']+'\n🌐Ip: '+cfg[username]['ip'])
		return
		
	if msg.startswith('/data'):
		await m.reply(data_pr)
		return
		
	if msg.startswith('/help'):
		help = "🆘Ayuda🆘\n\nDebes configurar⚙️el bot ejemplo: /cfg_pr rangominimo rangomaximo ip ,algo así /cfg_pr 1 65000 152.158.49.127"
		await m.reply(help)
		return
		
	if msg.startswith('/cfg_pr'):
		splitmsg = msg.split(' ')
		cfg[username] = {'range_min':splitmsg[1],'range_max':splitmsg[2],'ip':splitmsg[3]}
		await m.reply('⚙️Configurado⚙️')
		return

	if msg.startswith('/search_pr'):
		await m.reply('🛰️Buscando proxy🛰️')
		search_pr.search_pr_i(username,cfg)
		return
    
#Iniciar el bot
if __name__ == "__main__":
	print("🛰️Bot iniciado🛰️")
	bot.run()