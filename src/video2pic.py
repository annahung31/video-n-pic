import os
import cv2
print(cv2.__version__)
import glob
import argparse

class Video_processor(object):
    def video2pic(self):
        vidcap = cv2.VideoCapture('../input/test.mp4')
        success,image = vidcap.read()

        count = 0
        success = True
        while success:
            cv2.imwrite("../output/frame%d.jpg" % count, image)     # save frame as JPEG file
            success,image = vidcap.read()
            print ('Read a new frame: ', success)
            count += 1

        vidcap.release()



    def save_video(self, pics_dir, WIDTH, HEIGHT, fps):
        
        # vidcap = cv2.VideoCapture('../input/test2.mp4')
        fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
        # size = (int(vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)), 
        # int(vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        size = (WIDTH, HEIGHT)
        out = cv2.VideoWriter('../output/output.avi', fourcc, fps, size)
        pics = sorted(glob.glob(os.path.join(pics_dir, '*.jpg'))

        for frame in pics:
            frame = cv2.imread(frame)
            out.write(frame)
            
        cv2.destroyAllWindows()




def build_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('--job', type=str,
                    help='v2p: Turn video into a sequence of pictures; p2v: Turn a sequence of pictures into a video.', default='v2p')

    #arguments for v2p
    parser.add_argument('--video_name', type=str,
                    help='The video to be processed. if you want to process p2v, please ignore this.', default=None)

    #arguments for p2v
    parser.add_argument('--pics_dir', type=int,
                    help='The pictures folder', default='./input/')
    parser.add_argument('--WIDTH', type=int,
                    help='The width of input pictures', default=None)

    parser.add_argument('--HEIGHT', type=int,
                    help='The HEIGHT of input pictures', default=None)

    parser.add_argument('--fps', type=int,
                    help='frame per second', default=120)


    return parser



if __name__ == '__main__':
    parser = build_parser()
    args= parser.parse_args()
    VP = Video_processor()
    if args.job == 'v2p':
        VP.video2pic(args.video_name)
    elif args.job == 'p2v':
        VP.save_video(args.pics_dir, args.WIDTH, args.HEIGHT)
    else:
        print('{} is an undefined job, please choose "v2p" or "p2v".'.format(args.job))