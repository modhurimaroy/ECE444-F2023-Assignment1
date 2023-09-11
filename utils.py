class Utils:
	
	def __init__(self):
		pass
	
	def reversed(self, n):
		
		if(n < 0):
			result = - int(str(n)[::-1])

		else:
			result = int(str(n)[::-1])
