"""Main program."""

import cv2
from types import SimpleNamespace

from common.fps_counter import FPSTracker
from common.detectors.detector import Detector
from common.detectors.detector_manager import DetectorManager
from common.utils.json_utils import read_json
from common.utils.log import get_logger
from common.video_capture import VideoCapture

logger = get_logger(__name__)


class AutoUav:
    """Main autonomous UAV class.

    Attr:
        conf: App configurations
        video_capture: Video capture class that provides frames for object detection
        detector: Target identifier/detector
        fps_tracker: Tracks the fps of image processing
    """

    def __init__(self, conf: SimpleNamespace) -> None:
        """Constructor for AutoUav.

        Args:
            conf: App configuration
        """
        self.conf = conf
        self.video_capture: VideoCapture = VideoCapture(conf.video)
        self.detector: Detector = DetectorManager(conf.detector).get_detector()
        self.fps_tracker: FPSTracker = FPSTracker()

    def clean_up(self) -> None:
        """Cleanup for AutoUav."""
        logger.info("Cleaning up")
        self.video_capture.stop()
        cv2.destroyAllWindows()

    def run(self) -> None:
        """Runs the main logic."""
        logger.info("AutoUav starting up...")
        self.video_capture.start()

        while True:
            # get frame from the video capture
            frame = self.video_capture.read()

            if frame is not None:
                # detect aruco
                corners, ids, _ = self.detector.detect(frame, True)

                # After detection, we will translate into commands that can be sent to the PIXHAWK
                # TODO: Implement CameraCoordinateTransformer, FieldCoordinateMapper,
                # CommandGenerator

                # update fps tracker
                self.fps_tracker.update()
                self.fps_tracker.put_fps_on_frame(frame)

                # show video frame
                if self.conf.video.show_video:
                    self.detector.draw_detections(frame, corners, ids)
                    cv2.imshow("Video Capture", frame)

            # exit loop when the "q" key is pressed on the window
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.clean_up()
        logger.info("Shutting down gracefully")


if __name__ == "__main__":
    config: SimpleNamespace = read_json("config.json")

    auto_uav = AutoUav(config)
    auto_uav.run()
