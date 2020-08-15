from pytube import YouTube
import math
import cv2
import os


class FrameExtractor():
    '''
    Class used for extracting frames from a video file.
    '''
    def __init__(self,
                 data):
        self.url = data['url']
        video = YouTube(self.url)
        print('Start downloading...')
        video_path = video.streams.get_by_itag(data['itag']).download()

        self.video_path = video_path
        self.vid_cap = cv2.VideoCapture(video_path)
        self.n_frames = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.vid_cap.get(cv2.CAP_PROP_FPS))

        self.start_frame = data['start_frame']
        self.end_frame = data['end_frame']
        if self.end_frame == -1:
            self.end_frame = self.n_frames
        self.every_x_frame = data['every_x_frame']
        self.img_name = data['img_name']
        self.dest_path = data['dest_path']
        self.crop = data['crop']

    def get_video_duration(self):
        duration = self.n_frames/self.fps
        print(f'Duration: {datetime.timedelta(seconds=duration)}')

    def get_n_images(self, every_x_frame):
        n_img = math.floor(self.n_frames / every_x_frame) + 1
        return n_img

    def extract_frames(self, img_ext='.jpg'):

        if not self.vid_cap.isOpened():
            self.vid_cap = cv2.VideoCapture(self.video_path)

        if self.dest_path is None:
            self.dest_path = os.getcwd()
        else:
            if not os.path.isdir(self.dest_path):
                os.makedirs(self.dest_path)
                print(f'Created the following directory: {self.dest_path}')

        frame_cnt = 0

        while self.vid_cap.isOpened():

            success, image = self.vid_cap.read()

            if not success:
                break

            if frame_cnt >= self.end_frame:
                break

            is_included = frame_cnt % self.every_x_frame == 0

            if (frame_cnt >= self.start_frame) and is_included:
                img_name = ''.join([self.img_name, '_',
                                    str(frame_cnt), img_ext])
                img_path = os.path.join(self.dest_path, img_name)
                if self.crop is not None:
                    x1, y1, x2, y2 = self.crop
                    image = image[x1:x2, y1:y2]
                cv2.imwrite(img_path, image)

            frame_cnt += 1

        self.vid_cap.release()
        cv2.destroyAllWindows()
