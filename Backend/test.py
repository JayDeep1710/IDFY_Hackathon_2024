import time
from utils import *
from gliner import GLiNER
import os


text = """
\033[92m                                                                     
                                                                     
\033[31mIIIIIIIII\033[92mDDDDDDDDDDDDD     \033[31mFFFFFFFFFFFFFFFFFFFFF\033[92mYYYYYYY       YYYYYYY
\033[31mI:::::::I\033[92mD::::::::::::DDD  \033[31mF:::::::::::::::::::F\033[92mY:::::Y       Y:::::Y
\033[31mI:::::::I\033[92mD:::::::::::::::DD\033[31mF:::::::::::::::::::F\033[92mY:::::Y       Y:::::Y
\033[31mII::::::I\033[92mDDD:::::DDDDD:::::FF\033[31m::::::FFFFFFFFF:::F\033[92mY::::::Y     Y::::::Y
  \033[31mI::::I   \033[92mD:::::D    D:::::D\033[31mF:::::F       \033[31mFFFFF\033[92mYYY:::::Y   Y:::::YYY
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF:::::F               \033[92mY:::::Y Y:::::Y   
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF::::::FFFFFFFFFF\033[92m      Y:::::Y:::::Y    
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF:::::::::::::::F\033[92m       Y:::::::::Y     
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF:::::::::::::::F\033[92m        Y:::::::Y      
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF::::::FFFFFFFFFF\033[92m         Y:::::Y       
  \033[31mI::::I   \033[92mD:::::D     D:::::\033[31mF:::::F\033[92m                   Y:::::Y       
  \033[31mI::::I   \033[92mD:::::D    D:::::D\033[31mF:::::F\033[92m                   Y:::::Y       
\033[31mII::::::I\033[92mDDD:::::DDDDD:::::FF\033[31m:::::::FF\033[92m                 Y:::::Y       
\033[31mI:::::::I\033[92mD:::::::::::::::DD\033[31mF::::::::FF\033[92m              YYYY:::::YYYY    
\033[31mI:::::::I\033[92mD::::::::::::DDD  \033[31mF::::::::FF\033[92m              Y:::::::::::Y    
\033[31mIIIIIIII\033[92mDDDDDDDDDDDDD      \033[31mFFFFFFFFFFF\033[92m              YYYYYYYYYYYYY                                          
                                                                     
                                                                     \033[0m
"""
d = {1:"Texts", 2:"Docs", 3:"Pdfs" ,4:"CSV", 5:"Images", 6:"Codes", 7:"All"}
# Split the text into lines
lines = text.splitlines()

# Loop through each line and print it with a delay
for line in lines:
    print(line)
    time.sleep(0.1)  # Adjust the delay (in seconds) as needed


print("\033[92m" + "=" * 100 + "\033[0m")

print("\033[32m 1. Search Database \033[0m")
print("\033[32m 2. Search Local Folder \033[0m")
print("\033[32m 3. Search Cloud storage \033[0m")
# ANSI escape code for green text
print("\033[92m" + "=" * 100 + "\033[0m")

i = input()
# print(f"\033[32m{i} \033[0m")
if i=="1":
    pass
elif i=="2":
    print("\033[32mEnter the path to the local folder\033[0m")
    path = input()
    copy_files_by_extension(path)
    print("\033[32mWhat to search?\033[0m")
    for i in range(1,8):
        print(f"\033[32m {i}. {d[i]} \033[0m")
    j = int(input())
    search(j)
    
elif i=="3":
    pass
else:
    print(f"\033[32m{i} is not a valid input \033[0m")
    