class Utils:
	
	# def __init__(self):
	# 	pass
	
	def reversed(self, n):
		if isinstance(n, int):
			if(n < 0):
				result = - int(str(n)[::-1])

			else:
				result = int(str(n)[::-1])
		else:
			raise ValueError("Integer input required!")
		return result
	
	def formatter(self, n):
		if isinstance(n, int):
			binary = bin(n)
			octal = oct(n)
		
		else:
			raise ValueError("Integer input required!")
		
		return binary, octal
	
if __name__ == "__main__":
	utilsInstance = Utils()
	testNumber = 645
	result = utilsInstance.reversed(testNumber)
	binary, octal = utilsInstance.formatter(37)
	print("Reversed number: ", result)
	print("Binary number: ", binary)
	print("Octal number: ", octal)