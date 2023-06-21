
# █▄░█ █▀▀ █▄▀ █▀█ █▀▄▀█ █▀█ █▀▄ █░█ █░░ █▀▀ █▀
# █░▀█ ██▄ █░█ █▄█ █░▀░█ █▄█ █▄▀ █▄█ █▄▄ ██▄ ▄█

#    (C) Copyright 2023 • https://t.me/nekomodules

# meta developer: @nekomodules
# scope: hikka_only

from telethon import functions
from .. import loader, utils


@loader.tds
class PmHelperMod(loader.Module):
    """
    Helps in pm
    """

    strings = {
        "name": "PmHelper",
        "blocked": "<b>{} was blocked.</b>",
        "unblocked": "<b>{} unblocked.</b>",
        "delcontact": "<b>{} was removed from contacts.</b>",
        "who_to_block": "<b>Indicate, who to block.</b>",
        "who_to_unblock": "<b>Indicate, who to unblock.</b>",
        "who_to_delcontact": "<b>Indicate, who to remove from contacts.</b>",
    }

    def __init__(self):
        self.me = None

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        self.me = await client.get_me(True)

    async def blockcmd(self, message):
        """Add user to blacklist."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            if not user:
                await utils.answer(message, self.strings["who_to_block"])
                return
        await message.client(functions.contacts.BlockRequest(user))
        await utils.answer(message, self.strings["blocked"].format(user.first_name))

    async def unblockcmd(self, message):
        """Unblock user."""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            if not user:
                await utils.answer(message, self.strings["who_to_unblock"])
                return
        await message.client(functions.contacts.UnblockRequest(user))
        await utils.answer(message, self.strings["unblocked"].format(user.first_name))

    async def delcontcmd(self, message):
        """Delete contact"""
        args = utils.get_args(message)
        reply = await message.get_reply_message()
        if message.chat_id != (await message.client.get_me()).id and message.is_private:
            user = await message.client.get_entity(message.chat_id)
        else:
            if reply:
                user = await message.client.get_entity(reply.sender_id)
            else:
                user = await message.client.get_entity(
                    int(args) if args.isnumeric() else args
                )
            if not user:
                await utils.answer(message, self.strings["who_to_delcontact"])
                return
        await message.client(functions.contacts.DeleteContactsRequest(id=[user.id]))
        await utils.answer(message, self.strings["delcontact"].format(user.first_name))

    async def addcontcmd(self, message):
        """Add to contact"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if not args:
            return await message.edit("<b>Where args?.</b>")
        if not reply:
            return await message.edit("<b>Where reply?</b>")
        else:
            user = await message.client.get_entity(reply.sender_id)
        try:
            await message.client(
                functions.contacts.AddContactRequest(
                    id=user.id,
                    first_name=args,
                    last_name=" ",
                    phone="phone",
                    add_phone_privacy_exception=False,
                )
            )
            await message.edit(
                f"<code>{user.id}</code> added to contacts <code>{args}</code>"
            )
        except:
            return await message.edit(
                "<b>Something went wrong (come up with different reasons).</b>"
            )
