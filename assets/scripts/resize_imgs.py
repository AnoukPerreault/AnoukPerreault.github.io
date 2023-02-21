import cv2
import os


base_dir = "assets/imgs"
for dir in os.listdir(base_dir):
    sub_dir = os.path.join(base_dir, dir)
    if not os.path.isdir(sub_dir):
        continue
    for img_name in os.listdir(sub_dir):
        if not (img_name[-3:] != ".jpg" or img_name[-3:] != ".JPG" or img_name[-3:] != ".png"):
            continue
        
        img_path =os.path.join(sub_dir, img_name)
        img = cv2.imread(img_path)

        height, width, channel = img.shape
        
        downsample_ratio = max(height, width) / 1000

        resized_img = cv2.resize(img, (int(width/downsample_ratio), int(height/downsample_ratio)) )

        cv2.imwrite(img_path, resized_img)
        