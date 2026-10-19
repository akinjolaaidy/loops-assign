def is_armstrong(number):

    num_str = str(number)
    power = len(num_str)
    

    total_sum = sum(int(digit) ** power for digit in num_str)
    
    return total_sum == number


user_input = input("Enter a positive whole number to check: ")
num = int(user_input)

if num < 0:
     print("Please enter a positive integer.")
else:
    if is_armstrong(num):
        print(f"✨ Yes! {num} is an Armstrong number.")
    else:
     print(f"❌ No. {num} is not an Armstrong number.")

