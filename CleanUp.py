import os, time, datetime

def get_list_files(path):
    
    file_list = []

    for folderName, subfolders, filenames in os.walk(path):
        for filename in filenames:
            path_file = f"{folderName}\{filename}"
            file_list.append(path_file)
            
    return file_list

def get_timestampfile(path_file):

    timestamp = os.stat(path_file).st_ctime  

    return timestamp

# +++++++++++++++++++++++++++++++++++++++++++++++

remaining_days = 1  # Preencher a quantidade de dias de retenção

now = time.time()
parameter = now - (remaining_days * 86400)

files = get_list_files("C:\\Users\\rodolfho.queiroz\\Downloads") # Informar a pasta "pai" em que o script deve percorrer

for file in files:
    f = get_timestampfile(file)

    if f < parameter:
        
        print(F"Deleted File: {file}")
        os.remove(file)
        
print("End execution")
 
