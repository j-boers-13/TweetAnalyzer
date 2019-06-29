import os

def main():

    print("Writing may...")
    rootdir = "/run/user/1000/gvfs/smb-share:server=boers-desktop,share=05/"
    may = open("may.txt","w+")
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".json"):
                may.write(filepath + "\n")
    may.close()
      
    print("Writing june...")
    rootdir = "/run/user/1000/gvfs/smb-share:server=boers-desktop,share=06/"
    june = open("june.txt","w+")
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".json"):
                june.write(filepath + "\n")
    june.close()
                    
    print("Writing july...")      
    rootdir = "/run/user/1000/gvfs/smb-share:server=boers-desktop,share=07/"
    july = open("july.txt","w+")
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            filepath = subdir + os.sep + file

            if filepath.endswith(".json"):
                july.write(filepath + "\n")
    july.close()            
          
    print("Samples have been filed according to month.")



main()

