import cv2
import os

# 1. Load and resize to 256×256
image_path = './assets/images/deadpool.jpg'
img = cv2.imread(image_path)
img = cv2.resize(img, (256, 256))
canvas = img.copy()

# Extract image name for output files
image_name = os.path.splitext(os.path.basename(image_path))[0]

# 2. This list will collect your clicked points
points = []

# 3. Mouse‐callback: on each left‐click, record & draw
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        # draw a little circle
        cv2.circle(canvas, (x, y), 4, (0, 0, 255), -1)
        # if we have at least two points, draw a line from previous
        if len(points) > 1:
            cv2.line(canvas, points[-2], points[-1], (0, 255, 0), 2)
        cv2.imshow('trajectory', canvas)
        print(f"Point: x={x}, y={y}")

# 4. Show the window and bind the callback
cv2.imshow('trajectory', canvas)
cv2.setMouseCallback('trajectory', on_mouse)

# 5. Press any key to finish
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Save your drawn image and the x,y list only
cv2.imwrite(f'./my_trajs/{image_name}_256_with_trajectory.png', canvas)
with open(f'./my_trajs/trajectory_coords_{image_name}.txt', 'w') as f:
    for x, y in points:
        f.write(f"{x},{y}\n")
