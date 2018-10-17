import time
import glob
import shutil 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        folder = "10_Practical Uses of S3"
        current  = glob.glob("*.mp4")
        if len(current)!=0:
            path = "S3_Master_class/"+folder+"/"
            allFiles = glob.glob(path+"*.mp4")
            count = len(allFiles)
            currentname = current[0]
            shutil.copy2(currentname, path+str(count+1)+"_"+currentname)
            shutil.os.remove(currentname)
        # print ("Got it!")


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    

    
        
    
    

