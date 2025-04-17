import random

def main():
    name = "Vishal Shrivastava"  
    admission_number = "21JE1050" 
    print(f"\n🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮\n")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            f"Great things await you, {name.split()[0]}! Keep smiling. ✨",
            "Your energy is contagious—spread it far and wide!",
            "You're shining bright today. Don’t let anyone dim that light!"
        ],
        "sad": [
            "This too shall pass. Better days are coming. 🌈",
            "Tough times never last, but tough people do.",
            "Even the darkest night will end, and the sun will rise. ☀️"
        ],
        "neutral": [
            "Stay alert—unexpected adventures are ahead! 🌟",
            "Today might seem calm, but surprises await. 🧭",
            "Keep an open mind. Opportunity often hides in plain sight."
        ],
        "stressed": [
            "Breathe, relax. You’re doing better than you think. 🧘",
            "Even chaos has its own rhythm—trust yourself.",
            f"{name}, remember: pressure creates diamonds. 💎"
        ]
    }

    if mood in fortunes:
        print("\n✨ Your fortune:", random.choice(fortunes[mood]))
    else:
        print("\n🤔 Sorry, I don't have a fortune for that mood yet.")

if __name__ == "__main__":
    main()
