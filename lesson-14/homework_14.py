import numpy as np
from PIL import Image

# ============================================================
# Task 1: Fahrenheit to Celsius using numpy.vectorize
# ============================================================

def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9

fahrenheit = np.array([32, 68, 100, 212, 77])
vec_f_to_c = np.vectorize(fahrenheit_to_celsius)
celsius = vec_f_to_c(fahrenheit)

print("Task 1 - Celsius temperatures:")
print(celsius)
print()


# ============================================================
# Task 2: Power calculation using numpy.vectorize
# ============================================================

def power_func(x, p):
    return x ** p

numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

vec_power = np.vectorize(power_func)
power_results = vec_power(numbers, powers)

print("Task 2 - Power results:")
print(power_results)
print()


# ============================================================
# Task 3: Solve system of linear equations (x, y, z)
# ============================================================

A1 = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

B1 = np.array([7, 4, 5])

solution_xyz = np.linalg.solve(A1, B1)

print("Task 3 - Solution for x, y, z:")
print("x =", solution_xyz[0], "y =", solution_xyz[1], "z =", solution_xyz[2])
print()


# ============================================================
# Task 4: Electrical circuit currents (I1, I2, I3)
# ============================================================

A2 = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

B2 = np.array([12, -5, 15])

currents = np.linalg.solve(A2, B2)

print("Task 4 - Currents I1, I2, I3:")
print("I1 =", currents[0], "I2 =", currents[1], "I3 =", currents[2])
print()


# ============================================================
# Image Manipulation with NumPy + PIL
# ============================================================

def flip_image(img_array):
    flip_lr = np.fliplr(img_array)
    flip_ud = np.flipud(img_array)
    return flip_lr, flip_ud


def add_noise(img_array, noise_level=30):
    noise = np.random.randint(
        -noise_level, noise_level + 1, img_array.shape, dtype=np.int16
    )
    noisy_img = img_array.astype(np.int16) + noise
    return np.clip(noisy_img, 0, 255).astype(np.uint8)


def brighten_channels(img_array, channel=0, value=40):
    brightened = img_array.copy().astype(np.int16)
    brightened[:, :, channel] += value
    return np.clip(brightened, 0, 255).astype(np.uint8)


def apply_mask(img_array, mask_size=100):
    h, w, _ = img_array.shape
    start_y = h // 2 - mask_size // 2
    start_x = w // 2 - mask_size // 2

    masked_img = img_array.copy()
    masked_img[start_y:start_y + mask_size,
               start_x:start_x + mask_size] = [0, 0, 0]

    return masked_img


# Load image using PIL
img = Image.open("images/birds.jpg")
img_array = np.array(img)

# Perform image operations
flip_lr, flip_ud = flip_image(img_array)
noisy_img = add_noise(img_array)
bright_red_img = brighten_channels(img_array, channel=0, value=40)
masked_img = apply_mask(img_array)

# Save results using PIL
Image.fromarray(flip_lr).save("birds_flip_horizontal.jpg")
Image.fromarray(flip_ud).save("birds_flip_vertical.jpg")
Image.fromarray(noisy_img).save("birds_noisy.jpg")
Image.fromarray(bright_red_img).save("birds_bright_red.jpg")
Image.fromarray(masked_img).save("birds_masked.jpg")

print("Image processing completed. Output images saved.")
