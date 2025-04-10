from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def mad_libs():
    print(Fore.CYAN + "Let's play Mad Libs! Fill in the blanks with your own words.\n")

    name = input(Fore.YELLOW + "Give me a name: ")
    place = input(Fore.GREEN + "Give me a place: ")
    funny_adj = input(Fore.MAGENTA + "Give me a funny adjective: ")
    random_object = input(Fore.CYAN + "Give me a random object: ")
    animal = input(Fore.BLUE + "Give me an animal: ")
    action_verb = input(Fore.YELLOW + "Give me an action verb: ")
    funny_exclamation = input(Fore.RED + "Give me a funny exclamation: ")

    story = f"""
{Fore.LIGHTWHITE_EX}Once upon a time, there was a person named {Fore.YELLOW}{name}{Fore.LIGHTWHITE_EX} who lived in {Fore.GREEN}{place}{Fore.LIGHTWHITE_EX}.
One day, they found a {Fore.MAGENTA}{funny_adj} {Fore.CYAN}{random_object}{Fore.LIGHTWHITE_EX} that belonged to a {Fore.BLUE}{animal}{Fore.LIGHTWHITE_EX}.
The {Fore.BLUE}{animal}{Fore.LIGHTWHITE_EX} was very upset and started to {Fore.YELLOW}{action_verb}{Fore.LIGHTWHITE_EX} around.
{name} couldn't help but laugh and shouted \"{Fore.RED}{funny_exclamation}{Fore.LIGHTWHITE_EX}\"!
"""

    print("\nHere is your Mad Libs story:")
    print(story)

    # Save to file
    with open("madlibs_story.txt", "a") as file:
        file.write(story)
        file.write("\n" + "-"*50 + "\n")

    print(Fore.GREEN + "Your story has been saved to 'madlibs_story.txt'! 📄\n")

def main():
    while True:
        mad_libs()
        play_again = input(Fore.CYAN + "Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print(Fore.LIGHTMAGENTA_EX + "\n🎉 Thank you for playing Mad Libs! See you next time! 🎉\n")
            break

if __name__ == "__main__":
    main()
