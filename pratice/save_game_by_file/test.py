# -*- coding:utf-8 -*-
#!/usr/bin/python
from random import randint

#输入玩家的名字
name = raw_input('请输入你的名字：')

#打开文件之后保存每个分数段
f = open("E:\personal\pratice\save_game_by_file\game.txt")
lines = f.readlines()
f.close()

#将文件中的每人对应的分数存储到字典中，
#并查询玩家的分数有无在字典中，没有赋值0
scores = {}
for line in lines:
	s = line.split()
	scores[s[0]] = s[1:]
score = scores.get(name)
if score is None:
	score = [0,0,0]


game_times = int (score[0])
min_times = int (score[1])
total_times = int (score[2])

#计算游戏的平均轮数
if game_times > 0:
	avg_times = float(total_times/game_times)
else:
	avg_times = 0

#输出成绩信息
print '你已经玩了%d次,最少%d论猜出答案,平均%.2f轮猜出答案' % (game_times,min_times,avg_times)

#随机输入一个数，并判断
num = randint(1,100)
times = 0 
flag = False
while flag == False:
	times += 1
	count = input('随机输入一个数：')
	if count < num:
		print 'too small'
	elif count > num:
		print 'too big'
	else:
		flag = True

#统计数目到文件中
if game_times == 0 or times<min_times :
	min_times = times
game_times += 1
total_times += times
#result = ("%d %d %d"%(game_times,min_times,total_times))

#将玩家的信息写到字典中
scores[name] = [str(game_times),str(min_times),str(total_times)]

#开始将信息一个个重新写回行，初始化一个空字符
result = ''
for n in scores:
#信息拼接
	line = n + '' + ''.join(scores[n]) + '\n'
	result += line

f = open("E:\personal\pratice\save_game_by_file\game.txt",'w')
f.write(result)
f.close()

