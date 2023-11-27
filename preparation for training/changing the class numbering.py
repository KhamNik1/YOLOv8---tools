import os
import shutil

source_folder ='C:\\Users\\Desktop\\dataset3.0\\valid\\labels'
destination_folder = 'C:\\Users\\Desktop\\dataset3.7\\valid\\labels'
n1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]     #initial classes
n2 = [0, 1, 2, 3, 4, 5, 4, 4, 6, 7]     #modified classes

def find_and_convert(num):
    if num in n1:
        return n2[n1.index(num)]
    else:
        return num

def convert_line(line):
    nums = line.strip().split()
    nums[0] = str(find_and_convert(int(nums[0])))
    return ' '.join(nums)

def copy_file_with_convert(file_path, destination_folder):
    with open(file_path, 'r') as file:
        filename = os.path.basename(file_path)
        new_file_path = os.path.join(destination_folder, filename)
        with open(new_file_path, 'w') as new_file:
            first_line = True
            for line in file:
                if first_line:
                    new_line = convert_line(line)
                    first_line = False
                else:
                    new_line = "\n"+convert_line(line)

                new_file.write(new_line)

def copy_text_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print("The source folder does not exist.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        if os.path.isfile(file_path) and filename.endswith('.txt'):
            copy_file_with_convert(file_path, destination_folder)

    print("All text files have been copied successfully.")

copy_text_files(source_folder, destination_folder)
