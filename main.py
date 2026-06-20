import random

from qns import questions

print("Welcome to Kaun Banega Crorepati (KBC)\n"
      "Here are the rules:\n\n"
      "1. Answer correctly to win money.\n"
      "2. Wrong answer ends the game.\n"
      "3. Checkpoints at 10,000, 320,000, and 7,000,000 lock your winnings.\n"
      "4. Lifelines: '50-50' press (1) 'Swap Question' press (2).\n"
      "5. Use lifelines by entering 'l'.\n"
      "6. Quit with 'q'.\n"
      "7. Prize money increases with correct answers.\n"
      "8. If you quit, winnings based on last checkpoint.")

name = input("\nEnter your name to continue the game: ")
name = name if len(name) >= 3 else "guest"


def keyInput(messg="Choose option"):
  options = {
      'a': 1,
      'b': 2,
      'c': 3,
      'd': 4,
      'l': 'l',
      '1': '50-50',
      '2': 'swap question',
      'q': 'q',
  }

  i = input(f'{messg}: ').lower()

  while i not in options:
    print("\nInvalid key enter!")
    i = input(f'{messg}: ').lower()
  return options.get(i, None)


levels = (1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,
          640000, 1250000, 2500000, 5000000, 10000000, 30000000, 50000000,
          75000000)

lifeline = {"50-50", "swap question"}


def updateWinning(winning, current_winning):
  stages = (10000, 320000, 75000000)
  if winning in stages:
    current_winning = winning
  return current_winning


winningAmount = 0

for q in range(len(levels)):

  winning = levels[q]

  question = questions[q]["question"].capitalize()
  options = questions[q]["options"]
  answer = questions[q]["answer"]

  print(f"Question for Rs. {winning}\n\n{q + 1}. {question}")
  for i, option in enumerate(options):
    print(f"({chr(97+i)}) {option}")

  userInput = keyInput('Choose the correct answer')

  if userInput == answer:

    winningAmount = updateWinning(winning, winningAmount)

    print(f'\nCorrect answer! You won Rs. {winning}')

  elif userInput == "q":
    print(f'\nGame quited. Your winning amount is: Rs. {winningAmount}.')

    winningAmount = winning
    break

  elif userInput == 'l':

    if lifeline:

      print('\nYour lifelines')

      if "50-50" in lifeline:
        print("1. 50-50")
      if "swap question" in lifeline:
        print("2. swap question")

        lifelineChoice = keyInput("Choose the lifeline")

        lifeline.remove(lifelineChoice)

        if lifelineChoice == "50-50":

          incorrect_options = list(
              filter(lambda x: x != options[answer - 1], options))

          random_option = random.choice(incorrect_options)

          options = [options[answer - 1], random_option]

          random.shuffle(options)

          print(f"\n50-50: {' / '.join(options)}")

          lastChoice = keyInput("Choose the correct answer")

          answer = questions[q]["answer"]

          if lastChoice == answer:
            winningAmount = updateWinning(winning, winningAmount)

            print(f'\nYeh you be saved! You won Rs. {winning}')
          else:
            print(
                f'\nWrong answer, You loose the game.\nYour winning ammount is: {winningAmount}'
            )
            break

        elif lifelineChoice == "swap question":

          print("\nSwapping the question...")

          qu = random.choice(questions)
          question = qu['question']
          options = qu['options']
          answer = qu['answer']

          print(f"\nSwap qns: {question}")

          for i, option in enumerate(options):
            print(f"({chr(97+i)}) {option}")

          userInput = keyInput("Choose the correct answer")

          if userInput == answer:

            winningAmount = updateWinning(winning, winningAmount)

            print(f'\nYeh you be saved! You won Rs. {winning}')
          else:
            print(
                f'\nWrong answer, You loose the game.\nYour winning ammount is: {winningAmount}'
            )
            break

      else:
        print(
            f"\nNo lifeline remaining. Better luck next time!\nYour winning amount is: Rs. {winningAmount}"
        )
        break
  else:
    print(
        f'\nWrong answer, You loose the game.\nYour winning ammount is: {winningAmount}'
    )
    break

  if q + 1 == len(levels):
    print(
        f"\nCongratulations 🎉 {name.capitalize()}, You won the game!\nYour winning amount is: Rs. {winningAmount}"
    )
    break
