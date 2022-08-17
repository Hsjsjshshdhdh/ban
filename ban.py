import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var


logging.basicConfig(level=logging.INFO)

print("Starting.....")

Riz = TelegramClient('Riz', Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)


SUDO_USERS = []
for x in Var.SUDO: 
    SUDO_USERS.append(x)

@Riz.on(events.NewMessage(pattern="^مودي مبضون"))
async def testing(event):
  if event.sender_id in SUDO_USERS:
   if not event.is_group:
        Reply = f"Noob !! Use This Cmd in Group."
        await event.reply(Reply, parse_mode=None, link_preview=None )
   else:
       await event.delete()
       RiZoeL = await event.get_chat()
       RiZoeLop = await event.client.get_me()
       admin = RiZoeL.admin_rights
       creator = RiZoeL.creator
       if not admin and not creator:
           await event.reply("ليس لدي صلاحية الحظر في الجروب!")
           return
       await event.reply("جاري فشخ الروم🤓")
       everyone = await event.client.get_participants(event.chat_id)
       for user in everyone:
           if user.id == RiZoeLop.id:
               pass
           try:
               await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None,view_messages=True)))
           except Exception as e:
               await event.edit(str(e))
           await sleep(0.5)


@Riz.on(events.NewMessage(pattern="^مودي مبقاش مبضون"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "خلاص كفايه عليكو كدا هرحمكو المره دي🤓"
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await Riz.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


print("\n\n")
print("Bot Started")

Riz.run_until_disconnected()
