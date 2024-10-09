"""This module stores the different detectors that are available to use.

This will later be used when we make the detector we use configurable using a config file.
"""

from enum import Enum

from common.obj_detection.aruco_detectors.cv2 import Cv2Detector
from common.obj_detection.aruco_detectors.yolov3_tiny import YoloDetector


class AvailableDetectors(Enum):
    """This class encapsulates the available detectors.
    
    Attributes:
        CV2: OpenCV's built in arUco detector
        YOLO: YoloV3Tiny arUco detector
    """
    CV2: Cv2Detector = Cv2Detector
    YOLO: YoloDetector = YoloDetector
