def main():
    name = "Андрей"
    print(name)

    age = 20
    print("Мне", age, "лет")

    print(name * 5, "\n")

    print("Enter your name:\n")
    userName = input()
    if " " in userName:
        print("Value error for name")
        exit(1)
    print("Enter your age:\n")
    try:
        userAge = input()
    except:
        print("Value error for age")
        exit(1)
    if int(userAge) < 0 or int(userAge) > 150:
        print("Value error for age")
        exit(1)
    print("Hello", userName, userAge, "years old")

    userAgeInt = int(userAge)
    print(userAgeInt)
    if userAgeInt > 20:
        print("You are over 20")
    if userAgeInt < 20:
        print("You are under 20")
    if userAgeInt == 20:
        print("You are 20 years old")

    print(userName[::-1])
    print(userName[1:-1])
    print(userName[-3:])
    print(userName[:5])

    nameLen = len(userName)
    print("nameLen =", nameLen)
    i = 0
    summ = 0
    mult = 1
    while i < len(userAge):
        summ = summ + int(userAge[i])
        mult = mult * int(userAge[i])
        i +=1
    print("sum=",summ,"mult=",mult)

    print(userName.upper(),userName.lower(),userName[::-1].capitalize(),userName.capitalize())

    print("2+2*2")
    a = -1
    input(a)
    if a == 6:
        print("correct")
    else:
        print("incorrect")


main()
