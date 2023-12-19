from PIL import Image, ImageSequence
import sys, os


def extract_frames(webp_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the WebP file
    with Image.open(webp_path) as webp:
        # Save the entire animation as a sequence of PNG files
        for i, frame in enumerate(ImageSequence.Iterator(webp)):
            frame.save(os.path.join(output_folder, f"frame_{i:03d}.png"), "PNG")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: webp-to-pngs.py <webp> <png folder>")
        exit()
    webp_path = sys.argv[1]
    output_folder = sys.argv[2]

    # Extract frames from the WebP animation
    extract_frames(webp_path, output_folder)
