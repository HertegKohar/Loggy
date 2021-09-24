import logging
class LogStream:
  def __init__(self):
    self.logs=[]

  def write(self,msg):
    self.logs.append(msg)

  def flush(self):
    pass

  def refresh(self):
    self.logs = []

  def __str__(self):
    return str(self.logs)

def initialize():
  file_handler = logging.FileHandler("logging.txt",mode="w")

  streamer = LogStream()
  stream_handler = logging.StreamHandler(stream = streamer)


  logging.basicConfig(
        handlers = [file_handler,stream_handler],
        format="%(levelname)s %(asctime)s - %(message)s",
        level=logging.DEBUG,
    )


  logging.disable(logging.CRITICAL)
  return logging.getLogger(),streamer
  

  