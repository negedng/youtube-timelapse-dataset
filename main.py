from frame_extractor import FrameExtractor
import json
import argparse


def run(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)

    print('Download ', data['name'])
    need_download = data['data']
    
    while(len(need_download)>0):
        video_info = need_download.pop()
        try:
            fe = FrameExtractor(video_info)
            fe.extract_frames()
        except:
            print("Load unsuccessful, trying later")
            need_download.append(video_info)
        


if __name__ == "__main__":
    desc = 'Youtube Timelapse Dataset collector.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--data', default='ytld25.json')
    args = parser.parse_args()
    run(args.data)
