
import requests
import random

pokemon_list = [
    "charizard",
    "pikachu",
    "lucario",
    "bulbasaur",
    "mewtwo"
]

answer = random.choice(pokemon_list)
url = f"https://pokeapi.co/api/v2/pokemon/{answer}"

try:
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        data = response.json()

        name = data["name"]
        height = data["height"]
        weight = data["weight"]

        print("=== WHO'S THAT POKEMON? ===")
        print("Guess the Pokemon!")
        print(f"Height: {height}")
        print(f"Weight: {weight}")
        print("You have 3 attempts.")

        attempts = 0

        while attempts < 3:
            guess = input("Enter Pokemon name: ").strip().lower()

            if guess not in pokemon_list:
                print("Invalid Pokemon name! Try again.")
                continue

            attempts += 1

            if guess == name:
                print("Correct! You guessed the Pokemon!")
                break
            else:
                remaining = 3 - attempts

                if remaining > 0:
                    print(f"Wrong guess! {remaining} attempt(s) remaining.")
                else:
                    print(f"Game over! The Pokemon was {name.title()}.")

    else:
        print("Could not get Pokemon data. Try again later.")

except requests.exceptions.RequestException:
    print("Network error! Check your internet connection.")

except (ValueError, KeyError):
    print("Error processing Pokemon data. Try again later.")
