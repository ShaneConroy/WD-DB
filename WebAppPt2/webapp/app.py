import random

from model.data import make_deck, init_deck_values
from calcs import calc_total

from flask import Flask, render_template, request, session

app = Flask(__name__)

playerStood = False

app.secret_key = (
    "kfke hrt'oerj erterutv'rtjv 'oieqrut0345uv 0'34qutv0rutv 'eqrutv equeqtr' u"
)

# Global data.
deck_values = init_deck_values()

def draw():
    """Select a random card from the deck. The deck shrinks by 1."""
    selection = random.choice(session["deck"])
    session["deck"].remove(selection)
    session.modified = True
    return selection, deck_values[selection]
    


@app.get("/")
@app.get("/start")
def display_opening_state():
        session["deck"] = make_deck()
        session["player"] = []
        session["dealer"] = []
        session["player"].append(draw())
        session["dealer"].append(draw())
        session["player"].append(draw())
        session["dealer"].append(draw())
        return render_template(
            "start.html",
            player_cards=session["player"],
            player_total=calc_total(session["player"]),
            dealer_cards=session["dealer"],
            dealer_total=calc_total(session["dealer"]),
            title="",
            header="",
            footer="",
            number_of_cards=len(session["deck"]),
            dealerReveal=0
        )


@app.post("/hit")
def select_another_card():
    if(playerStood == False):
        if(calc_total(session["player"]) > 21):
            return render_template(
                "start.html",
                player_cards=session["player"],
                player_total=calc_total(session["player"]),
                dealer_cards=session["dealer"],
                dealer_total=calc_total(session["dealer"]),
                title="",
                header="",
                footer="",
                number_of_cards=len(session["deck"]),
                lost_text="Player busted! Game over.",
                dealerReveal=0
            )
        elif(calc_total(session["player"]) <= 21):
            session["player"].append(draw())   
            return render_template(
                "start.html",
                player_cards=session["player"],
                player_total=calc_total(session["player"]),
                dealer_cards=session["dealer"],
                dealer_total=calc_total(session["dealer"]),
                title="",
                header="",
                footer="",
                number_of_cards=len(session["deck"]),
                dealerReveal=0
            )
    return render_template(
        "start.html",
        player_cards=session["player"],
        player_total=calc_total(session["player"]),
        dealer_cards=session["dealer"],
        dealer_total=calc_total(session["dealer"]),
        title="",
        header="",
        footer="",
        number_of_cards=len(session["deck"]),
        dealerReveal=1,
    )
        

@app.post("/stand")
def over_to_the_dealer():
    global playerStood
    playerStood = True
    while(calc_total(session["dealer"]) < 17):
        session["dealer"].append(draw())
        return render_template(
            "start.html",
            player_cards=session["player"],
            player_total=calc_total(session["player"]),
            dealer_cards=session["dealer"],
            dealer_total=calc_total(session["dealer"]),
            title="",
            header="",
            footer="",
            number_of_cards=len(session["deck"]),
            dealerReveal=1,
        )
    if(calc_total(session["dealer"]) > 21): # Dealer Busted
        return render_template(
            "start.html",
            player_cards=session["player"],
            player_total=calc_total(session["player"]),
            dealer_cards=session["dealer"],
            dealer_total=calc_total(session["dealer"]),
            title="",
            header="",
            footer="",
            number_of_cards=len(session["deck"]),
            lost_text="Player won! Dealer busted.",
            dealerReveal=1
        )
    if(calc_total(session["dealer"]) > calc_total(session["player"])): # Dealer Beat Player
        return render_template(
            "start.html",
            player_cards=session["player"],
            player_total=calc_total(session["player"]),
            dealer_cards=session["dealer"],
            dealer_total=calc_total(session["dealer"]),
            title="",
            header="",
            footer="",
            number_of_cards=len(session["deck"]),
            lost_text="Dealer Won! Game over.",
            dealerReveal=1
        )
    
@app.post("/restart")
def restart_the_game():
    session["deck"] = make_deck()
    session["player"] = []
    session["dealer"] = []
    session["player"].append(draw())
    session["dealer"].append(draw())
    session["player"].append(draw())
    session["dealer"].append(draw())
    return render_template(
        "start.html",
        player_cards=session["player"],
        player_total=calc_total(session["player"]),
        dealer_cards=session["dealer"],
        dealer_total=calc_total(session["dealer"]),
        title="",
        header="",
        footer="",
        number_of_cards=len(session["deck"]),
        dealerReveal=0,
        playerStood=0
    )

if __name__ == "__main__":
    app.run(debug=True)
