#!/bin/python
from flask import Flask
import subprocess
import time as time_module
import threading
import datetime

def log(message: str = ""):
  print("[" + datetime.datetime.now().isoformat() + "] " + message)

class Light:
  def __init__(self, light: int):
  # Create a new Light with given Identifier.
  # The Identifier is not escaped or validated.
    self.light = light

  _lock = threading.Lock()

  def switch(self, status: str):
  # Sets the status of the light to on (1) or off (any other value).
  # Blocks until the command has been sent and sleeps for 0.1 seconds.
    if status != "1":
      status = "0"

    with Light._lock:
      subprocess.run(["./send", "110000", str(self.light), str(status)],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
      time_module.sleep(0.1)

api = Flask(__name__)

@api.route('/lights/<light>/<status>', methods=['POST'])
def switchLight(light: int, status: int):
  
  if status != "1":
    status = "0"

  if light in ["1","2","3"]:
    log("Switching light " + light + " to " + status)
    Light(int(light)).switch(status)
    log()
  else:
    log("Invalid light: " + light) 
    
  log("Done " + light + ": " + status)
  return "", 204


if __name__ == '__main__':
    api.run(host="0.0.0.0", threaded=True)
