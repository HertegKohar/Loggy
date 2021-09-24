from discord.ext import commands
from logger.logger import LogStream
class Bot(commands.Bot):
  def __init__(self,prefix: str,streamer:LogStream ):
    super().__init__(command_prefix=prefix)
    self.log_stream = streamer
    self.consumer_thread=None
    self.producer_thread=None
    


  