import json
from types import SimpleNamespace
from typing import Union

from common.utils.log import get_logger

logger = get_logger(__name__)


def read_json(file_path: str, to_dict: bool = False) -> Union[SimpleNamespace, dict]:
    """Extracts JSON content from a file.
    
    Args:
        file_path: The file path to the JSON
        to_dict: To extract as a dict object or not

    Returns: The JSON data in SimpleNamespace or dict object format depending on the to_dict flag
    """
    logger.debug(f"Extracting JSON from {file_path}")
    data = json.loads(file_path, object_hook=lambda d: SimpleNamespace(**d) if to_dict else None)
    return data
