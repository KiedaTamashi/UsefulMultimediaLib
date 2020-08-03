from EssentialPack import *

def TransferFiles(input_dir,output_dir,suffix):
    '''
    Transfer files with SPECIFIC suffix from one dictionary to another.
    :param input_dir: Origin dictionary
    :param output_dir: Target dictionary
    :param suffix: suffix like '.avi', '.jpg'
    :return:
    '''
    files = os.listdir(input_dir)
    cnt=0
    for file in files:
        if file.endswith(suffix):
            shutil.move(os.path.join(input_dir,file),os.path.join(output_dir,file))
            cnt+=1
    print(cnt)






# TransferFiles('a','b','.jpg')