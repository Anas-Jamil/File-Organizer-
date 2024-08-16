import os
import shutil

target_destination = './Downloads'
specified_extensions = ['jpg', 'png', 'txt', 'pdf', 'docx', 'zip', 'jar', 'exe']

for extension in specified_extensions:
    folder_path = os.path.join(target_destination, extension)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

for i in os.listdir(target_destination):
    file_path = os.path.join(target_destination, i)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(i)[-1][1:]
        if file_extension in specified_extensions:
            destination_folder = os.path.join(target_destination, file_extension)
            shutil.move(file_path, os.path.join(destination_folder, i))
