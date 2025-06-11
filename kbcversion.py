import random

print("Welcome to the KBC Game!")

# List of questions
questions = [
    {"question": "What is the capital of France?", "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"], "answer": "A"},
    {"question": "What is the largest planet in our solar system?", "options": ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"], "answer": "B"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "options": ["A. Harper Lee", "B. Mark Twain", "C. F. Scott Fitzgerald", "D. Ernest Hemingway"], "answer": "A"},
    {"question": "What is the chemical symbol for gold?", "options": ["A. Au", "B. Ag", "C. Pb", "D. Fe"], "answer": "A"},
    {"question": "What is the smallest country in the world?", "options": ["A. Monaco", "B. Vatican City", "C. San Marino", "D. Liechtenstein"], "answer": "B"},
    {"question": "What is the main ingredient in guacamole?", "options": ["A. Tomato", "B. Avocado", "C. Onion", "D. Pepper"], "answer": "B"},
    {"question": "Who painted the Mona Lisa?", "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"], "answer": "C"},
    {"question": "What is the hardest natural substance on Earth?", "options": ["A. Gold", "B. Diamond", "C. Iron", "D. Quartz"], "answer": "B"},
    {"question": "What is the largest mammal?", "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Hippopotamus"], "answer": "B"},
    {"question": "What is the boiling point of water?", "options": ["A. 100°C", "B. 90°C", "C. 80°C", "D. 70°C"], "answer": "A"},
    {"question": "What is the currency of India?", "options": ["A. Dollar", "B. Euro", "C. Rupee", "D. Pound"], "answer": "C"},
]

# Shuffle the questions
random.shuffle(questions)

# Function to ask a single question
def ask_question(question):
    print("\n" + question["question"])
    for option in question["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == question["answer"]:
        print("✅ Correct!")
        return True
    else:
        print(f"❌ Wrong! The correct answer was {question['answer']}.")
        return False

# Run the quiz
score = 0
for i, q in enumerate(questions[:10], start=1):  # Ask up to 10 questions
    print(f"\nQuestion {i}:")
    if ask_question(q):
        score += 1
    else:
        print(f"\n💥 Game Over! You scored {score} out of {i - 1}. Better luck next time!")
        break
else:
    print(f"\n🏆 Congratulations! You answered all 10 questions correctly!")


