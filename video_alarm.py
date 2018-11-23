import sys
from threading import Thread
from src.video_capturing import VideoCapturing
from src.wait_user import wait_user_input


def print_help_and_exit():
    print("**********************************")
    print("********** ALARM SYSTEM **********")
    print("**********************************", end='\n\n')
    print('python3 video_alarm.py -t [threshold] -c [alarm_check]', end='\n\n')
    print('-h | --help:\t to see this help message')
    print('-t [threshold]: value between 10 and 100 that define the sensibility of the alarm system, '
          'lower the value higher the sensibility (default: 50)')
    print('-c [alarm_check]: min value of danger pixel to trigger the alarm (default: 50)')
    exit(1)


def get_arguments_value(argv):
    defaults = {
        'threshold': 50,
        'alarm_check': 50
    }
    if len(argv) > 1:
        if argv[1] == '-h' or argv[1] == '--help':
            return print_help_and_exit()

        for i, arg in enumerate(argv):
            if arg == '-t' and len(argv) > i + 1:
                defaults['threshold'] = int(argv[i + 1])
                if defaults['threshold'] < 10 or defaults['threshold'] > 100:
                    defaults['threshold'] = 50
            if arg == '-c' and len(argv) > i + 1:
                defaults['alarm_check'] = int(argv[i + 1])

    return defaults


def main(argv):
    arguments = get_arguments_value(argv)
    video_capturing = VideoCapturing(threshold=arguments['threshold'])
    user_thread = Thread(target=lambda: wait_user_input(video_capturing, arguments))
    user_thread.start()
    video_capturing.init_camera()


if __name__ == '__main__':
    main(sys.argv)
