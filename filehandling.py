import os

path = r"recent_file"
dir_list = os.listdir(path)
  
print("Files and directories in '", path, "' :") 
  
# print the list
print(dir_list)

os.remove(path+str("\\")+dir_list[0])