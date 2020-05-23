from random import choice
names = ['段子杰', '王星霖', '王韵哲', '陈锦泽', '谢荣华']
times = ['昨天晚上', '昨天早上', '昨天中午', '昨天下午', '昨天黎明', '昨天半夜', '昨天傍晚', '昨天上午']
places = ['厕所','卧室','大街上','楼顶','下水道','教室','客厅','宿舍','衣柜里','棺材里','马桶上']
actions = ['吃','拉','喝','玩','睡','打','扔','干']
objs = ['狗','鸡巴','屎','尿','鞋','脚']
while True:
	input('--------------------')
	print("{}{}{}{}{}".format(choice(names),choice(times),choice(places),choice(actions),choice(objs)))
