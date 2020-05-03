with open('C://Users//pc//Desktop//python资料//lecture 5//toefl100.txt','r',encoding='utf-8') as file:
	content = file.read()

#分割
punc_list = ['.',',','?','[',']',"\'",'-','—','!','\"','\n','’']
for punc in punc_list:
	content = content.replace(punc,' ')
words_list = content.split(' ')
lword_list = [ word.lower() for word in words_list]
word_set = set(lword_list)
cnt_dict = {}
#筛词
for word in word_set:
	if word.isalpha() and len(word)>=5:
		cnt_dict[word] = lword_list.count(word)
wdcnttuplist = []
for k in sorted(cnt_dict,key=cnt_dict.__getitem__,reverse=True):
	wdcnttuplist.append((k,cnt_dict[k]))

#写入进excel
from openpyxl import load_workbook
work_book = load_workbook(filename='C://Users//pc//Desktop//python资料//lecture 5//sample.xlsx')
work_sheet = work_book['Sheet1']
row_num = 0
for word in wdcnttuplist:
	row_num += 1
	work_sheet['A'+str(row_num)] = word[0]
	work_sheet['B'+str(row_num)] = word[1]

work_book.save(filename='C://Users//pc//Desktop//python资料//lecture 5//sample.xlsx') 	

'''
#词云图
import pyecharts as pec
from pyecharts.charts import WordCloud
wordcloud = WordCloud()
wordcloud = WordCloud()
wordcloud.add("", wdcnttuplist, word_size_range=[20, 100])
wordcloud.render()
'''