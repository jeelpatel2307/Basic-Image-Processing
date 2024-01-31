from PIL import Image, ImageFilter

def apply_image_processing(input_path, output_path):
    """
    Open an image, apply basic processing, and save the result.

    Args:
    - input_path (str): Path to the input image file.
    - output_path (str): Path to save the processed image.
    """
    # Open the image
    original_image = Image.open(input_path)

    # Apply a basic filter (blurring)
    processed_image = original_image.filter(ImageFilter.BLUR)

    # Save the processed image
    processed_image.save(output_path)

if __name__ == "__main__":
    # Example: Apply basic image processing to "input.jpg" and save the result as "output.jpg"
    apply_image_processing("input.jpg", "output.jpg")
