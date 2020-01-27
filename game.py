from pieces import I,J,L,O,S,Z,T
from copy import deepcopy as dc
import random
from getkey import getkey, keys
grid=[]
for x in range(22):			#save as:
	grid.append([])			#-2
	for y in range(10):		#-1
		grid[-1].append(0)	#0
print(grid)					#1
							#...
							#19
def dump(grid):
	print('----------------------')
	for x in range(20):
		print('|',end='')
		for y in range(10):
			if grid[x][y]==1:
				print('\033[48;2;255;255;255m  \x1b[0m',end='')
			elif grid[x][y]==2:
				print('\033[48;2;255;182;0m  \x1b[0m',end='')
			elif grid[x][y]==3:
				print('\033[48;2;255;0;0m  \x1b[0m',end='')
			else:
				print('  ',end='')
		print('|')
	print('----------------------')
num2block='tjzosli'
drop_max=6
do_max=6
point=0
while 1:#a drop-to-end
	drop_point=0
	center=[0,5]
	b=num2block[random.randint(0,6)]
	clean_num=0
	if b=='t':block=T()
	if b=='j':block=J()
	if b=='z':block=Z()
	if b=='o':block=O()
	if b=='s':block=S()
	if b=='l':block=L()
	if b=='i':block=I()
	index=block.get_d_blocks_index()
	for tx,ty in index:
		if grid[tx][ty]:break
	drop=drop_max
	do=do_max
	while 1:#a move
		a=min(drop,do)
		drop-=a;do-=a
		down=block.get_d_blocks_index()
		if not drop:#can drop
			drop=drop_max
			ok=True
			for i in down:
				tx=center[0]+i[0]+1;ty=center[1]+i[1]
				if tx<20 and tx>-3 and ty>-1 and ty<10 and grid[tx][ty]:ok=False;break
				if tx>=20 or tx<-2 or ty<0 or ty>=10:ok=False;break
			if ok:
				center[0]+=1
			else:break
		if not do:#can do
			g=dc(grid)
			result=block.get_all_index()
			for i in result:
				g[center[0]+i[0]][center[1]+i[1]]=block.color
			dump(g)
			do=do_max
			print(center,point)
			a=getkey()
			if a in 'asd':
				if a=='a':index=block.get_l_blocks_index();play=True
				elif a=='s':index=block.get_d_blocks_index();play=True
				elif a=='d':index=block.get_r_blocks_index();play=True
				ok=True
				if play:
					for i in index:
						if a=='a':tx=center[0]+i[0];ty=center[1]+i[1]-1#the place to detect is beside the edge(outside)
						if a=='s':tx=center[0]+i[0]+1;ty=center[1]+i[1]
						if a=='d':tx=center[0]+i[0];ty=center[1]+i[1]+1
						print(tx,ty)
						if tx<20 and tx>-3 and ty>-1 and ty<10 and grid[tx][ty]:
							ok=False
							break
						if tx>=20 or tx<-2 or ty<0 or ty>=10:
							ok=False
							break
					print(index)
					print(ok)
					if ok:
						if a=='a':center[1]-=1
						if a=='s':
							center[0]+=1
							drop_point+=1
							if drop_point==16:drop_point=10
						if a=='d':center[1]+=1
					else:
						if a=='s':break
			#rotate
			elif a in 'kl':
				if a=='k':block.turn_r()
				if a=='l':block.turn_l()
				index=block.get_all_index()
				ok=True
				for i in index:
					tx=center[0]+i[0];ty=center[1]+i[1]
					if tx<20 and tx>-3 and ty>-1 and ty<10 and grid[tx][ty]:
						ok=False
						break
					if tx>=20 or tx<-2 or ty<0 or ty>=10:
						ok=False
						break
				if not ok:
					if a=='k':block.turn_l()
					if a=='l':block.turn_r()
	result=block.get_all_index()
	for i in result:
		grid[center[0]+i[0]][center[1]+i[1]]=block.color
	toclean=1
	pre=[]
	clean=0
	for x in range(21,-1,-1):
		toclean=1
		for y in range(10):
			if not grid[x][y]:
				toclean=0
		if not toclean:
			pre.append(dc(grid[x]))
	while len(pre)<22:
		pre.append([0,0,0,0,0,0,0,0,0,0])
		clean+=1
	for i in range(22):
		grid[i]=dc(pre[21-i])
	point+=[0,400,1000,3000,12000][clean]
	point+=drop_point
