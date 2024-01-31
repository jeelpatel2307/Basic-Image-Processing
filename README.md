# Basic Image Processing

This project demonstrates basic image processing in Python using the Pillow library. The script opens an image, applies a basic processing operation (blurring), and saves the result.

## How It Works

1. **Image Processing Function:**
    - The `apply_image_processing` function in `app.py` takes two parameters: `input_path` (path to the input image file) and `output_path` (path to save the processed image).
    - It opens the input image using the Pillow library (`Image.open`).
    - A basic image processing operation is applied using the `filter` method, specifically a blur filter (`ImageFilter.BLUR`).
    - The processed image is then saved to the specified output path.
2. **Example Usage:**
    - In the `__main__` block, an example is provided where the function is called with "input.jpg" as the input image and "output.jpg" as the output path.

## Usage

1. **Run the Script:**
    - Save the script in a file, for example, `app.py`.
    - Install the Pillow library using the following command:
        
        ```bash
        pip install Pillow
        
        ```
        
    - Replace "input.jpg" with the path to your input image file.
    - Run the script using a Python interpreter:
        
        ```bash
        python app.py
        
        ```
        
    - The script will apply basic image processing (blurring) to the input image and save the result as "output.jpg."
2. **Customization:**
    - Experiment with different image processing filters provided by Pillow's `ImageFilter` module.
    - Modify the `apply_image_processing` function to include additional processing steps or techniques.
    - Create a more interactive script or GUI to allow users to choose different images and processing options.

Feel free to explore and modify this project based on your specific image processing needs!

---

## Author

Jeel patel
