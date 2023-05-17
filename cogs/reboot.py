import discord
from discord.ext import commands
import os
import time

class Reboot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def reboot(self, ctx):
        await ctx.send("Rebooting...")
        os.system("python main.py")
        time.sleep(0.2)

    @reboot.error
    async def reboot_error(self, error, ctx):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Parece que não tens premissões.")

async def setup(client):
    await client.add_cog(Reboot(client))