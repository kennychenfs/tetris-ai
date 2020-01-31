from pieces import I,J,L,O,S,Z,T
from copy import deepcopy as dc
import random
from getkey import getkey, keys
num2block='tjzosli'
#the grid under is for user
'''
grid=[]
for x in range(22):
	grid.append([])
	for y in range(10):
		grid[-1].append(0)
'''
class board:
	def __init__(self):
		self.grid=[]
		for x in range(22):
			self.grid.append([])
			for y in range(10):
				self.grid[-1].append(0)
	#	self.drop_time=self.drop=drop_time
	#	self.do_time=self.do=do_time
		self.point=0
		self.block=None
		self.center=[0,5]
		self.drop_point=0
	def dump(self):
		print('----------------------')
		for x in range(20):
			print('|',end='')
			for y in range(10):
				if self.grid[x][y]==1:
					print('\033[48;2;255;255;255m  \x1b[0m',end='')
				elif self.grid[x][y]==2:
					print('\033[48;2;255;182;0m  \x1b[0m',end='')
				elif self.grid[x][y]==3:
					print('\033[48;2;255;0;0m  \x1b[0m',end='')
				else:
					print('  ',end='')
			print('|')
		print('----------------------')
	def move(self,move):#move is 0~3, which represents none,left,down,right
		if move:
			if move==1:index=self.block.get_l_blocks_index()
			elif move==2:index=self.block.get_d_blocks_index()
			elif move==3:index=self.block.get_r_blocks_index()
			ok=True
			for i in index:
				if move==1:tx=self.center[0]+i[0];ty=self.center[1]+i[1]-1#the place to detect is beside the edge(outside)
				if move==2:tx=self.center[0]+i[0]+1;ty=self.center[1]+i[1]
				if move==3:tx=selfcenter[0]+i[0];ty=self.center[1]+i[1]+1
				if tx<20 and tx>-3 and ty>-1 and ty<10 and self.grid[tx][ty]:
					ok=False
					break
				if tx>=20 or tx<-2 or ty<0 or ty>=10:
					ok=False
					break
			if ok:
				if move==1:self.center[1]-=1
				if move==2:
					self.center[0]+=1
					self.drop_point+=1
					if self.drop_point==16:self.drop_point=10
				if move==3:center[1]+=1
			else:
				if move==2:return False
		return True
	def rotate(self,move):#move 0=none,1=r,2=l
		if move:
			if move==1:self.block.turn_r()
			if move==2:self.block.turn_l()
			index=self.block.get_all_index()
			ok=True
			for i in index:
				tx=self.center[0]+i[0];ty=self.center[1]+i[1]
				if tx<20 and tx>-3 and ty>-1 and ty<10 and self.grid[tx][ty]:
					ok=False
					break
				if tx>=20 or tx<-2 or ty<0 or ty>=10:
					ok=False
					break
			if not ok:
				if move==1:self.block.turn_l()
				if move==2:self.block.turn_r()
	def new_block(self):
		b=random.randint(1,224)
		if b<=33:self.block=T()
		elif b<=65:self.block=J()
		elif b<=97:self.block=Z()
		elif b<=129:self.block=O()
		elif b<=162:self.block=S()
		elif b<=193:self.block=L()
		elif b<=224:self.block=I()
	def end_drop(self):
		clean=0
		pre=[]
		for x in range(21,-1,-1):
			toclean=1
			for y in range(10):
				if not self.grid[x][y]:
					toclean=0
			if not toclean:
				pre.append(dc(self.grid[x]))
		while len(pre)<22:
			pre.append([0,0,0,0,0,0,0,0,0,0])
			clean+=1
		for i in range(22):
			self.grid[i]=dc(pre[21-i])
		self.point+=[0,400,1000,3000,12000][clean]
		self.point+=self.drop_point
	def drop_init(self):
		self.center=[0,5]
	#	self.do=self.do_time;self.drop-self.drop_time
	def get_now_grid(self):
		g=dc(self.grid)
		index=self.block.get_all_index()
		for x,y in index:
			tx=self.center[0]+x;ty=self.center[1]+y
			g[tx][ty]=self.block.color
		return g
	def drop(self):#drop one step
		index=self.block.get_d_blocks_index()
		for x,y in index:
			tx=self.center[0]+x+1;ty=self.center[1]+y
			if tx<20 and tx>-3 and ty>-1 and ty<10 and self.grid[tx][ty]:return False
			if tx>=20 or tx<-2 or ty<0 or ty>=10:return False
		self.center[0]+=1
		return True
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
b=board()
drop_time=6
do_time=6
while 1:
	drop=drop_time
	do=do_time
	b.drop_init()
	b.new_block()
	while 1:
		m=min(do,drop)
		do-=m;drop-=m
		dump(b.get_now_grid())
		if not do:
			do=do_time
			a=input('move(asd)?')
			try:print('\''+str({'a':1,'s':2,'d':3}[a])+'\'')
			except:pass
			try:c=b.move({'a':1,'s':2,'d':3}[a])
			except:c=b.move(0)
			if not c:
				break
			a=input('rotate(kl)?')
			try:b.rotate({'k':1,'l':2}[a])
			except:b.rotate(0)
		if not drop:
			drop=drop_time
			if not b.drop():
				break
	b.end_drop()
	b.grid=b.get_now_grid()
'''
drop_max=6
do_max=6
point=0
while 1:#a drop-to-end
	drop_point=0
	center=[0,5]
	b=random.randint(1,224)
	if b<=33:block=T()
	elif b<=65:block=J()
	elif b<=97:block=Z()
	elif b<=129:block=O()
	elif b<=162:block=S()
	elif b<=193:block=L()
	elif b<=224:block=I()
	index=block.get_all_index()
	end=False
	for i in index:
		tx=center[0]+i[0];ty=center[1]+i[1]
		if grid[tx][ty]:print('ended');end=True;break
	if end:
		dump(grid)
		break
	drop=drop_max
	do=do_max
	while 1:#a move
		a=min(drop,do)
		drop-=a;do-=a
		down=block.get_d_blocks_index()
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
	result=block.get_all_index()
	xtocheck=[]
	for i in result:
		grid[center[0]+i[0]][center[1]+i[1]]=block.color
	newx=19
	lines=0
	new_grid=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
	for x in range(19,-1,-1):
		toclean=1
		for y in range(10):
			if not grid[x][y]:
				toclean=0;break
		if not toclean:
			new_grid[newx]=dc(grid[x])
			newx-=1
		else:
			lines += 1
	if lines > 0:
		grid=dc(new_grid)
	point+=[0,400,1000,3000,12000][lines]
	point+=drop_point
'''
