import discord
from discord.ext import commands
from discord import app_commands
import random

class Roll(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @app_commands.command(name="roll",description="サイコロを振る")
    async def roll(self, interaction: discord.Interaction, sides: int = 6):
        """サイコロを振るコマンド
        
        Args:
            interaction (discord.Interaction): インタラクションオブジェクト
            sides (int, optional): サイコロの面の数. 初期は6.
        """
        if sides < 1:
            await interaction.response.send_message("サイコロの面の数は1以上で指定してください。")
            return
        result = random.randint(1,sides)
        await interaction.response.send_message(f"{sides}面ダイス → **{result}**")

async def setup(bot):
    await bot.add_cog(Roll(bot))