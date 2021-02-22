from flask import (
    Flask,
    render_template,
	jsonify,
	request
)
import Game

# Create the application instance
app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    #hosted on localhost:5000/ this has a small README
    return render_template('home.html')
	

@app.route('/game')
def api_scores():
	#takes in the scores values and converts them to a list of ints that we give to Game to get scores and other info
	if 'scores' in request.args:
		scores = request.args['scores']
		
	rawScores = []
	for i in range(len(scores)):
		if (scores[i] == 'x'):
			rawScores.append(10)
		elif (scores[i].isnumeric()):
			rawScores.append(int(scores[i]))
		else:
			print("unkown value: " + scores[i] + " - ignoring")
	
	game = Game.Game(rawScores)
	answer = [
		{'GameFinished': game.isFinished(),
			'GameScore': game.getScore()
		}]
	frameScores = game.getFrameScores()
	#get the scores from the individual frames
	for i in range(len(frameScores)):
		answer.append({ 'Frame'+str(i+1)+'Round(s)': game.getFrameRounds(i),
						'Frame'+str(i+1)+'Score': frameScores[i]})
	
	return jsonify(answer)
	
	

if __name__ == "__main__":
    app.run(debug=True)