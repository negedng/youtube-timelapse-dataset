# Youtube Timelapse Dataset
Dataset collection of static youtube timelapse video frames
## Requirements
Pip package `pytube3` with fix: `pip install git+https://gitlab.com/obuilds/public/pytube@ob-v1 --upgrade`
# Build dataset
```
pip install git+https://gitlab.com/obuilds/public/pytube@ob-v1 --upgrade    # install pytube3
git clone https://github.com/negedng/youtube-timelapse-dataset.git          # clone this repo
cd youtube-timelapse-dataset                                                # navigate to dir
python main.py                                                              # Build a dataset
```
## YTLD 25
Youtube Timelapse Dataset 25 contains image frames from 25 videos extracted from Youtube. The videos were cut to display a static camera recordings. Texts were crop from the images. Each video takes around 1-5 minutes.

Videos include daily and yearly changes of a forest, garden, parking lot and more. They contains various natural phenomenon like fog, storm, snow and fire.