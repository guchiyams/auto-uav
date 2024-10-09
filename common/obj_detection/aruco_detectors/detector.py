"""Abstract class for ArUco detectors."""

import numpy as np
from abc import ABC

class Detector(ABC):
    """This class serves as the abstract base class for all ArUco detectors."""
    def __init__(self) -> None:
        pass

    def detect(self, frame: np.ndarray, **kwargs) -> None:
        """Abstract method to detect arUco markers.
        
        Args:
            frame: np.ndarray representing a video frame
            kwargs: additional args
        """
        pass

    def draw_detectors(self, frame: np.ndarray, **kwargs) -> None:
        """Abstract method to draw the detection bounding boxes.
        
        Args:
            frame: np.ndarray representing a video frame
            kwargs: additional args
        """
        pass
