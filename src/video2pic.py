import cv2
print(cv2.__version__)
import glob

class Video_processor(object):
    def video2pic(self):
        vidcap = cv2.VideoCapture('../input/test2.mp4')
        success,image = vidcap.read()

        count = 0
        success = True
        while success:
            cv2.imwrite("../output/frame%d.jpg" % count, image)     # save frame as JPEG file
            success,image = vidcap.read()
            print ('Read a new frame: ', success)
            count += 1
            if count == 200:
                success = False
        vidcap.release()



    def save_video(self):
        vidcap = cv2.VideoCapture('../input/test2.mp4')
        fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        size = (int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
        int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        out = cv2.VideoWriter('../output/output.avi', fourcc, 120.0, size)
        pics = sorted(glob.glob('../output/*.jpg'))

        for frame in pics:
            # 寫入影格
            frame = cv2.imread(frame)
            out.write(frame)
            
        cv2.destroyAllWindows()





if __name__ == '__main__':
    VP = Video_processor()
    VP.save_video()