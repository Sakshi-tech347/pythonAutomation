import sys
import schedule
import time 
import os

def BackupFiles(source , Destination ):
    copied_files= []

    print("creating the backup folder for bakup process")
    os.makedirs(Destination,exist_ok=True)

    for root , dir ,files in os.walk(source):
        for file in files:
            src_path = os.path.join(root,file)

            relative= os.path.relpath(src_path,source)
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            shutil.copy2(src_path,dest_path)
            copied_files.append(relative)
    return copied_files

    

def DataShieldStart(Source = "Data"):
    BackupName= "DesktopBackup"
    print("Backup Process started Succefully at :",time.ctime())

    files = BackupFiles(Source , BackupName)

    print("Report About the Backup ")

    for name in files:
        print(name)


def main():
    Border = "-"*50
    print(Border)
    print("------------------Data Shield system ------------------")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]== "--h" or sys.argv[1]== "--H"):
            print("This scipt is used to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")

        elif(sys.argv[1]== "--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")

    elif(len(sys.argv)==3):
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        schedule.every(int(sys.argv[1])).minutes.do(fun,sys.argv[2])

        print("Data shield started succesfully")
        print("time intrvals in minutes :",sys.argv[1])
        print("press Ctrl+ c to stop the exrcution ")

        while (True):
            schedule.run_pending()
            time.sleep(1)
        
    else:
        print("Invalid number of commandline argument  ")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details") 
    
    print(Border)
    print("---------- Thank you for using our script -----------")
    print(Border)

if __name__ == "__main__":
    main()
