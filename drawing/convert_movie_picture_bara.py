import cv2
import os
import shutil
import math

# Input frames at fracture in order of camera ID
fracture_frame=[1066,1059,1067,1074,1069,1068,1568,1496,1527,1510,2820,2821,2819,200,3782,200,3772,2821,2819,3775]

def main():
    make_directory('./picture')
    directory = '../capture/capture'
    print(sum(os.path.isfile(os.path.join(directory,name)) for name in os.listdir(directory)))

    for num in range(1,20):
        make_directory('./frame_' + str(num))

    ID=0
    for filename in os.listdir(directory):
        print(filename)
        file = os.path.join(directory, filename)
        if os.path.isfile(file) and filename.endswith('.mp4'):
            print(file)
            save_frame_range_bara(file, filename)
            ID=ID+1


def save_frame_range_bara(video_dir, filename):

    file_num=filename[6]
    if(int_check(filename[7])):
        file_num=file_num+filename[7]
    
    cap = cv2.VideoCapture(video_dir)
    if not cap.isOpened():
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    print(" - FPS: " + '{:.05f}'.format(fps))

    totalframecount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print("total: " + str(totalframecount))

    start_frame=fracture_frame[int(file_num)-1]-10
    stop_frame=fracture_frame[int(file_num)-1]+10
    #start_frame=totalframecount-1
    #stop_frame=totalframecount
    print(" - Frame number: " + str(start_frame) + "-" + str(stop_frame))

    for n in range(start_frame, stop_frame):
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        ID=n-start_frame
        if ret:
            cv2.imwrite('{}_{}_{}.{}'.format('frame_' + str(ID) + '/camera', file_num, ID, 'jpg'), frame)
        else:
            return


def make_directory(dir):
    print("create a directory, " + str(dir))
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)

def int_check(check_num):
    try:
        int(check_num)
    except ValueError:
        return False
    else:
        return True
                 
if __name__ == '__main__':
   main()
  