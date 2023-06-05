import os

def get_all_files(directory):
    all_files = []
    for root, dirs, files in os.walk(directory):
        for dirss in dirs:
            child_path = os.path.join(directory, dirss)
            for child_root, child_dirs, child_files in os.walk(child_path):
                for file in child_files:
                    if 'image' in file:
                        file_path = os.path.join(child_path, file)
                        mask_path = os.path.join(child_path, file.replace('image', 'label'))
                        write_path = str(file_path) + ' ' + str(mask_path)
                        all_files.append(write_path)
    return all_files

def write_file_paths_to_txt(file_paths, output_file):
    with open(output_file, 'w') as f:
        for file_path in file_paths:
            f.write(file_path + '\n')

# 指定目录
directory = '/mfs/patches/lung/v16_scale20_320_320/patches/'

# 获取所有文件路径
file_paths = get_all_files(directory)

# 指定输出文件名
output_file = 'eval_img_mask_paths.txt'

# 写入文件路径到文本
write_file_paths_to_txt(file_paths, output_file)

print(f"All file paths have been written to {output_file}")
