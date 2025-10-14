from datetime import date
if __name__ == "__main__":
    name, surname, birth_year = input("Please provide your name, last name and year of birth separated by space: ").split()

    try:
        birth_year = int(birth_year)
        print(f"Name: {name}, Surname: {surname}, Year of Birth: {birth_year}, Your Age: {(birth_year - date.today().year) * (-1)}")
    except:
        print("Error - check if your birth year is an integer")