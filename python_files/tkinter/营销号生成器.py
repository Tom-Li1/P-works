import tkinter as Tkinter
import os

# 创建窗口对象 设置初始化属性
window = Tkinter.Tk()
window.title("营销号文案生成器")
window.geometry("380x320")

# 创建所需的标签对象 以便提示用户应输入的内容
topicLabel = Tkinter.Label(window, text = '主题：', font = ('微软雅黑', 14))
eventLabel = Tkinter.Label(window, text = '事件：', font = ('微软雅黑', 14))
explanationLabel = Tkinter.Label(window, text = '解释：', font = ('微软雅黑', 14))

# 创建所需的输入框对象 以便获取用户的输入
topicEntry = Tkinter.Entry()
eventEntry = Tkinter.Entry()
explanationEntry = Tkinter.Entry()

# 声明一个字典用来储存关键词语
keyWords = {}

def getEssay(keyWords):
	return "{topic}{event}是怎么回事呢？{topic}相信大家都很熟悉，但是{topic}{event}是怎么回事呢，下面就让小编带大家一起了解吧。\r\n\
{topic}{event}，其实就是{explanation}，大家可能会很惊讶{topic}怎么会{event}呢？但事实就是这样，小编也感到非常惊讶。\r\n\
这就是关于{topic}{event}的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！".format(**keyWords)

def getInputAndOutput():
	# 获取用户输入并添加至关键词字典中并打印出来 与按钮关联
	keyWords['topic'] = topicEntry.get()
	keyWords['event'] = eventEntry.get()
	keyWords['explanation'] = explanationEntry.get()
	# 迭代一次关键词字典 确保不为空
	for keyWord in keyWords.values():
		if keyWord == '':
			print('输入框中的内容不能为空', '\n')
			return None
	print(getEssay(keyWords), '\n')

def clearOutput():
	# 用于清空命令行终端输出 随后补充被清空的标题
	os.system('cls')
	print('\n{:^100}\n'.format('文案输出区域'))

# 创建按钮对象 点击获取输入 生成文案并打印
createButton = Tkinter.Button(window, text = '生成文案', command = getInputAndOutput, font = ('微软雅黑', 10), width = 10)
clearButton = Tkinter.Button(window, text = '清空输出', command = clearOutput, font = ('微软雅黑', 10), width = 10)

# 使用表格布局放置各组件对象于Tkinter对象上
topicLabel.grid(row = 0, column = 0, padx = 20, pady = 20)
topicEntry.grid(row = 0, column = 2, padx = 20, pady = 20)
eventLabel.grid(row = 1, column = 0, padx = 20, pady = 20)
eventEntry.grid(row = 1, column = 2, padx = 20, pady = 20)
explanationLabel.grid(row = 2, column = 0, padx = 20, pady = 20)
explanationEntry.grid(row = 2, column = 2, padx = 20, pady = 20)
createButton.grid(row = 3, column = 0, padx = 20, pady = 20)
clearButton.grid(row = 3, column = 2, padx = 20, pady = 20)

# 打印标题于终端命令行居中位置
print('\n{:^100}\n'.format('文案输出区域'))

# 进入窗口循环
window.mainloop()