
from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def main():
    print("Welcome to the Age Calculator!")
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(dob_input, "%Y-%m-%d")
        age = calculate_age(birth_date)
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format. Please enter in YYYY-MM-DD format.")

if __name__ == "__main__":
    main()
