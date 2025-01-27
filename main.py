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
    qlr=qlr,				# The BrotherQLRaster object created earlier
    images=[image],			# List of images to print (in this case, just one)
    label=label_type,		# The type of label being used (e.g., '62')
    rotate='auto',			# Rotation angle of the image. Use angles dividiable by 90 for better prints. 0-360
    threshold=70.0,			# Threshold for converting color images to black and white (0-255)
    dither=False,			# Whether to apply dithering to the image (False for no dithering)
    compress=True,			# Whether to compress the print data (True for compression)
    red=False,				# Whether to print in red (for printers supporting two-color printing)
    dpi_600=False,			# Whether to use 600 DPI printing (False for standard resolution)
    hq=True,				# Whether to use high-quality print mode. False for faster prints but lower quality.
    cut=True				# Whether to cut the label after printing
)


# Print the label
try:
    send(instructions, printer_connection)
    print("Label printed successfully!")
except BrotherQLError as e:
    print(f"Error printing label: {e}")
