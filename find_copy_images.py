import os
import shutil

def find_and_copy_files(source_folder, destination_folder, target_filename):
    # 遍历指定文件夹内所有文件和子文件夹
    for root, dirs, files in os.walk(source_folder):
        # 遍历当前文件夹内的所有子文件夹
        for file in dirs:
            target_name = file.split('_')[0] + '.png'
            child_dirs = os.path.join(source_folder, file).replace('\\','/')
            # 遍历子文件夹内的所有文件与文件夹
            for child_root, child_dir, child_files in os.walk(child_dirs):
                # 检查文件是否是指定的目标文件
                for target_file in child_files:
                    if target_file == target_filename:
                        # 构造源文件路径和目标文件路径
                        source_path = os.path.join(child_root, target_file).replace('\\','/')
                        destination_path = os.path.join(destination_folder, target_name).replace('\\','/')
                        # 复制文件
                        shutil.copyfile(source_path, destination_path)
                        print(f'已复制文件: {source_path} -> {destination_path}')

# 指定源文件夹和目标文件夹路径
source_folder = './jsons'
destination_folder = './labels'
target_filename = 'label.png'

# 调用函数进行文件复制
find_and_copy_files(source_folder, destination_folder, target_filename)
