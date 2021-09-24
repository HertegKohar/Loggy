from queue import Queue
from log_format import log_format


def consume_logs(work: Queue, finished: Queue)->None:
  while True:
    if not work.empty():
      line = work.get()
      #Classify line here
    else:
      finish = finished.get()
      if finish:
        break



# Consumer
# def perform_work(work: Queue, finished: Queue) -> None:
#     """Consumes the data given from the producer function

#     Args:
#         work (Queue): Filled with random numbers to be assigned
#         finished (Queue): Boolean as to whether the work if finished or not
#     """
#     counter = 0
#     while True:
#         if not work.empty():
#             v = work.get()
#             display(f"Consuming {counter}: {v}")
#             counter += 1
#         else:
#             q = finished.get()
#             if q:
#                 break
#             display("finished")

#--------------------------------------------------------------

# This is how I calassified the logs
# Dispatch event 
# POST
# WebSocket event
# HTTP connection
# websocket alive

# how to create a web socket log object - same method for all the other log types
# websocket_log_object = log_format.websocket_alive_log("DEBUG 2021-09-17 18:16:31,681 - For Shard ID None: WebSocket Event: {'t': None, 's': None, 'op': 11, 'd': None}")

# how to write to both file options - file names are already made ;)
# websocket_log_object.write_to_csv()
# websocket_log_object.write_to_file()

#--------------------------------------------------------------