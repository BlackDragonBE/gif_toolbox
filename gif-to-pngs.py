from PIL import Image, ImageSequence
import sys, os

def extract_frames(gif_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the GIF file
    with Image.open(gif_path) as gif:
        # Iterate over each frame in the GIF
        for i, frame in enumerate(ImageSequence.Iterator(gif)):
            # Save each frame as a PNG file
            frame.save(os.path.join(output_folder, f"frame_{i:03d}.png"), "PNG")

if __name__ == "__main__":  
    if len(sys.argv) != 3:
        print("Usage: gif-to-pngs.py <gif> <png folder>")
        exit()
    gif_path = sys.argv[1]
    output_folder = sys.argv[2]

    # Extract frames from the GIF
    extract_frames(gif_path, output_folder)
