

from aiohttp import web
from pyrogram import Client
from config import Config
from BotzPW.web_support import web_server

class BotzPW(Client):
    def __init__(self):
        super().__init__(
            name="BotzPW",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "BotzPW"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.uptime = Config.BOT_UPTIME
        self.force_channel = Config.FORCE_SUB
        if Config.FORCE_SUB:
            try:
                link = await self.export_chat_invite_link(Config.FORCE_SUB)
                self.invitelink = link
            except Exception as e:
                print(e)
                print("Make Sure Bot admin in force sub channel")
                self.force_channel = None
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, Config.PORT).start()
        print(f"{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️")
        for id in Config.ADMIN:
            try:
                await self.send_message(id, f"**__{me.first_name}  Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️__**")
            except:
                pass
        
    async def stop(self, *args):
        await super().stop()
        print("Bot Stopped 🙄")
        
BotzPW().run()

