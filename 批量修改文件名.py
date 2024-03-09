import os  

#此文件可以批量把文件夹内文件修改名字为：名字1，名字2...以此类推，适用于sovits模型训练需要的干音在分割文件以后批量修改文件名

def rename_files_with_fixed_letters_and_numbers(directory):  
    file_count = 0  
    for filename in os.listdir(directory):  
        file_count += 1  
        new_filename = "名字" + str(file_count) + ".wav"  # 固定字母和顺序数字的组合  
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))  
  
# 调用函数，指定要修改的目录  
rename_files_with_fixed_letters_and_numbers("需要批量修改文件的所在文件夹路径")