import cv2
import os
 
# Specify the path to your grayscale image dataset
grayscale_folder = 'R:\cnn_test\lc_test\Benign'

# Specify the output folder for the RGB images
output_folder = 'R:\cnn_test\lc_test\BenignRGB'
os.makedirs(output_folder, exist_ok=True)

# Function to convert a single grayscale image to RGB
def convert_to_rgb(input_path, output_path):
    # Read the grayscale image
    grayscale_img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Convert to three-channel RGB
    rgb_img = cv2.cvtColor(grayscale_img, cv2.COLOR_GRAY2RGB)

    # Save the RGB image
    cv2.imwrite(output_path, rgb_img)

# Iterate through all grayscale images in the folder and convert to RGB
for filename in os.listdir(grayscale_folder):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        input_path = os.path.join(grayscale_folder, filename)
        output_path = os.path.join(output_folder, filename)
        convert_to_rgb(input_path, output_path)
