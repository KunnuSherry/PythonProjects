# from flask import Flask, url_for, render_template, redirect, request
# import random

# app = Flask(__name__)

# words_with_hints = {
#     "python": "coding language",
#     "ocean": "vast body of water",
#     "mountain": "high natural elevation",
#     "desert": "land of sand",
#     "galaxy": "collection of stars",
#     "forest": "dense area of trees",
#     "piano": "musical instrument",
#     "volcano": "erupts with lava",
#     "rainbow": "colors in the sky",
#     "castle": "medieval fortress"
# }

# def randWord():
#     listofwords = list(words_with_hints.keys())
#     return random.choice(listofwords).upper()

# def wordHint(word):
#     return words_with_hints.get(word.lower())

# def play(wordList, word, userTyped):
#     updated = False
#     for i in range(len(word)):
#         if word[i] == userTyped:
#             wordList[i] = userTyped.upper()
#             updated = True
#     return updated

# # Initial game state
# ansWord = randWord()
# wordList = ['_'] * len(ansWord)
# ansHint = wordHint(ansWord)
# chance = 1
# max_chances = 5

# @app.route("/", methods=["POST", "GET"])
# def main():
#     global chance

#     if request.method == "POST":
#         if chance <= max_chances:  # Only process if there are chances left
#             char = request.form.get("char").upper()
#             # Update word list based on the guess
#             updated = play(wordList, ansWord, char)
#             if not updated:
#                 chance += 1  # Increase chance only if the guess was incorrect

#     # Check if the game has ended (either win or max chances reached)
#     game_over = chance > max_chances or "_" not in wordList  # If no underscores are left, user won

#     return render_template(
#         'index.html',
#         wordList="".join(wordList),
#         ansHint=ansHint,
#         chance=chance,
#         game_over=game_over
#     )

# @app.route("/reset")
# def reset():
#     global chance, ansHint, ansWord, wordList
#     ansWord = randWord()
#     wordList = ['_'] * len(ansWord)
#     ansHint = wordHint(ansWord)
#     chance = 1
#     return redirect ("/")

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, session, render_template, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session to work

words_with_hints = {
    "python": "coding language",
    "ocean": "vast body of water",
    "mountain": "high natural elevation",
    "desert": "land of sand",
    "galaxy": "collection of stars",
    "forest": "dense area of trees",
    "piano": "musical instrument",
    "volcano": "erupts with lava",
    "rainbow": "colors in the sky",
    "castle": "medieval fortress"
}

def randWord():
    listofwords = list(words_with_hints.keys())
    return random.choice(listofwords).upper()

def wordHint(word):
    return words_with_hints.get(word.lower())

def play(wordList, word, userTyped):
    updated = False
    for i in range(len(word)):
        if word[i] == userTyped:
            wordList[i] = userTyped.upper()
            updated = True
    return updated

@app.route("/", methods=["POST", "GET"])
def main():
    if 'ansWord' not in session:  # Check if the word is already set in the session
        session['ansWord'] = randWord()
        session['wordList'] = ['_'] * len(session['ansWord'])
        session['chance'] = 1

    ansWord = session['ansWord']
    wordList = session['wordList']
    chance = session['chance']
    ansHint = wordHint(ansWord)

    if request.method == "POST":
        if chance <= 5:
            char = request.form.get("char").upper()
            updated = play(wordList, ansWord, char)
            if not updated:
                session['chance'] += 1

    game_over = chance > 5 or "_" not in wordList

    return render_template(
        'index.html',
        wordList="".join(wordList),
        ansHint=ansHint,
        chance=session['chance'],
        game_over=game_over
    )

@app.route("/reset")
def reset():
    session.pop('ansWord', None)
    session.pop('wordList', None)
    session.pop('chance', None)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
