print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_string = name1 +name2
lower_string ="combined_string".lower()
t ="lower_string".count("t")
r ="lower_string".count("r")
u ="lower_string".count("u")
e ="lower_string".count("e")
true = t+r+u+e
l ="lower_string".count("l")
o ="lower_string".count("o")
v ="lower_string".count("v")
e ="lower_string".count("e")
love = l+o+v+e
score =true + love
if (score<10) or (score)>90:
 print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >=40) and (score<=50):
 print(f"Your score is {score} , you are alright together.")
else:
 print(f"Your score is {score}.")
