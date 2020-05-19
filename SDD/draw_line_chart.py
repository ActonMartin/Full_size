import os
import matplotlib.pyplot as plt
import numpy as np
'''
这个代码的作用是绘制分类折线图
'''


class DrawLineChart():
	def __init__(self, fold:str, learn_rate:str, ng, ok, ng_list:list, ok_list:list):
		self.fold = fold
		self.learn_rate = learn_rate
		self.ng = ng # 真实的NG数量
		self.ok = ok # 真实的OK数量
		self.ng_list = ng_list
		self.ok_list = ok_list
		self.dilate = [0, 5, 9, 13, 17]

	def drawpillar(self):
		# plt.figure(figsize=(6.4, 4.8), dpi=300)
		fig, ax = plt.subplots(figsize=(6.4, 4.8), dpi=300)
		y_ticks = np.arange(0, 140, 10)

		rects1 = plt.plot(self.dilate,self.ng_list,color="blue",linewidth=2,linestyle=':',label='NG', marker='*')
		rects1 = plt.plot(self.dilate,self.ok_list,color="green",linewidth=2,linestyle=':',label='OK', marker='*')
		rects1 = plt.plot(self.dilate,self.ng,color="black",linewidth=2,linestyle='-',label='real NG', marker='.')
		rects1 = plt.plot(self.dilate,self.ok,color="black",linewidth=2,linestyle='-',label='real OK', marker='.')

		plt.xlabel('dilate', fontsize=20)
		plt.ylabel('images', fontsize=20)
		plt.title('fold_' + self.fold + '_learn_rate_' + self.learn_rate, fontsize=20)
		plt.xticks(self.dilate, ('0', '5', '9', '13', '17'), fontsize=16)

		plt.yticks(y_ticks, fontsize=16)
		plt.ylim(0, 140)
		plt.legend(fontsize=12, framealpha=0.8, frameon=True)

		plt.tight_layout()
		img_name = 'fold_' + self.fold + '_learn_rate_' + self.learn_rate + '.svg'
		img = plt.savefig(img_name)
		# plt.show()
		return img


if __name__ == "__main__":
	ng_list_fold_0 = [18.4, 19, 20, 18.8, 19]
	ok_list_fold_0 = [116.6, 116, 115, 116.2, 116]
	ng_list_fold_1 = [17.4, 17, 16.8, 17, 15.2]
	ok_list_fold_1 = [118.6, 119, 119.2, 119, 120.8]
	ng_list_fold_2 = [14.4, 14.6, 14.6, 14.8, 14.4]
	ok_list_fold_2 = [113.6, 113.4, 113.4, 113.2, 113.6]
	DrawLineChart('0', '0.01', [18]*5, [117]*5, ng_list_fold_0, ok_list_fold_0).drawpillar()
	DrawLineChart('1', '0.01', [18]*5, [118]*5, ng_list_fold_1, ok_list_fold_1).drawpillar()
	DrawLineChart('2', '0.01', [16]*5, [112]*5, ng_list_fold_2, ok_list_fold_2).drawpillar()

	ng_list_fold_0_2 = [19.8, 20.2, 19.8, 19.4, 18.4]
	ok_list_fold_0_2 = [115.2, 114.8, 115.2, 115.6, 117.8]
	ng_list_fold_1_2 = [17, 17, 17, 17, 17.2]
	ok_list_fold_1_2 = [119, 119, 119, 119, 118.8]
	ng_list_fold_2_2 = [15, 15, 14.6, 14.4, 12.2]
	ok_list_fold_2_2 = [113.2, 113, 113.4, 113.6, 115.8]
	DrawLineChart('0', '0.1', [18] * 5, [117] * 5, ng_list_fold_0_2, ok_list_fold_0_2).drawpillar()
	DrawLineChart('1', '0.1', [18] * 5, [118] * 5, ng_list_fold_1_2, ok_list_fold_1_2).drawpillar()
	DrawLineChart('2', '0.1', [16] * 5, [112] * 5, ng_list_fold_2_2, ok_list_fold_2_2).drawpillar()

	ng_list_fold_0_3 = [135, 101.25, 135, 30.25, 116]
	ok_list_fold_0_3 = [0, 33.75, 0, 104.75, 19]
	ng_list_fold_1_3 = [124.8, 135, 94.6, 62.4, 61.4]
	ok_list_fold_1_3 = [11.2, 1, 41.4, 73.6, 74.6]
	ng_list_fold_2_3 = [81.6, 79.2, 73.6, 128, 79.4]
	ok_list_fold_2_3 = [46.4, 48.8, 54.4, 0, 48.6]
	DrawLineChart('0', '0.5', [18] * 5, [117] * 5, ng_list_fold_0_3, ok_list_fold_0_3).drawpillar()
	DrawLineChart('1', '0.5', [18] * 5, [118] * 5, ng_list_fold_1_3, ok_list_fold_1_3).drawpillar()
	DrawLineChart('2', '0.5', [16] * 5, [112] * 5, ng_list_fold_2_3, ok_list_fold_2_3).drawpillar()

	ng_list_fold_0_4 = [111, 111.4, 135, 135, 134.4]
	ok_list_fold_0_4 = [24, 23.6, 0, 0, 0.6]
	ng_list_fold_1_4 = [108.8, 81.6, 86, 91.6, 136]
	ok_list_fold_1_4 = [27.2, 54.4, 50, 44.4, 0]
	ng_list_fold_2_4 = [128, 128, 128, 105.4, 128]
	ok_list_fold_2_4 = [0, 0, 0, 22.6, 0]
	DrawLineChart('0', '1', [18] * 5, [117] * 5, ng_list_fold_0_4, ok_list_fold_0_4).drawpillar()
	DrawLineChart('1', '1', [18] * 5, [118] * 5, ng_list_fold_1_4, ok_list_fold_1_4).drawpillar()
	DrawLineChart('2', '1', [16] * 5, [112] * 5, ng_list_fold_2_4, ok_list_fold_2_4).drawpillar()
