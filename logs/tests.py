# from django.test import TestCase

# Create your tests here.
import re, os, stat
file_list = []
def get_file(dir_path):
    path_list = os.listdir(dir_path)  # 获取当前路径下的文件名，返回List
    for file in path_list:
        new_path = os.path.join(dir_path, file) # 将文件命加入到当前文件路径后面

        # if os.path.isdir(newDir): # 如果是文件夹
        if os.path.isfile(new_path):  # 如果是文件
            user = file.split('@')[0]
            u_ip = file.split('@')[1].split('_')[0]
            u_date = file.split('@')[1].split('_')[1]
            u_datetime = '-'.join(list(re.findall(r'(\d{4})(\d{2})(\d{2})', u_date)[0])) + ' {}'.format(file.split('@')[1].split('_')[2])
            # user = SysUser(u_name=user, u_ip=u_ip, u_create=u_datetime)
            # user.save()
            os.chmod(new_path, stat.S_IRUSR + stat.S_IWUSR  + stat.S_IXUSR )
            i = 1
            print(new_path)
            with open(new_path,'r') as fp:
                line = fp.readline()
                while line:
                    h_time = line.split(';')[0].split(':')[1].strip()
                    h_user_index = line.split(';')[0].split(':')[2]
                    handel = line.split(';')[1]
                    
                    # print(line)
                    print(h_time, h_user_index, handel, i)
                    i += 1
                    line = fp.readline()
                    
        else:
            get_file(new_path)
    return file_list 

if __name__ == "__main__":
    get_file('history')
