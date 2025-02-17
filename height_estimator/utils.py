import cv2

def find_contours(edges):
    """Finds and returns sorted contours from an edge-detected image."""
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sort contours by area (largest first)
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]
    
    return sorted_contours

def get_reference_height(contours):
    """Extracts the pixel height of the reference and target objects."""
    ref_contour = contours[0]  # Reference object
    target_contour = contours[1]  # Target object

    ref_height_px = cv2.boundingRect(ref_contour)[3]  # Height of reference in pixels
    target_height_px = cv2.boundingRect(target_contour)[3]  # Height of target in pixels

    return ref_height_px, target_height_px
