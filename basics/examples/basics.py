'''
Basics
'''
import random as rn

def conversation(yes, no):
    answers = [yes, no]
    print("Do you want to ask me?")
    for answer in answers:
        if answer != answers[-1]:
            print("{yes} or {y}, ".format(yes=answer, y=answer[0]), end='')
        else:
            print(f"{answer} or {answer[0]}")

    choice = input()
    while choice == "yes" or choice == "y" or choice == "Yes":
        print("How much money do you have?")
        money = int(input("Suggest: "))
        if money >= 1000:
            print("I can give you", money, "dollars")
        elif money >= 500 and money < 1000:
            print("I can give you only", money, "dollars")
        else:
            print(f"I can't give you {money} dollars")
        print("Do you want to ask me?")
        print("(", end='') 
        for i in range(len(answers)):
            if answers[i] != answers[-1]:
                print(f"{answers[i]}, ", end='')
            else:
                print("{0}".format(answers[i]), end='')
        print(")") 
        choice = answers[rn.randint(0, len(answers)-1)]
        print(choice)
    return choice

listOfAnswers = ['yes', 'no']
listOfAnswers.append(['Yes', 'No'])
listOfAnswers.insert(len(listOfAnswers), ['Yes', 'No'])
print(conversation(*listOfAnswers[2]))

dictOfAnswers = {
    'first answer': [
        'yes',
        'no'
    ],
    'second answer': [
        'no',
        'yes'
    ]
}

conversation(dictOfAnswers["first answer"][0], dictOfAnswers["second answer"][0])