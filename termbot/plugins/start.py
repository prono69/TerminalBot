#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Telegram Terminal Bot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, Filters

from termbot import (
    AUTH_USERS,
    HELP_STICKER
)


@Client.on_message(~Filters.chat(chats=AUTH_USERS))
async def not_auth_text(client, message):
    await message.reply("`Bonjour! I am Online and Healthy. Now Fu#k Off. \n Nikal Lawde`🐈")
