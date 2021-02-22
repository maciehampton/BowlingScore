#The frame Class, can have multiple Rounds in a frame
#the frame knows when it is full (has all rounds possible) and when complete (has a final score for the frame)
import Round

MAX_PINS = 10

class Frame:

	def __init__(self, finalFrame = False):
		self.strike = False #does the frame contain a strike?
		self.spare = False #does the frame contain a spare?
		self.finalFrame = finalFrame #is this the final frame in the game?
		self.frameFull = False #does the frame have all the rounds needed?
		self.frameComplete = False #are all scoring and rounds completed?
		self.rawScore = 0 #score of the frame before any bonuses from strikes or spares are added
		self.finalScore = 0 #complete score of the frame (with bonuses)
		self.firstRound = None
		self.secondRound = None
		self.thirdRound = None #only possible if the last frame of the game has a strike or spare in it
		
		
	def addRound(self, newRound):
		if self.frameFull:
			#let the caller know if the frame is full (no more rounds can be added)
			return False
		elif (self.firstRound == None):
			self.addFirstRound(newRound)
		elif (self.secondRound == None):
			self.addSecondRound(newRound)
		else:
			self.addThirdRound(newRound)
	
	
	def addFirstRound(self, newRound):
		self.firstRound = newRound
		if (newRound.isStrike()):
			self.strike = True
			self.rawScore = MAX_PINS
			if not(self.finalFrame):
				#as long as it is not the final frame, a strike will complete the frame
				self.frameFull = True
	
	
	def addSecondRound(self, newRound):
		self.secondRound = newRound
		self.rawScore = self.getFirstRoundScore() + self.getSecondRoundScore()
		
		#the last frame rawScore could be greater than MAX_PINS if the first round was a strike
		if( self.rawScore >= MAX_PINS): 
			self.spare = True
			if( not self.finalFrame):
				self.frameFull = True
		else:
			self.finishScore()
			
			
	def addThirdRound(self, newRound):
		self.thirdRound = newRound
		self.finishScore(newRound.getScore())
	
	
	def finishScore(self, firstBonus = 0, secondBonus = 0):
		#add in any bonuses from strikes or spares, if none, just finalize the raw score and mark frame as complete
		self.finalScore = self.rawScore + firstBonus + secondBonus
		self.frameComplete = True
		self.frameFull = True
				
				
	def getFirstRoundScore(self):
		if (self.firstRound == None):
			return False
		return self.firstRound.getScore()
		
		
	def getSecondRoundScore(self):
		if (self.secondRound == None):
			return False
		return self.secondRound.getScore()
			
			
	def getThirdRoundScore(self):
		if (self.thirdRound == None):
			return False
		return self.thirdRound.getScore()			
				
				
	def isFull(self):
		return self.frameFull
		
		
	def isScored(self):
		return self.frameComplete
		
		
	def getScore(self):
		return self.finalScore
		
		
	def isStrike(self):
		return self.strike
		
		
	def isSpare(self):
		return self.spare

		
		
#################### Testing #############################

if (__name__ == "__main__"):
	strike = Frame()
	strikeRound = Round.Round(10)
	strike.addRound(strikeRound)
	answer = strike.isStrike() and (strike.getFirstRoundScore() == 10) and strike.isFull() and not(strike.isScored())
	print("Correctly made Strike: " + str(answer))
	
	answer = (strike.addRound(strikeRound) == False)
	print("Correctly refused to add round to completed frame: " + str(answer))
	
	strike.finishScore(10,10)
	answer = strike.isScored and (strike.getScore() == 30) 
	print("Correctly finished scoring Frame: " + str(answer))
	
	spare = Frame()
	spareRound = Round.Round(5)
	spare.addRound(spareRound)
	spare.addRound(spareRound)
	answer = spare.isSpare() and spare.isFull() and not spare.isScored()
	print("Correctly made spare: " + str(answer))
	
	spare.finishScore(10)
	answer = spare.isScored and (spare.getScore() == 20) and (spare.getFirstRoundScore() == 5) and (spare.getSecondRoundScore() == 5)
	print("Correctly scored spare frame: " + str(answer))
	
	finalFrame = Frame(True)
	finalFrame.addRound(strikeRound)
	answer = (finalFrame.addRound(strikeRound) != False)
	print("Correctly added more rounds on Final Round: " + str(answer))
	finalFrame.addRound(strikeRound)
	answer = finalFrame.isScored and (finalFrame.getScore() == 30)
	print("Correctly scored last frame: " + str(answer))
	
	regularFrame = Frame()
	lowRound = Round.Round(2)
	regularFrame.addRound(spareRound)
	regularFrame.addRound(lowRound)
	answer = regularFrame.isFull and regularFrame.isScored and (regularFrame.getScore() == 7)
	print("Correctly scored regular frame: " + str(answer))