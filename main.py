"""Main program."""

import cv2

from common.obj_detection.aruco_detectors.cv2 import Cv2Detector
from common.obj_detection.vision_capture import VisionCapture
from common.utils.fps_counter import FPSTracker
from common.utils.log import get_logger

logger = get_logger(__name__)


if __name__ == "__main__":
    vision_capture: VisionCapture = VisionCapture()
    detector: Cv2Detector = Cv2Detector()
    fps_tracker: FPSTracker = FPSTracker()

    # start vision capture
    vision_capture.start()

    while True:
        # get frame from the video capture
        frame = vision_capture.read()

        if frame is not None:
            # detect aruco
            corners, ids, _ = detector.detect(frame, True)

            # draw detected markers
            detector.draw_detections(frame, corners, ids)

            # update fps tracker
            fps_tracker.update()
            fps_tracker.put_fps_on_frame(frame)

            # show video frame
            cv2.imshow("Video Capture", frame)

        # exit loop when the "q" key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            logger.info("Exiting gracefully.")
            break

    # clean up
    logger.info("Shutting down video capture.")
    vision_capture.stop()
    cv2.destroyAllWindows()