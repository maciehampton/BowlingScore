#Looking at each time the bowling ball is thrown and the results
MAX_PINS = 10
class Round:
	
	def __init__(self, pins):
		self.score = pins
		self.strike = False
		
		#force the data to be in the correct range
		if (pins > MAX_PINS):
			pins = MAX_PINS
		if ( pins < 0 ):
			pins = 0
		
		#Check for a strike
		if (pins == MAX_PINS):
			self.strike = True
			
			
	def getScore(self):
		return self.score
		
		
	def isStrike(self):
		return self.strike
		
############# Testing ######################	
	
if (__name__ == "__main__"):
	strike = Round(10)
	lowScore = Round(0)
	highScore = Round(9)
	
	print("Correctly Identified Strike: " + str(strike.isStrike()))
	print("Correctly Identified Non-Strikes: " + str(not(lowScore.isStrike())  and not(highScore.isStrike())))
	