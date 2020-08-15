from frame_extractor import FrameExtractor
import json
import argparse


def run(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)

    print('Download ', data['name'])

    for video_info in data['data']:
        fe = FrameExtractor(video_info)
        fe.extract_frames()


if __name__ == "__main__":
    desc = 'Youtube Timelapse Dataset collector.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('data', default='ytld25.json')
    args = parser.parse_args()
    run(args.data)
