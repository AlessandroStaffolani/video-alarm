# Video Alarm
Simple python project that use your camera as a video alarm system.
It is implemented using OpenCv and applaying the two frame difference algorithm.

### Installation
To install this script you should install OpenCv python version on your device and then you need to clone this project
```
git clone https://github.com/ale8193/video-alarm.git
``` 

### Run
To run this script is very simple, you need to do as follow:
```
cd video-alarm
python video_alarm.py 
```

You can change two parameters adding these arguments:
* `-t [threshold]` value between 10 and 100 that define the sensibility of the alarm system, lower the value higher the sensibility (default: 50)
* `-c [alarm_check]` min value of danger pixel to trigger the alarm (default: 50)