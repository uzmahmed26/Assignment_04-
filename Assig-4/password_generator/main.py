import random
import string

def generate_password(lenght):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range (lenght))
    return password

lenght = int(input("enter the desired password lenght: "))

if __name__ == "__main__":
    print("Generate Password:", generate_password(lenght))
    