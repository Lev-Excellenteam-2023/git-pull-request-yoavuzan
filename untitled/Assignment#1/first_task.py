import os

# while True:
#     path = input("please enter a path to folders")
#     if os.path.isdir(path):
#         break
#     else:
#         print("This direction dos'nt exist please try again")


def deep_list(path):
    if not os.path.isdir(path):#check if the path exist
        return []
    os.chdir(path)
    list_all_files = os.listdir(path)
    for file in list_all_files:
        if not file.startswith("deep"):
            list_all_files.remove(file)
    return list_all_files