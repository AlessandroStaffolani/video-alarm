import cv2
import numpy as np
import logging
logging.basicConfig(filename='alarm.log', format='%(asctime)s - %(message)s', datefmt='%d-%m-%y %H:%M:%S', level=logging.INFO)


DANGER = 255
SAFE = 0


def calculate_difference(previous, current, threshold):
    if previous is not None:
        image = current.copy()
        difference = np.abs(previous.astype(float) - current.astype(float))
        white_pixels = difference > threshold
        black_pixels = difference <= threshold
        image[white_pixels] = DANGER
        image[black_pixels] = SAFE

        return image.astype(np.uint8)
    else:
        return None


class VideoCapturing:

    def __init__(self, camera_index=0, threshold=50, alarm_check=50):
        self.camera_index = camera_index
        self.threshold = threshold
        self.alarm_check = alarm_check
        self.monitoring = False
        self.alarm_fired = False

    def init_camera(self):
        cap = cv2.VideoCapture(self.camera_index)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print('Capturing with ' + str(w) + ' x ' + str(h) + ' resolution')
        previous_frame = None
        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                current = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                cv2.imshow('frame', current)
                # Check if we need to applay the kernel to the captured images

                image_difference = calculate_difference(previous_frame, current, self.threshold)
                if image_difference is not None:
                    cv2.imshow('frame difference', image_difference)
                    if self.monitoring:
                        self.difference_checker(image_difference)

                previous_frame = current.copy()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def start_monitoring(self):
        print("Starting monitoring")
        self.monitoring = True

    def difference_checker(self, image_difference):
        num_white = image_difference[image_difference == DANGER].shape[0]
        print('Actual current pixel number: ' + str(num_white))
        if num_white > self.alarm_check and not self.alarm_fired:
            # ALARM!!
            print('ALARM!!!')
            logging.info('ALARM!!!')
