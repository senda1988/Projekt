import random


def game():
    user_choice_str = input("Wähle eine ganze Zahl zwischen 1 und 10! ")
    user_choice = int(user_choice_str)

    if not user_choice_str.isdigit():
        print("Keine gültige Zahl! Probiere nochmal")
        game()

    if not (
        (user_choice == 1)
        or (user_choice == 2)
        or (user_choice == 3)
        or (user_choice == 4)
        or (user_choice == 5)
        or (user_choice == 6)
        or (user_choice == 7)
        or (user_choice == 8)
        or (user_choice == 9)
        or (user_choice == 10)
    ):
        print("Ungültige Angabe! Probiere nochmal!")
        game()

    compu_choice = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    if user_choice == compu_choice:
        print(
            f"Glückwunsch! Das Computer hat auch die {compu_choice} gewählt. Du hast gewonnen!"
        )
    else:
        print(
            f"Das Computer hat die {compu_choice} gewählt. Du hast leider verloren. Probiere noch einmal!"
        )
        game()


game()
