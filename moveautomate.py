import os
import glob
import shutil 
    
folder = "02_Monitoring, Metrics and Analysis"
while True:
   current  = glob.glob("*.mp4")
   if len(current)!=0:
       path = "Sysops/"+folder+"/"
       allFiles = glob.glob(path+"*.mp4")
       count = len(allFiles)
       currentname = current[0]
       shutil.copy(currentname, path+str(count+1)+"_"+currentname)
       shutil.os.remove(currentname)
   else:
       continue
    

    
        
    
    

