from flask import Flask, render_template, request
from games.dice_game import DiceGame

app = Flask(__name__)
game = DiceGame()

@app.route("/", methods=["GET", "POST"])
def dice():
    global game

    if request.method == "POST":
        if "new_game" in request.form:
            game = DiceGame()
        else:
            roll = int(request.form.get("roll"))
            game.play_turn(roll)

    return render_template(
        "dice.html",
        turn=game.turn,
        point=game.point,
        result=game.result,
        finished=game.finished
    )

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)
