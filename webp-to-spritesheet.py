import sys
from PIL import Image


def get_frame_count(webp_path):
    try:
        with Image.open(webp_path) as img:
            frame_count = 1
            while True:
                try:
                    img.seek(frame_count)
                    frame_count += 1
                except EOFError:
                    break
            return frame_count - 1
    except Exception as e:
        print("Error:", e)
        return 0


def extract(webp, out, num_columns):
    with Image.open(webp) as im:
        width, height = im.width, im.height
        frame_nums = get_frame_count(webp)
        num_rows = (frame_nums + num_columns - 1) // num_columns
        new_width = width * num_columns
        new_height = height * num_rows
        new_image = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))

        for index, i in enumerate(range(frame_nums)):
            im.seek(im.n_frames * i // frame_nums)
            row = index // num_columns
            col = index % num_columns
            paste_x = col * width
            paste_y = row * height
            new_image.paste(im, (paste_x, paste_y))

        new_image.save(out)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: webp-to-spritesheet.py <webp> <png output> <num_columns>")
        exit()
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    columns = int(sys.argv[3])
    extract(in_file, out_file, columns)
