
import shutil
import os

srchstr = "C:\\Users\\mysti\\Desktop\\zips"

zipdir = "C:\\Users\\mysti\\Desktop\\zips"

print("")

print("Zipping Files.")

print("")

for dirs in os.walk(srchstr):

    for dir in dirs:

        #for subdir in subdirs:
        
        #if  filepath.endswith(".wav") and (("HomeLoops" in filepath) or  ("Trance" in filepath)) and  (("Pad"in filepath) or ("Strings" in filepath)):  

        if dir.endswith("zips"):

            shutil.make_archive(dir, 'zip', zipdir)

            print("")

            print("Zipping.")
                            
print("")

print("Directories Zipped and ready.")

print("")