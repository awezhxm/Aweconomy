from disnake import *
from disnake.ext import commands
from assets import functions as func
import traceback
from cogs.points_commands import PointsCommands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True, case_insensitive=True)
    async def help(self,ctx):
        e = Embed(title=":notepad_spiral: Help Menu :notepad_spiral:", description="• Prefix is /", color=ctx.author.color)
        e.add_field(name="Commands", value="• `/points <username>` View how many {PointsName} you or someone has.\n• `/points add <username> <number>` Supply {PointsName} to any member.*\n• `/points remove <member> <number>` Remove {PointsName} from any member.* \n• `leaderboard` `/leaderboard` See ranking of all members.\n• `/shop`: Shows the shop\n• `/shop add <price> <item-name>`: Add a item in the shop.\n• `/shop remove`: Remove a item from the shop.\n• `/shop buy`: Buy a item from the shop.\n*: These commands are admin only")
        await ctx.send(embed=e)

def setup(bot):
    bot.add_cog(Help(bot))
