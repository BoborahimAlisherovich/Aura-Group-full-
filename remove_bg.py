from PIL import Image
import os

def remove_background(input_path, output_path):
    print(f"Opening {input_path}...")
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # If the pixel is white (or very close to white), make it transparent
        # Range 200-255 is usually enough to catch almost-white artifacts
        if item[0] > 220 and item[1] > 220 and item[2] > 220:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path, "PNG")
    print(f"Saved transparent image to {output_path}")

if __name__ == "__main__":
    base_dir = r"c:\Users\Anonymous\Desktop\AURA Group"
    input_file = os.path.join(base_dir, "static", "imgs", "logo_image", "tmpm29hi4hn.png")
    output_file = os.path.join(base_dir, "static", "imgs", "logo_image", "logo_transparent.png")
    remove_background(input_file, output_file)
