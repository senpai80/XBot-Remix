import asyncio
import re
import time
from time import sleep
from platform import python_version, uname
from userbot import CMD_HELP, ZALG_LIST, ALIVE_NAME, bot
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
modules = CMD_HELP
# ============================================

@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	sleep(1)
	await typew.edit("'Hallo Semua Saya` **{DEFAULTUSER}**")
	sleep(2)
	await typew.edit("`Assalamualaikum.....😚`")
# Owner @Si_Dian

@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	sleep(1)
	await typew.edit("'Hallo Semua Saya` **{DEFAULTUSER}**")
	sleep(2)
	await typew.edit("`Assalamualaikum.....😚`")
# Owner @Si_Dian

@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	sleep(1)
	await typew.edit("`Astaghfirulloh Jawab Salam Dong...`")
	sleep(1)
	await typew.edit("`Waallaikumsalam......`")
# Owner @Si_Dian

@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	sleep(1)
	await typew.edit("`Astaghfirulloh Jawab Salam Dong...`")
	sleep(1)
	await typew.edit("`Waallaikumsalam.....`")
# Owner @Si_Dian


CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."   
})  
