import aiohttp
from discord.ext import commands

from tux.bot import Tux


class Accuracy(commands.Cog):
    def __init__(self, bot: Tux) -> None:
        self.bot = bot
        self.url = "https://accuratelinuxgraphs.com/api/graphs/random"  # The url to get our data (you could edit this for something else but you'd have to change data points too)

    @commands.hybrid_command(name="accuracy", aliases=["a"], description="Get a Random Accurate Graph")
    @commands.guild_only()
    async def accuracy(self, ctx: commands.Context[Tux]) -> None:
        async with aiohttp.ClientSession() as session, session.get(self.url) as resp:
            if resp.status == 200:
                data = await resp.json()
                graph_url = f"https://accuratelinuxgraphs.com{data['graphImgUrl']}"
                await ctx.send(content=f"{data['caption']}\n{graph_url}")
            else:
                await ctx.send("Could not fetch graph data.")


async def setup(bot: Tux) -> None:
    await bot.add_cog(Accuracy(bot))
