#用于读取电子表格xlsx文件并存入二维列表

import xlrd

def excelReader(path):
	#打开指定目录的xlsx文件
	xlsxfile = xlrd.open_workbook(path)
	#打开第一个工作表
	sheet = xlsxfile.sheet_by_name(xlsxfile.sheet_names()[0])
	# 获取行数和列数
	rownum = sheet.nrows #总行数
	clonum = sheet.ncols #总列数

	allcontents = [] #创建一个用来存储所有内同的列表
	for r in range(rownum):
		rowcontent = [] #选定一行

		for c in range(clonum):
			rowcontent.append(sheet.cell(r, c).value) #遍历次y轴上所有内容并添加到列表

		allcontents.append(rowcontent) #将添加完毕的列表加入到存储所有内容的列表中

	return allcontents

path = input("拖入文件>>>")
path = path.strip('"').replace('\\', '/')
xlsx = excelReader(path)
print('\n', xlsx, '\n')
while True:
	x = input('X>>>')
	y = input('Y>>>')
	print(xlsx[int(x)][int(y)], '\n')