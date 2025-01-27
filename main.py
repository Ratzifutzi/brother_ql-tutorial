from brother_ql.raster import BrotherQLRaster
from brother_ql.backends.helpers import send
from brother_ql.conversion import convert
from brother_ql import BrotherQLError
from PIL import Image

# Printer settings
printer_model = 'QL-820NWB'
printer_connection = 'tcp://169.254.72.185'  # Replace with your printer's IP address
label_type = '62'

# Load the image
image_path = r'C:\Users\ratzi\Documents\Development\Python\BrotherQL\tempQR.png'  # Replace with your image path
image = Image.open(image_path)

# Create a raster object
qlr = BrotherQLRaster(printer_model)

# Convert the image to label instructions
instructions = convert(
    qlr=qlr,
    images=[image],
    label=label_type,
    rotate='auto',
    threshold=70.0,
    dither=False,
    compress=True,
    red=False,
    dpi_600=False,
    hq=True,
    cut=True
)

# Print the label
try:
    send(instructions, printer_connection)
    print("Label printed successfully!")
except BrotherQLError as e:
    print(f"Error printing label: {e}")
