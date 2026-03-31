#Calculator not really just age shit
def scores(score):
    if(score<0 or score>100):
        print("this is incorrect?")
    elif(score>=90):
        print("Your grade is: A")
    elif(score>=80):
        print("Your grade is: B")
    elif(score>=70):
        print("Your grade is: C")
    elif(score>=60):
        print("Your grade is: D")
    else:
        print("Your grade is: F")
def main():
    print("Welcome to the Grade Calculator!")
    print("Please enter your score (0-100):")
    score = input()
    score = int(score)
    scores(score)
if __name__ == "__main__":
    main()

# def scores(score):
#     if(score<0 or score>100):
#         print("this is incorrect?")
#     elif(score>=90):
#         print("Your grade is: A")
#     elif(score>=80):
#         print("Your grade is: B")
#     elif(score>=70):
#         print("Your grade is: C")
#     elif(score>=60):
#         print("Your grade is: D")
#     else:
#         print("Your grade is: F")