
import shutil
import os

srchstr = "C:\\Users\\mysti\\Desktop\\zips"

zipdir = "C:\\Users\\mysti\\Desktop\\zips\\unzipped"

print("")

print("Un-Zipping Files.")

print("")

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file
        
        #if  filepath.endswith(".wav") and (("HomeLoops" in filepath) or  ("Trance" in filepath)) and  (("Pad"in filepath) or ("Strings" in filepath)):  
        if  filepath.endswith(".zip"):  

            shutil.unpack_archive(filepath, zipdir)

            print("")

            print("Unzipping ", file)
                         
print("")

print("Directories unzipped and ready.")

print("")