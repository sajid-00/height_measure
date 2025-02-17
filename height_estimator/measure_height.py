import cv2
import numpy as np
from .utils import find_contours, get_reference_height

def measure_height(image_path, reference_height_cm):
    """
    Measures the height of an object in an image using a reference object.

    :param image_path: Path to the image
    :param reference_height_cm: Known height of the reference object in cm
    :return: Estimated height of the detected object
    """
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect edges
    edges = cv2.Canny(gray, 50, 150)
    
    # Find contours
    contours = find_contours(edges)
    
    if len(contours) < 2:
        raise ValueError("Could not detect both reference and target object.")
    
    # Get reference and target object heights in pixels
    ref_height_px, target_height_px = get_reference_height(contours)
    
    # Convert pixel height to real-world height
    pixel_to_cm_ratio = reference_height_cm / ref_height_px
    estimated_height = target_height_px * pixel_to_cm_ratio

    return estimated_height
