import os
import cv2
import numpy as np
"""
这个代码仅仅是把标签图像进行了膨胀，然后后面是自己手动的复制train_set和test_set，用刚刚膨胀的图片进行的替换，
这是在三折文件夹下来做的不同膨胀度的图片数据集
"""
images_sample_folder = "E:/DATA/3_fold/fold_2/train_set/NG,positive/"
images = os.listdir(images_sample_folder)
images_folder = "E:/DATA/3_fold_xxx/fold_2/"
list_dilate_rate = [0, 5, 9, 13, 17]
for image in images:
    if image.endswith(".bmp"):
        image_path = os.path.join(images_sample_folder, image)
        img = cv2.imread(image_path)
        for rate in list_dilate_rate:
            kernel = np.ones((rate, rate), np.uint8)
            dilate_folder = "dilate_" + str(rate)
            dilate_image_rate = os.path.join(images_folder, dilate_folder)
            dilate_image = os.path.join(dilate_image_rate, image)
            if not os.path.exists(dilate_image_rate):
                os.makedirs(dilate_image_rate)
            image_dd = cv2.dilate(img, kernel, iterations=1)
            cv2.imwrite(dilate_image, image_dd)
