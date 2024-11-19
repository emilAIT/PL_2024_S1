# import os
# import subprocess

# directory = "C:\\Users\\User\\Downloads\\domashka" 

# with open('output.txt', 'w') as fid:
#     for filename in os.listdir(directory):
#         print(f'\n\n\n***** RUNNING FILE -> {filename}')
#         if filename.endswith(".py"):  
#             filepath = os.path.join(directory, filename)
#             try:
#                 print(f"Running: {filename}")
#                 subprocess.run(["python", filepath], check=True)
#                 fid.write(f'{filename} -> SUCCESS\n')
#             except:
#                 try:
#                     print(f"Error running {filename}")
#                     fid.write(f'{filename} -> FAIL\n')
#                 except:
#                     pass


import os
import subprocess

directory = "C:\\Users\\User\\Downloads\\domashka" 

with open('output.txt', 'w') as fid:
    for filename in os.listdir(directory):
        print(f'\n\n\n***** RUNNING FILE -> {filename}')
        if filename.endswith(".py"):  
            filepath = os.path.join(directory, filename)
            try:
                print(f"Running: {filename}")
                subprocess.run(["python", filepath], check=True)
                fid.write(f'{filename} -> SUCCESS\n')
            except:
                try:
                    print(f"Error running {filename}")
                    fid.write(f'{filename} -> FAIL\n')
                except:
                    pass
