from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Open the 512x512 Lena image
peppers_image = Image.open("/content/drive/My Drive/Colab Notebooks/cryptosystem/peppers.tiff")
peppers_image_256 = peppers_image.resize((256, 256))

# Save or use the 256x256 Lena image
peppers_image_256.save("/content/drive/My Drive/Colab Notebooks/cryptosystem/peppers_256x256.tiff")
peppers_image_256.show()

# Load the Lena image
image_path = '/content/drive/My Drive/Colab Notebooks/cryptosystem/peppers_256x256.tiff'
image = cv2.imread(image_path)

# Ensure the image is in RGB format
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Function to check if two numbers are coprime using the Euclidean algorithm
def is_coprime(a, b):
    while b:
        a, b = b, a % b
    return a == 1

# Define keys for each channel
a1, b1 = 5, 20  # Keys for R channel
a2, b2 = 7, 30  # Keys for G channel
a3, b3 = 11, 15  # Keys for B channel

# Check if the 'a' keys are coprime with 256
if not (is_coprime(a1, 256) and is_coprime(a2, 256) and is_coprime(a3, 256)):
    raise ValueError("One or more 'a' keys are not coprime with 256. Please select different keys.")

# Function to scramble pixel positions
def affine_scramble_positions(image, a, b):
    height, width = image.shape[:2]
    scrambled_image = np.zeros_like(image)
    for x in range(height):
        for y in range(width):
            new_x = (a * x + b) % height
            new_y = (a * y + b) % width
            scrambled_image[new_x, new_y] = image[x, y]
    return scrambled_image

# Scramble pixel positions for each channel
R_channel = image[:, :, 0]
G_channel = image[:, :, 1]
B_channel = image[:, :, 2]

R_scrambled = affine_scramble_positions(R_channel, a1, b1)
G_scrambled = affine_scramble_positions(G_channel, a2, b2)
B_scrambled = affine_scramble_positions(B_channel, a3, b3)

# Combine scrambled channels
scrambled_image = cv2.merge((R_scrambled, G_scrambled, B_scrambled))

# Show the original image and its histogram
plt.figure(figsize=(9, 7))
plt.subplot(2, 2, 1)
plt.title('Original Görüntü')
plt.imshow(image)
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Histogram-Original Görüntü')
plt.hist(image[:, :, 0].ravel(), bins=256, color='red', alpha=0.5, label='Red')
plt.hist(image[:, :, 1].ravel(), bins=256, color='green', alpha=0.5, label='Green')
plt.hist(image[:, :, 2].ravel(), bins=256, color='blue', alpha=0.5, label='Blue')
plt.xlim([0, 256])
plt.legend()

# Show the scrambled image and its histogram
plt.subplot(2, 2, 3)
plt.title('Piksel Konumlarını Değiştirme Görüntü')
plt.imshow(scrambled_image)
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Histogram- Piksel Konumlarını Değiştirme Görüntü')
plt.hist(scrambled_image[:, :, 0].ravel(), bins=256, color='red', alpha=0.5, label='Red')
plt.hist(scrambled_image[:, :, 1].ravel(), bins=256, color='green', alpha=0.5, label='Green')
plt.hist(scrambled_image[:, :, 2].ravel(), bins=256, color='blue', alpha=0.5, label='Blue')
plt.xlim([0, 256])
plt.legend()

plt.tight_layout()
plt.show()

# Save the scrambled image
#cv2.imwrite('/content/drive/My Drive/Colab Notebooks/cryptosystem/scrambled_lena.png', cv2.cvtColor(scrambled_image, cv2.COLOR_RGB2BGR))
