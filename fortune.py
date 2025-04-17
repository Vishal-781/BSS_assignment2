def main():
    name = "Vishal Shrivastava"  # 🔁 Replace with your full name
    admission_number = "21je1050"  # 🔁 Replace with your admission number

    print(f"\n🔮 Welcome to {name}'s Fortune Teller ({admission_number}) 🔮\n")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print(f"\n✨ Your fortune: Great things await you, {name.split()[0]}! Keep smiling. ✨")
    elif mood == "sad":
        print("\n🌧️ Your fortune: This too shall pass. Better days are coming. 🌈")
    elif mood == "neutral":
        print("\n🔍 Your fortune: Stay alert—unexpected adventures are ahead! 🌟")
    else:
        print("\n🤔 Sorry, I can only read happy/sad/neutral moods for now.")

if __name__ == "__main__":
    main()
