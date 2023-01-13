import os 

folders = os.listdir('data')
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f'data/{folder}'))
    
    