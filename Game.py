#This takes a list of raw rounds (just the number of pins knocked down per round), puts them in frames, and scores them
import Frame
import Round
class Game:
	
	def __init__(self, rawRounds):
		self.finished = False
		self.score = 0
		self.frames = [Frame.Frame() for i in range(9)]
		self.frames.append(Frame.Frame(True))
		self.makeFrames(rawRounds)
		
		
	def makeFrames(self, rawRounds):
		j=0
		for i in range(len(rawRounds)):
			success = self.frames[j].addRound(Round.Round(rawRounds[i]))
			if (success == False):
				j+= 1
				if (j < len(self.frames)):
					success = self.frames[j].addRound(Round.Round(rawRounds[i]))
				else:
					print("Error: too many rounds for number of frames")
					return
					
			if (self.frames[j].isStrike() and self.frames[j].isFull() and not self.frames[j].isScored()):
				if ((i+2) < len(rawRounds)):
					self.frames[j].finishScore(rawRounds[i+1], rawRounds[i+2])
			elif (self.frames[j].isSpare() and self.frames[j].isFull() and not self.frames[j].isScored()):
				if ((i+1) < len(rawRounds)):
					self.frames[j].finishScore(rawRounds[i+1])
			
			if (self.frames[j].isScored()):
				self.score += self.frames[j].getScore()
				if (j == 9):
					self.finished = True
					
	def getFrameScores(self):
		scores = []
		for i in range(len(self.frames)):
			scores.append(self.frames[i].getScore())
		
		return scores
		
	def getFrameRounds(self, index):
		rounds = []
		first = self.frames[index].getFirstRoundScore()
		
		if (first != False):
			if (first == 10):
				rounds.append('x')
			else:
				rounds.append(first)
		second = self.frames[index].getSecondRoundScore()
		
		if (second != False):
			if (second == 10):
				rounds.append('x')
			elif (self.frames[index].isSpare()):
				rounds.append('/')
			else:
				rounds.append(second)
		third = self.frames[index].getThirdRoundScore()
		
		if (third != False):
			if (third == 10):
				rounds.append('x')
			else:
				rounds.append(third)
		
		return rounds
		
				
	def isFinished(self):
		return self.finished
		
		
	def getScore(self):
		return self.score
		
		
################################### Testing ################################
if (__name__ == "__main__"):
	strikeGame = Game([10,10,10,10,10,10,10,10,10,10,10,10])
	answer = strikeGame.isFinished() and (strikeGame.getScore() == 300)
	print("Correctly processed strike game: " + str(answer))
	
	almostStrikeGame = Game([10,10,10,10,9,0,10,10,10,10,10,10,10])
	answer = almostStrikeGame.isFinished() and (almostStrikeGame.getScore() == 267)
	print("Correctly processed almost strike game: " + str(answer))
	
	inProgress = Game([10])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==0)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==26)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==26)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==26)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==41)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==50)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==50)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==50)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==72)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==72)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5,5])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==72)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5,5,7])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==89)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5,5,7,3])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==89)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5,5,7,3,1])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==100)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5,5,7,3,1,9])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==100)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5,5,7,3,1,9,10])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==120)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5,5,7,3,1,9,10,9])
	answer = not inProgress.isFinished() and (inProgress.getScore() ==120)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5,5,7,3,1,9,10,9,0])
	answer = inProgress.isFinished() and (inProgress.getScore() ==139)
	print("Correctly scorring in progress game: " + str(answer))
	
	inProgress = Game([10,5,3,7,3,5,4,10,4,2,5,5,7,3,1,9,10,9,6])
	answer = inProgress.isFinished() and (inProgress.getScore() ==145)
	print("Correctly scorring in progress game: " + str(answer))
	
	print(inProgress.getFrameScores())
