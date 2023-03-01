#CodeWithAlfred
#automate_ideas
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import json

class Handler(FileSystemEventHandler):
    i=1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/"+ filename
            dest = folder_destination + "/" + filename
            os.rename(src, dest)

folder_to_track = "/home/c0d3r/Desktop/PROJECTS"
folder_destination = "/home/c0d3r/Desktop/FCC"
event_handler = Handler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    observer.join()
