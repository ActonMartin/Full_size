import os
import cv2
import numpy as np
import shutil
"""
v2代码实现逻辑：先将每折文件夹下面的train_set和test_set分别复制到不同膨胀率的文件夹下面，就地进行膨胀。

v1代码实现逻辑：这个代码仅仅是把标签图像进行了膨胀，然后后面是自己手动的复制train_set和test_set，用刚刚膨胀的图片进行的替换，
这是在三折文件夹下来做的不同膨胀率的图片数据集
"""
all_folder = "E:/DATA/3_fold_xxx/"
sub_folders = os.listdir(all_folder)
list_dilate_rate = [0, 5, 9, 13, 17]

for sub_sub_folder in sub_folders:
	sub_sub_folder_path =os.path.join(all_folder, sub_sub_folder)

	sub_sub_train_set = os.path.join(sub_sub_folder_path,"train_set")
	sub_sub_test_set = os.path.join(sub_sub_folder_path,"test_set")

	for rate in list_dilate_rate:
		dilate_folder_name = "dilate_" + str(rate)
		dilate_folder = os.path.join(sub_sub_folder_path, dilate_folder_name)
		if not os.path.exists(dilate_folder):
			os.makedirs(dilate_folder)
		train_set_in_dilate = os.path.join(dilate_folder, "train_set")
		test_set_in_dilate = os.path.join(dilate_folder, "test_set")
		shutil.copytree(sub_sub_train_set, train_set_in_dilate)
		shutil.copytree(sub_sub_test_set, test_set_in_dilate)
		need_dilate_folder = dilate_folder + "/train_set/NG,positive/"
		print(need_dilate_folder)
		images = os.listdir(need_dilate_folder)
		for image in images:
			if image.endswith(".bmp"):
				kernel = np.ones((rate, rate), np.uint8)
				image_path = os.path.join(need_dilate_folder, image)
				img = cv2.imread(image_path)
				image_dd = cv2.dilate(img, kernel, iterations=1)
				cv2.imwrite(image_path, image_dd)
				print("{}已经膨胀完毕".format(image_path))
