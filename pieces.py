from copy import deepcopy as dc
ESC_BG="\x1b[48;5;"
ESC="\x1b[38;5;"
ESC_END="m"
RESET="\x1b[0m"
class piece:
	def __init__(self,rotate_grids,color,lenofturns=4):
	#	self.grid=grid
		self.grid=rotate_grids[0]
		self.rotate=0
		self.rotate_grids=rotate_grids
		self.color=color
		self.turns=lenofturns
	def turn_r(self):
		self.rotate+=1
		if self.rotate==self.turns:self.rotate=0
		self.update_rotate()
	def turn_l(self):
		self.rotate-=1
		if self.rotate==-1:self.rotate=self.turns-1
		self.update_rotate()
	def update_rotate(self):
		print('rotate:',self.rotate)
		self.grid=dc(self.rotate_grids[self.rotate])
	def get_r_blocks_index(self):
		blocks=[]
		for x in range(5):
			for y in range(4,-1,-1):
				if self.grid[x][y]:
					blocks.append([x-2,y-2])
					break
		return blocks
	def get_l_blocks_index(self):
		blocks=[]
		for x in range(5):
			for y in range(5):
				if self.grid[x][y]:
					blocks.append([x-2,y-2])
					break
		return blocks
	def get_d_blocks_index(self):
		blocks=[]
		for y in range(5):
			for x in range(4,-1,-1):
				if self.grid[x][y]:
					blocks.append([x-2,y-2])
					break
		return blocks
	def get_all_index(self):
		blocks=[]
		for y in range(5):
			for x in range(5):
				if self.grid[x][y]:
					blocks.append([x-2,y-2])
		return blocks
	'''for test
	def dump(self):
		a='  '
		for i in range(5):
			for j in range(5):
				if (i,j)==(2,2):
					a=' .'
				else:
					a='  '
				if self.grid[i][j]:
					print('\033[48;2;'+self.color[0]+';'+self.color[1]+';'+self.color[2]+'m'+a+RESET,end='')
				else:
					print(a,end='')
			print()
		print('----------')
	'''
class I(piece):
	def __init__(self):
		i=[
			[[0,0,0,0,0],
			[0,0,0,0,0],
			[1,1,1,1,0],
			[0,0,0,0,0],
			[0,0,0,0,0]],
			[[0,0,1,0,0],
			[0,0,1,0,0],
			[0,0,1,0,0],
			[0,0,1,0,0],
			[0,0,0,0,0]]]
		super().__init__(i,color=1,lenofturns=2)
class O(piece):
	def __init__(self):
		i=[
			[[0,0,0,0,0],
			[0,0,0,0,0],
			[0,1,1,0,0],
			[0,1,1,0,0],
			[0,0,0,0,0]]]
		super().__init__(i,color=1,lenofturns=1)
	def turn_r(self):
		pass
	def turn_l(self):
		pass
	def update_rotate(self):
		pass
class S(piece):
	def __init__(self):
		i=[
			[[0,0,0,0,0],
			[0,0,0,0,0],
			[0,0,1,1,0],
			[0,1,1,0,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,0,1,0,0],
			[0,0,1,1,0],
			[0,0,0,1,0],
			[0,0,0,0,0]]]
		super().__init__(i,color=3,lenofturns=2)
class Z(piece):
	def __init__(self):
		i=[
			[[0,0,0,0,0],
			[0,0,0,0,0],
			[0,1,1,0,0],
			[0,0,1,1,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,0,0,1,0],
			[0,0,1,1,0],
			[0,0,1,0,0],
			[0,0,0,0,0]]]
		super().__init__(i,color=2,lenofturns=2)
class T(piece):
	def __init__(self):
		i=[
			[[0,0,0,0,0],
			[0,0,0,0,0],
			[0,1,1,1,0],
			[0,0,1,0,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,0,1,0,0],
			[0,1,1,0,0],
			[0,0,1,0,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,0,1,0,0],
			[0,1,1,1,0],
			[0,0,0,0,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,0,1,0,0],
			[0,0,1,1,0],
			[0,0,1,0,0],
			[0,0,0,0,0]]]
		super().__init__(i,color=1,lenofturns=4)
class L(piece):
	def __init__(self):
		i=[
			[[0,0,0,0,0],
			[0,0,0,0,0],
			[0,1,1,1,0],
			[0,1,0,0,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,1,1,0,0],
			[0,0,1,0,0],
			[0,0,1,0,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,0,0,1,0],
			[0,1,1,1,0],
			[0,0,0,0,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,0,1,0,0],
			[0,0,1,0,0],
			[0,0,1,1,0],
			[0,0,0,0,0]]]
		super().__init__(i,color=2,lenofturns=4)
class J(piece):
	def __init__(self):
		i=[
			[[0,0,0,0,0],
			[0,0,0,0,0],
			[0,1,1,1,0],
			[0,0,0,1,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,0,1,0,0],
			[0,0,1,0,0],
			[0,1,1,0,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,1,0,0,0],
			[0,1,1,1,0],
			[0,0,0,0,0],
			[0,0,0,0,0]],
			[[0,0,0,0,0],
			[0,0,1,1,0],
			[0,0,1,0,0],
			[0,0,1,0,0],
			[0,0,0,0,0]]]
		super().__init__(i,color=3,lenofturns=4)
