from time import sleep


def wait_user_input(video_capturing, arguments):
    print("**********************************")
    print("********** ALARM SYSTEM **********")
    print("**********************************", end='\n\n')
    print("Current parameters:")
    print("\t- threshold: " + str(arguments['threshold']))
    print("\t- alarm_check: " + str(arguments['alarm_check']))
    print("(type -h or --help to see how to configure these parameters")
    sleep(2)
    print("\nSet the camera to the object to monitor before starting the alarm")
    print("(press 'q' on camera's window to quit the monitoring", end='\n\n')
    input("Press enter to start alarm monitoring")
    video_capturing.start_monitoring()
