from PIL import Image

# Load the image
image_path = input("Enter Your Image Path.\n If the image is within the same Folder Then just type the name of the image.:")  # Ensure the image is in the same folder as the script
image = Image.open(image_path)

# Convert the image to RGBA if not already
if image.mode != "RGBA":
    image = image.convert("RGBA")

# Process to remove white background
datas = image.getdata()
new_data = []
for item in datas:
    if item[0] > 200 and item[1] > 200 and item[2] > 200:  # Threshold for white
        new_data.append((255, 255, 255, 0))  # Transparent
    else:
        new_data.append(item)

# Apply the updated data
image.putdata(new_data)

# Save the new image
image.save("image_transparent.png", "PNG")
