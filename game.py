def run_quiz():
    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["a) func", "b) define", "c) def", "d) function"],
            "answer": "c"
        },
        {
            "question": "What color was the pill Neo took in The Matrix?",
            "options": ["a) Blue", "b) Red", "c) Green", "d) Yellow"],
            "answer": "b"
        },
        {
            "question": "What does HTML stand for?",
            "options": ["a) HighText Machine Language", "b) HyperText Markup Language", "c) HyperTransfer Media Language", "d) Home Tool Markup Language"],
            "answer": "b"
        },
        {
            "question": "Which movie features the quote: 'To infinity and beyond!'?",
            "options": ["a) The Incredibles", "b) Finding Nemo", "c) Toy Story", "d) Cars"],
            "answer": "c"
        },
        {
            "question": "What is the output of: print(2 ** 3)?",
            "options": ["a) 5", "b) 6", "c) 8", "d) 9"],
            "answer": "c"
        }
    ]

    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (a/b/c/d): ").strip().lower()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {q['answer']}")
    
    print(f"\n🎉 Quiz Over! You scored {score}/{len(questions)}")

while True:
    run_quiz()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! 👋")
        break
