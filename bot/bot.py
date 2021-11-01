from discord.ext import commands
from logger.logger import LogStream


#Inherit from discord Bot class
class Bot(commands.Bot):
    def __init__(self, prefix: str, streamer: LogStream):
        """Description: Constructor for discord Bot inherited from discord.ext.commands creates a bot which adds custom properties.
    

    Args:
        prefix (str): The prefix the which the bot recognizes to execute a named command
        streamer (LogStream): The stream of the logs which the bot will process when an appropriate command is called
    """
        super().__init__(command_prefix=prefix)
        self.log_stream = streamer