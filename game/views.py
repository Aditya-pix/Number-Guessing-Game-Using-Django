import random
from django.shortcuts import render, redirect

def index(request):
    # Initialize session variables
    if "target" not in request.session:
        request.session["target"] = random.randint(1, 100)
        request.session["chances"] = 10
        request.session["message"] = "Guess a number between 1 and 100."

    if request.method == "POST":
        guess = int(request.POST.get("guess"))
        chances = request.session["chances"]
        target = request.session["target"]

        if chances > 0:
            chances -= 1
            request.session["chances"] = chances

            if guess == target:
                request.session["message"] = f"🎉 Congratulations! You guessed it in {10 - chances} tries."
            elif guess > target:
                request.session["message"] = f"📈 Too high! Try again. Chances left: {chances}"
            else:
                request.session["message"] = f"📉 Too low! Try again. Chances left: {chances}"

        if chances == 0 and guess != target:
            request.session["message"] = f"❌ Better luck next time! The number was {target}"

        return redirect("index")

    return render(request, "game/index.html", {
        "message": request.session["message"],
        "chances": request.session["chances"],
    })

def reset(request):
    request.session.flush()  # clears session
    return redirect("index")
