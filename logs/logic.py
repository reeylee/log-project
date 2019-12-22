from .models import UserLogin, UserHandle
import re, os, stat, datetime
file_list = []
def create_handle_log(dir_path):
    # data = {'code':0, 'status':'ok'}
    path_list = os.listdir(dir_path)  # 获取当前路径下的文件名，返回List
    if not path_list:
        # data['code'] = 1
        # data['status'] = 'no file'
        return #data 
    for file in path_list:
        new_path = os.path.join(dir_path, file) # 将文件命加入到当前文件路径后面

        # if os.path.isdir(newDir): # 如果是文件夹
        if os.path.isfile(new_path):  # 如果是文件
            # 解析文件名,获取登陆道用户名,登陆ip,登陆时间信息
            user = file.split('@')[0]
            u_ip = file.split('@')[1].split('_')[0]
            u_date = file.split('@')[1].split('_')[1]
            u_datetime = '-'.join(list(re.findall(r'(\d{4})(\d{2})(\d{2})', u_date)[0])) + ' {}'.format(file.split('@')[1].split('_')[2])
            
            # 把登陆信息写入数据库并保存
            user = UserLogin(l_user=user, l_ip=u_ip, l_time=u_datetime)
            user.save()
            
            # 修改文件权限,完成写入后删除
            os.chmod(new_path, stat.S_IRUSR + stat.S_IWUSR  + stat.S_IXUSR )
            i = 1 # 按照操作顺序排序,更容易区分同一时间内的操作顺序
            with open(new_path,'r') as fp:
                line = fp.readline()
                while line: #一行行读取文件
                    #解析操作顺序,并写入到数据库保存

                    try:
                        h_time = line.split(';')[0].split(':')[1].strip()
                        h_user_index = line.split(';')[0].split(':')[2]
                        handle = line.split(';')[1]
                        print(h_time, h_user_index, handle)
                        userhandle = UserHandle( h_time=datetime.datetime.fromtimestamp(eval(h_time)), 
                                    h_user_index=eval(h_user_index), 
                                    handle=handle, 
                                    h_index=i,
                                    h_user_login=user.pk
                                )
                        userhandle.save()
                        i += 1
                        
                    except:
                        pass
                    else:
                        line = fp.readline()
            os.remove(new_path)
        else:
            create_handle_log(new_path)
    # return data 

if __name__ == "__main__":
    create_handle_log('history')

