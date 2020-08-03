from EssentialPack import *

def extractFrames(ori_dir,map_dir,frame_base_dir,index_path,interval,start_num=0):
    '''
    :param ori_dir: .mp4
    :param map_dir: .avi
    :param interval: frame extraction maximum interval
    :param start_num: continue from last node.
    :return:
    '''
    x_frame_dir = os.path.join(frame_base_dir,"OriFrame")
    y_frame_dir = os.path.join(frame_base_dir,"MapFrame")
    if not os.path.exists(x_frame_dir):
        os.mkdir(x_frame_dir)
    if not os.path.exists(y_frame_dir):
        os.mkdir(y_frame_dir)

    ori_videoNames = os.listdir(ori_dir)
    map_videoNames = os.listdir(map_dir)
    ori_videoNames.sort(key=lambda x:int(x.split("_")[1]))
    file_pair_list = []
    cnt = 0
    random.seed(time.time())
    interval_new = random.randint(interval-2, interval+2)
    ban_list = ["Eren.avi","GTGoku.avi","RoseFreyja.avi","ifuleet.avi","inkling.avi",'luigi.avi',"Nikos.avi"]

    for mapVideoName in map_videoNames:
        flag = False
        video_2 = cv2.VideoCapture(os.path.join(map_dir,mapVideoName))
        for ban in ban_list:
            if mapVideoName.endswith(ban):
                flag=True
                break
        if flag:
            continue
        for oriVideoName in ori_videoNames:
            if not oriVideoName.startswith("_".join(mapVideoName.split("_")[0:3])):
                continue
            else:
                video_1 = cv2.VideoCapture(os.path.join(ori_dir, oriVideoName))
                frame_number = 0
                tick = 0
                while True:
                    ret1, img1 = video_1.read()
                    ret2, img2 = video_2.read()
                    if not ret1 or not ret2: break
                    if tick==interval_new:
                        print(mapVideoName + str(frame_number))
                        x_name = "x_" + str(mapVideoName.split("_")[-1])[:-4] + "_" + str(cnt)
                        y_name = "y_" + str(mapVideoName.split("_")[-1])[:-4] + "_" + str(cnt)  # TODO need check when actually use.
                        cv2.imwrite(os.path.join(x_frame_dir, x_name + '.jpg'), img1)
                        cv2.imwrite(os.path.join(y_frame_dir, y_name + '.jpg'), img2)
                        file_pair_list.append([x_name, y_name])
                        cnt += 1
                        random.seed(time.time())
                        interval_new = random.randint(interval - 2, interval + 2)
                        tick = 0
                    else:
                        tick += 1
                    frame_number += 1
                video_1.release()
        video_2.release()
    df = pd.DataFrame(file_pair_list)
    df.to_csv(index_path,index=None,header=None)