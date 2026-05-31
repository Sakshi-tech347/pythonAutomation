import os

folderpath = os.getcwd()

File = [

    f for f in os.listdir(folderpath)
    if os.path.isfile(os.path.join(folderpath,f))

]

File.sort(key=lambda f :os.path.getctime(os.path.join(folderpath,f)))

for index ,file_name in enumerate(File ,start=1):
    old_path = os.path.join(folderpath,file_name)

    if file_name.split("_")[0].isdigit():
        continue


    new_name = (f"{index}_{file_name}")
    new_path = os.path.join(folderpath,new_name)

    os.rename(old_path , new_path)
    print(f"Renamed:{file_name} -> {new_name}")


print("Done")


