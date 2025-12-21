# we are making a game of millionaire (Kaun Banega Crorepati)
questions = [["who is the First Prime Minister of India" , "Jawaharlal Nehru" , "Narendra Modi", "Rajendra Prasad", "Manmohan Singh",1 ],
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]]
prize_money = [100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000,1100000,1200000]
i = 0
for question in questions:
    print(question[0])
    print(f"option 1. {question[1]}")
    print(f"option 2. {question[2]}")
    print(f"option 3. {question[3]}")
    print(f"option 4. {question[4]}") 

    answer = int(input("enter your seleced answer (1/2/3/4): "))
    if answer == question[5]:
        print("\n Correct answer!")
    else:
        print(f"Incorrect , the correct answer was {question[5]}")
        print("Your game has now ended")
        break
    print(f"You have won the total of rs{prize_money[i]} \n")
    i+=1

