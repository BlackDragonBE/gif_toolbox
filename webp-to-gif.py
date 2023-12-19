from PIL import Image
import sys

def convert_webp_to_gif(input_path, output_path):
    try:
        # Open the WebP image
        webp_image = Image.open(input_path)
        # Convert to GIF and preserve animation
        webp_image.save(output_path, 'GIF', save_all=True)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: webp-to-gif.py <input.webp> <output.gif>")
        exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_webp_to_gif(input_file, output_file)
