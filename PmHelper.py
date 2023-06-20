import logging

from telethon import functions, types

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class PmHelperMod(loader.Module):
    """Helps in pm"""

    strings = {
        "name": "PmHelper",
        "who_to_block": "⚠️ <b>Specify whom to block</b>",
        "blocked": (
            "🚫 <a href='tg://user?id={}'>You</a> have been blocked, "
            "<b>I'm really sorry</b>"
        ),
        "who_to_unblock": "<b>⚠️ Specify whom to unblock</b>",
        "unblocked": (
            "<b>✅ Success! PM has been unblocked for"
            " </b> <a href='tg://user?id={}'>this user</a>"
        ),
        "notif_off": "<b>Notifications from denied PMs are silenced.</b>",
        "notif_on": "<b>Notifications from denied PMs are now activated.</b>",
    }

:
        self.config = loader.ModuleConfig(
            "PM_BLOCK_LIMIT", None, lambda m: self.strings("limit_cfg_doc", m)
        )
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self._me = await client.get_me(True)

    async def blockcmd(self, message):
        """Block this user to PM without being warned"""
        user = await utils.get_target(message)
        if not user:
            await utils.answer(message, self.strings("who_to_block", message))
            return
        await message.client(functions.contacts.BlockRequest(user))
        await utils.answer(message, self.strings("blocked", message).format(user))

    async def unblockcmd(self, message):
        """Unblock this user to PM"""
        user = await utils.get_target(message)
        if not user:
            await utils.answer(message, self.strings("who_to_unblock", message))
            return
        await message.client(functions.contacts.UnblockRequest(user))
        await utils.answer(message, self.strings("unblocked", message).format(user))

     
        
        
            
            
    async def notifoffcmd(self, message):
        """Disable the notifications from denied PMs"""
        self._db.set(__name__, "notif", True)
        await utils.answer(message, self.strings("notif_off", message))

    async def notifoncmd(self, message):
        """Enable the notifications from denied PMs"""
        self._db.set(__name__, "notif", False)
        await utils.answer(message, self.strings("notif_on", message))

  
                

