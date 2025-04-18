import random

def tell_a_joke():
    jokes = [
        "Why do Python programmers wear glasses? Because they can't C!",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why was the JavaScript developer sad? Because he didn't Node how to Express himself.",
        "I told my computer I needed a break, and it said 'Why? I haven’t crashed today!'",
        "What's a programmer's favorite hangout place? The Foo Bar.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How do you comfort a JavaScript bug? You console it.",
        "Why did the Python file break up with the C file? Because it had too many issues to handle.",
        "There are 10 kinds of people in the world: those who understand binary and those who don’t.",
        "Why don't bachelors like Git? Because they are afraid to commit!"
    ]

    print("\n🤣 Here's your joke:")
    print(random.choice(jokes))

while True:
    tell_a_joke()
    another = input("\nWant another one? (yes/no): ").strip().lower()
    if another != "yes":
        print("Alright, enough giggles for now. See you later! 👋")
        break