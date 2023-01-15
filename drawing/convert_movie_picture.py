import cv2
import os
import shutil
import math

start_sec=2.3
stop_sec=2.32

def main():
    make_directory('./picture')
    directory = '../capture/capture'
    print(sum(os.path.isfile(os.path.join(directory,name)) for name in os.listdir(directory)))

    ID=0
    for filename in os.listdir(directory):
        print(filename)
        file = os.path.join(directory, filename)
        if os.path.isfile(file) and filename.endswith('.mp4'):
            print(file)
            save_frame_range(file, start_sec, stop_sec, ID)
            #save_frame_range_bara(file, filename)
            ID=ID+1


def save_frame_range(video_dir, start_sec, stop_sec, ID):
    cap = cv2.VideoCapture(video_dir)
    if not cap.isOpened():
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    print('{:.08f}'.format(fps))
    print(" - FPS: " + str(round(fps)))

    totalframecount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    start_frame=int(math.floor(start_sec*fps))
    stop_frame=int(math.ceil(stop_sec*fps))

    print(totalframecount)
    print(" - second range: " + str(start_sec) + "-" + str(stop_sec) + "sec")
    print(" - Frame number: " + str(start_frame) + "-" + str(stop_frame))

    for n in range(start_frame, stop_frame):
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        frame_sec='{:.02f}'.format(n/fps)
        if ret:
            cv2.imwrite('{}_{}_{}_{}sec.{}'.format('picture/picture', ID,n,frame_sec, 'jpg'), frame)
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
  