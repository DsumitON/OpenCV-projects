#!/usr/bin/python3
import cv2
import numpy as np

# ---------- 1. Load image and prepare grayscale ----------
img = cv2.imread(r"/mnt/win/Users/Sumit/Documents/SKS_Drive/OPenCV/images/bottle.jpeg")
if img is None:
    raise FileNotFoundError("Image not found. Check the path!")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Optional: resize for easier display
h, w = gray.shape
max_width = 400
scale = max_width / w if w > max_width else 1.0
if scale != 1.0:
    gray = cv2.resize(gray, (int(w * scale), int(h * scale)))
    img = cv2.resize(img, (int(w * scale), int(h * scale)))

# ---------- 2. Sobel (reference baseline) ----------
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_mag = cv2.magnitude(sobelx, sobely)
sobel_mag = cv2.convertScaleAbs(sobel_mag)

# ---------- 3. Prewitt ----------
prewitt_kx = np.array([[-1, 0, 1],
                       [-1, 0, 1],
                       [-1, 0, 1]], dtype=np.float32)
prewitt_ky = np.array([[-1, -1, -1],
                       [ 0,  0,  0],
                       [ 1,  1,  1]], dtype=np.float32)

prewitt_x = cv2.filter2D(gray, cv2.CV_32F, prewitt_kx)
prewitt_y = cv2.filter2D(gray, cv2.CV_32F, prewitt_ky)
prewitt_mag = cv2.magnitude(prewitt_x, prewitt_y)
prewitt_mag = cv2.convertScaleAbs(prewitt_mag)

# ---------- 4. Roberts ----------
roberts_kx = np.array([[1, 0],
                       [0, -1]], dtype=np.float32)
roberts_ky = np.array([[0,  1],
                       [-1, 0]], dtype=np.float32)

roberts_x = cv2.filter2D(gray, cv2.CV_32F, roberts_kx)
roberts_y = cv2.filter2D(gray, cv2.CV_32F, roberts_ky)
roberts_mag = cv2.magnitude(roberts_x, roberts_y)
roberts_mag = cv2.convertScaleAbs(roberts_mag)

# ---------- 5. Scharr ----------
scharr_x = cv2.Scharr(gray, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(gray, cv2.CV_64F, 0, 1)
scharr_mag = cv2.magnitude(scharr_x, scharr_y)
scharr_mag = cv2.convertScaleAbs(scharr_mag)

# ---------- 6. Laplacian ----------
lap = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)
lap = cv2.convertScaleAbs(lap)

# ---------- 7. LoG (Gaussian + Laplacian) ----------
blur_log = cv2.GaussianBlur(gray, (5, 5), 1.0)
log = cv2.Laplacian(blur_log, cv2.CV_64F, ksize=3)
log = cv2.convertScaleAbs(log)

# ---------- 8. DoG (Difference of Gaussians) ----------
blur1 = cv2.GaussianBlur(gray, (5, 5), 1.0)
blur2 = cv2.GaussianBlur(gray, (5, 5), 2.0)
dog = cv2.subtract(blur1, blur2)
dog = cv2.convertScaleAbs(dog)

# ---------- 9. Canny ----------
canny = cv2.Canny(gray, 100, 200)

# ---------- 10. Prepare labels + stack ----------
def add_label(img_gray, text):
    """Add a small label at the top of a grayscale image."""
    out = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
    cv2.putText(out, text, (5, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),
                1, cv2.LINE_AA)
    return out

# Ensure all are same size
def resize_to_ref(src, ref):
    return cv2.resize(src, (ref.shape[1], ref.shape[0]))

ref = gray
images = [
    add_label(ref, "Gray"),
    add_label(resize_to_ref(sobel_mag, ref), "Sobel"),
    add_label(resize_to_ref(prewitt_mag, ref), "Prewitt"),
    add_label(resize_to_ref(roberts_mag, ref), "Roberts"),
    add_label(resize_to_ref(scharr_mag, ref), "Scharr"),
    add_label(resize_to_ref(lap, ref), "Laplacian"),
    add_label(resize_to_ref(log, ref), "LoG"),
    add_label(resize_to_ref(dog, ref), "DoG"),
    add_label(resize_to_ref(canny, ref), "Canny"),
]

# Arrange in grid: 3 x 3

row1 = np.hstack(images[0:3])
row2 = np.hstack(images[3:6])
row3 = np.hstack(images[6:9])
grid = np.vstack([row1, row2, row3])


cv2.imshow("Edge Detection Comparison", grid)
cv2.waitKey(0)
cv2.destroyAllWindows()

