guess = input("Enter a number between -10 and 10:")

if guess < 0:
    print("Your guess was negative.")
elif guess > 0:
    print("Your guess was positive.")
else:
    print("Your guess was zero.")

print("Done.")
