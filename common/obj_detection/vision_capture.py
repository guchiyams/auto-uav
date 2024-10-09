import cv2
import numpy
import queue
import threading
from typing import Union

from common.utils.log import get_logger

logger = get_logger(__name__)


class VisionCapture:
    """Wrapper for the cv2.VideoCapture.
    
    This class implements a video capture in a separate thread. This allows the object detection
    to not be blocked by the video capture process, thus improving performance.
    """
    def __init__(self, src: int = 0, width: int = 640, height: int = 480, buffer_size: int = 6) -> None:
        """Initialized VisionCaptureThreaded.
        
        Args:
            src: Camera source index
            width: Video feed width
            height: Video feed height
            buffer_size: Frame buffer size

        Raises:
            RunTimeError: Failed to initialize Video Capture
        """
        self.video_cap: cv2.VideoCapture = cv2.VideoCapture(src)

        if self.video_cap is None or not self.video_cap.isOpened():
            raise RuntimeError("Failed to initialize Video Capture. Try a different index.")
        
        self.video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.frame_buffer: queue.Queue = queue.Queue(maxsize=buffer_size)
        self.stop_event: threading.Event = threading.Event()

    def start(self) -> None:
        """Starts the video capture thread."""
        logger.info("Starting video capture thread")
        self.capture_thread = threading.Thread(target=self._capture_frames)
        self.capture_thread.start()

    def _capture_frames(self) -> None:
        """Capture frames from the camera and put it in the buffer."""
        while not self.stop_event.is_set():
            # ret: bool, frame: numpy.ndarray
            ret, frame =self.video_cap.read()
            if not ret:
                break
            # only populate to frame buffer if there is available space
            if not self.frame_buffer.full():
                self.frame_buffer.put(frame)
        self.video_cap.release()

    def stop(self) -> None:
        """Stop the video capture thread."""
        self.stop_event.set()
        self.capture_thread.join()

    def read(self) -> Union[numpy.ndarray, None]:
        """Read a frame from the frame_buffer (not from the VideoCapture).
        
        Returns: A numpy.ndarray representing a frame or None if frame buffer is empty
        """
        if not self.frame_buffer.empty():
            return self.frame_buffer.get()
        return None
    