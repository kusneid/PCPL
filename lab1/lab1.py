#lab1, ооп
from sys import stdin

class Solution:
	def __init__(self):
		pass

class OneRoot(Solution):
	def __init__(self, x):
		self.root = x
	def RootPrint(self):
		print(f'one root {self.root}')
	
class NoRoots(Solution):
	def RootPrint(self):
		print('no roots')
	
class TwoRoots(Solution):
	def __init__(self, x1, x2):
		self.root1 = x1
		self.root2 = x2
	def RootPrint(self):
		print(f'two roots {self.root1}; {self.root2}')
	

def Solve(a,b,c) -> Solution:
	d = b**2 - 4*a*c
	if d<0:
		ans = NoRoots()
	elif d==0:
		ans = OneRoot(-b/2/a)
	else:
		ans = TwoRoots((-b+ d**0.5)/2/a,(-b- d**0.5)/2/a)
	return ans

def main():
	a = []
	for i in stdin:
			a.append(int(i))
			if len(a)>=3:
				break

	ans = Solve(a[0],a[1],a[2])
	ans.RootPrint()
if __name__ == "__main__":
	main()
