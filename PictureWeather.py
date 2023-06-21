"""
┏━┓╋┏┳━━━┳┓┏━┳━━━┳━┓┏━┳━━━┳━━━┳┓╋┏┳┓╋╋┏━━━┳━━━┓
┃┃┗┓┃┃┏━━┫┃┃┏┫┏━┓┃┃┗┛┃┃┏━┓┣┓┏┓┃┃╋┃┃┃╋╋┃┏━━┫┏━┓┃
┃┏┓┗┛┃┗━━┫┗┛┛┃┃╋┃┃┏┓┏┓┃┃╋┃┃┃┃┃┃┃╋┃┃┃╋╋┃┗━━┫┗━━┓
┃┃┗┓┃┃┏━━┫┏┓┃┃┃╋┃┃┃┃┃┃┃┃╋┃┃┃┃┃┃┃╋┃┃┃╋┏┫┏━━┻━━┓┃
┃┃╋┃┃┃┗━━┫┃┃┗┫┗━┛┃┃┃┃┃┃┗━┛┣┛┗┛┃┗━┛┃┗━┛┃┗━━┫┗━┛┃
┗┛╋┗━┻━━━┻┛┗━┻━━━┻┛┗┛┗┻━━━┻━━━┻━━━┻━━━┻━━━┻━━━┛
"""

#    (C) Copyright 2023 • https://t.me/nekomodules

# meta developer: @nekomodules
# scope: hikka_only

import requests

from .. import loader, utils


@loader.tds
class WeatherMod(loader.Module):
    """View wather of city with photo"""

    strings = {"name": "PictureWeather"}

    async def pweathercmd(self, m):
        """Weather Picture - use `.pweather <city>`"""
        args = utils.get_args_raw(m).replace(" ", "%20")
        city = requests.get(
            f"https://wttr.in/{args if args != None else ''}.png"
        ).content
        await utils.answer(m, city)
