from rembg import remove
from PIL import Image

input_path = 'src/images/main banner doctor.png'
output_path = 'src/images/main_banner_doctor_no_bg.png'

print(f"Loading {input_path}...")
input_img = Image.open(input_path)

print("Removing background...")
output_img = remove(input_img)

print("Cropping to content...")
bbox = output_img.getbbox()
if bbox:
    output_img = output_img.crop(bbox)

print(f"Saving to {output_path}...")
output_img.save(output_path)
print("Done!")
