from pyrogram import Client, filters as f
import requests as rq, random, os
from time import sleep

token = os.getenv("TOKEN")
sendId = os.getenv("SENDID").replace(" ", ",").split(",")
getId = os.getenv("GETID").replace(" ", ",").split(",")
botToken = os.getenv("BOTTOKEN")

ifTanimlama = True

def tanimlama():
	for i in sendId:
		a = rq.get(f"https://api.telegram.org/bot{botToken}/sendMessage?chat_id={i}&text=tanımlama!").json()
		sleep(2)
		try:
			a = rq.get(f"https://api.telegram.org/bot{botToken}/deleteMessage?chat_id={i}&message_id={str(a['result']['message_id'])}").json()
		except:
			print("Hatalı Grup/Kanal İd Veya Bot Grupta Yetkili Değil!!")
			return


_rg = Client(token,"5775802","6011ffc6cec69c60ef86456db0ce4d09")



@_rg.on_message(f.group | f.channel)
async def _(b, m):
	global ifTanimlama
	chat = m.chat
	if ifTanimlama:
		ifTanimlama = False
		tanimlama()
		sleep(10)

	if str(chat.id) not in getId:
		return

	if m.photo:
		for i in sendId:
			try:
				await b.send_photo(chat_id=i, photo=m.photo.file_id, caption=m.caption)
			except:
				try:
					await b.send_photo(chat_id=i, photo=m.photo.file_id)
				except:
					pass
	elif m.video:
		for i in sendId:
			try:
				await b.send_video(chat_id=i, video=m.video.file_id, caption=m.caption)
			except:
				try:
					await b.send_video(chat_id=i, video=m.video.file_id)
				except:
					pass
	elif m.text:
		for i in sendId:
			try:
				await b.send_message(chat_id=i, text=m.text)
			except Exception as r:
				print(r)

_rg.run()
