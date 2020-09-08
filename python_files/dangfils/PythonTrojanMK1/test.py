import os, shutil, time, itertools
'''
def moveOrCopyFileOrDir(src_file_or_path, dst_file_or_path, operate_mode):
		# 若第二个参数为文件，复制source_file内容至此文件
		# 若为文件夹，复制source_file的内容至文件夹内的同名文件
		# 此方法强制使用绝对路径
		if os.path.exists(src_file_or_path) == False:
			# 源文件或目录不存在 错误代码08
			return ['ERROR_CODE', '08', None]

		if operate_mode == 'copy':
			# 复制文件或目录
			try:
				# 对不同类型的源采取针对性函数
				if os.path.isfile(src_file_or_path):
					shutil.copy(src_file_or_path, dst_file_or_path)
				elif os.path.isdir(src_file_or_path):
					shutil.copytree(src_file_or_path, dst_file_or_path)
			except Exception as e:
				# 复制文件或目录时发生的错误 错误代码09
				return ['ERROR_CODE', '09', str(e.__class__.__name__) + ' ' + str(e)]

		elif operate_mode == 'move':
			# 剪切文件或目录
			try:
				# move函数不讲究源的类型
				shutil.move(src_file_or_path, dst_file_or_path)
			except Exception as e:
				# 剪切文件或目录的错误 错误代码10
				return ['ERROR_CODE', '10', str(e.__class__.__name__) + ' ' + str(e)]

while True:
	md = input('MODE>>>')
	src = input('SRC>>>')
	dst = input('DST>>>')
	rt = moveOrCopyFileOrDir(src_file_or_path = src, dst_file_or_path = dst, operate_mode = md)
	if rt == None:
		input('Finished. \n')
	else:
		print('ERROR_CODE-' + rt[1])
		print(rt[2])
'''
PLAY_ANIMATION = False
def showAnimation(text):
	global PLAY_ANIMATION

	for icon in itertools.cycle('-\\|/'):
		if PLAY_ANIMATION:
			print('\r' + '[INFO]', text, icon, end='')
			time.sleep(0.2)
		else:
			break

showAnimation('Fucking...')