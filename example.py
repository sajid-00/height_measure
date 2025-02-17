import cv2
from height_estimator import measure_height

# Example usage
image_path = "test_images/person_with_reference.jpg"
reference_height_cm = 170  # Known reference height

estimated_height = measure_height(image_path, reference_height_cm)
print(f"Estimated Height: {estimated_height:.2f} cm")

# Display image
image = cv2.imread(image_path)
cv2.imshow("Measured Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
