import random


questions = [
    {
        "question": "In Marvel Comics, which superhero team consists of characters like Iron Man, Thor, and Hulk?:",
        "choices": ["A) Global Guardians", "B) The Avengers", "C) Justice League", "D) Teen Titans"],
        "correct_answer": "B"
    },
    {
        "question": "Which video game franchise features a character named Kratos as the protagonist?:",
        "choices": ["A) Uncharted", "B) The Last of Us", "C) God of War", "D) Infamous"],
        "correct_answer": "C"
    },
    {
        "question": "Who is the co-founder of Apple Inc., and a pioneer in the personal computer revolution?:",
        "choices": ["A) Elon Musk", "B) Steve Jobs", "C) Bill Gates", "D) Jeff Bezos"],
        "correct_answer": "B"
    },
    {
        "question": "Which director is often referred to as the 'king of the nerds' and has directed movies for Star Wars and Indiana Jones franchises?:",
        "choices": ["A) George Lucas", "B) Steven Spielberg", "C) J. K. Rowling", "D) Gene Roddenberry"],
        "correct_answer": "A"
    },
    {
        "question": "Name the director of the science fiction film 'Inception':",
        "choices": ["A) Quentin Tarantino", "B) James Cameron", "C) Steven Spielberg", "D) Christopher Nolan"],
        "correct_answer": "D"
    },
    {
        "question": "In 'Nurato', the main character, Naruto Uzumaki, is a host for the powerful Nine-Tales. What creature is the Nine-Tails?:",
        "choices": ["A) Lion", "B) Wolf", "C) Fox", "D) Cat"],
        "correct_answer": "C"
    },
    {
        "question": "Which anime series holds the record for the most manga book sold?:",
        "choices": ["A) One Piece", "B) Naruto", "C) Dragon Ball", "D) Detective Conan"],
        "correct_answer": "A"
    },
    {
        "question": "Which American road runs from Chicago to Los Angeles?:",
        "choices": ["A) Route 66", "B) Route 45", "C) Route 13", "D) Route 6"],
        "correct_answer": "A"
    },
    {
        "question": "Who is the author of the epic fantasy series A Song of Ice And Fire, which inspired the TV show 'Game Of Thrones'?:",
        "choices": ["A) J. K. Rowling", "B) J. R. R. Tolkien", "C) Andrzej Sapkowski", "D) George RR Martin"],
        "correct_answer": "D"
    },
    {
        "question": "Who painted the Mona Lisa?:",
        "choices": ["A) Caravaggio", "B) Raffaello", "C) Leonardo da Vinci", "D) Michelangelo"],
        "correct_answer": "C"
    }
]

random.shuffle(questions)

score = 0

print("Welcome to the Quiz Game")
print("------------------------")

for question in questions:
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    
    user_answer = input("Enter the letter corresponding to your answer (A, B, C, or D): ").upper()
    
    if user_answer == question["correct_answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong answer. The correct answer is {question['correct_answer']}.\n")

score = int(score / len(questions) * 100)
print("Congratulations on completing the Quiz, below you will find your score: ")
print("---------------------------------------")
print(f"Your score is: {score}%")