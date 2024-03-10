#program:the user is showen a list containing a group of games.the user chooses the aappropriate game for him
#Authors:menna mohammed abdullah_20230420:problem(1,6)
# nada samir hanafi ahmed_20230441:problem(2,5)
#habiba osama abd elmonem _20231045(3,4)
#version:1.2
#date:26\2\2024
def calculating_grads (): 
 #welcome message
  print("hellow  ")
# the user will enter his mark and the grade will show
  while True:
    try:
        the_grade=int(input("inter your grade :"))
    #if the user doesnt enter an integr number, i will display message error
    except ValueError:
        print("please enter valid value")
        continue
    #if the user enter number greater than 100 or less than 0, i will display messege error
    if not(the_grade>=0 and the_grade<=100):
         print("please enter valid value")
         continue
    if the_grade>=90:
        print("the grade : A+")
        break
    if the_grade>=85:
        print("the grade :A")
        break
    if the_grade>=80:
        print("the grade:B+")
        break
    if the_grade>=75:
        print("the grade:B")
        break
    if the_grade>=70:
        print("the grade:C+")
        break
    if the_grade>=65:
        print("the grade:C")
        break
    if the_grade>=60 :
        print("the grade:D+")
        break
    if the_grade>=50:
        print("the grade:D")
        break
    if the_grade<50:
        print("YOU failed")
        break
def armstrong_number():
    import math

    print("Welcome")
    print("Please enter a positive integer (or a negative number to exit)")

    while True:
     try:
        number = int(input())

        if number < 0:
            print("Exiting the program")
            break  # Exit the loop if the user enters a negative number

        number_string = str(number)
        result = 0

        for digit_char in number_string:
            digit = int(digit_char)
            result += math.pow(digit, 3)

        if result == number:
            print(f"{number}: is an Armstrong number")
            break
        else:
            print(f"{number}: is not an Armstrong number")
            break

     except ValueError:
        print("Invalid input. Please enter an integer.")
def find_pi():
    print ("welcome , this program get value of pi according to number of terms given \nby using Leibniz math formula")
    n = input("enter no of terms : ")
    while True  :             # Make sure its valid
     if n.isdigit() :
      n = int(n)
     if n > 0 :
        break
     else :
        n = input("ERROR : enter valid positive no of terms : ")
     quarter_pi = 1            # Put first term in variable
     i=1                       
     count= 1
     if count == (n/2) :               # One term in the count ..without 1
      i +=2
      x=(1/i)
      i+=2
      quarter_pi -= x
      count+=1
     while count < (n / 2) :    # Two terms each count ..without 1  
      i +=2
      x=(1/i)-(1/(i+2))
      i+=2
      quarter_pi -= x         # Minus each couple of terms 
      count+=1
     if count == (n/2) and n % 2 == 0 : # At last count for positive no of terms minus one term only
       i +=2
       x=(1/i)
       i+=2
       quarter_pi -= x
       count+=1
  
    print (f"pi = {quarter_pi * 4}")
def transfferring():
    print ("welcome , this program make incrypted massage")
    string = input("enter a message to be incrypted : ")
    new_string = ""
    for i in string :
      if i == " " :
        new_string += " "
        continue
    new_string += chr(ord(i) + 1)
    print (f"your new message is : {new_string}")
def  check2_lists_are_equal_or_not():
    print("Welcome , this program checks if two lists are equal or not")
    print("Please enter the length of the first list")
    while True:
      try:
        len1 = int(input())
        if len1 > 0:
            break
        else:
            print("Please enter a valid positive integer for the length of the first list")
      except ValueError:
        print("Invalid input. Please enter an integer.")

      print("Please enter the length of the second list")
      while True:
       try:
         len2 = int(input())
         if len2 > 0:
            break
         else:
            print("Please enter a valid positive integer for the length of the second list")
       except ValueError:
         print("Invalid input. Please enter an integer.")

      a = []
      b = []

      if len1 != len2:
        print("Lists are not equal => as two lengths are not equal")
      else:
       count = 0
       print("Please enter list1")
       for _ in range(len1):
        while True:
            try:
                a.append(int(input()))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

      print("Please enter list2")
      for _ in range(len2):
        while True:
            try:
                b.append(int(input()))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

      a.sort()
      b.sort()

      for i in range(len1):
        if a[i] == b[i]:
            count += 1

      if count == len1:
        print("Lists are equal ")
      else:
        print("Lists are not equal")
def find_factors():
    #welcome message 
  print ("welcom user name")
  while True:
    try:
        the_number=int(input("enter the number:"))
#if the user doesnt enter an integr number, i will display message errorr
    except ValueError:
        print("please enter valid value")
        continue
#i will check the numbers from 1 to the enterd number that the enterd number is divised by
    for i in range(1,the_number+1):
        if the_number%i==0:
            print (i)
    break
    
while True:
    list_of_problems=["a:calculating_grads", "b:armstrong_number" ,"c:find_pi", "d:transferring" ,"e:check 2 lists are eqal or not" ,"f:find the factors"]
    print(list_of_problems)
    the_choice=input("choose form the list")
    if the_choice=="a":
        calculating_grads()
        while True:
          choice2=["A:TRY AGAIN","B:ExIT"]
          print(choice2)
          the_choice2=input("choose A or B:")
          if the_choice2=="A" or the_choice2=="B":
              break
          else:
              continue
        if the_choice2=="A":
           continue
        if the_choice2=="B":
            break
    if the_choice=="b":
        armstrong_number()

        while True:
          choice2=["A:TRY AGAIN","B:ExIT"]
          print(choice2)
          the_choice2=input("choose A or B:")
          if the_choice2=="A" or the_choice2=="B":
              break
          else:
              continue
        if the_choice2=="A":
           continue
        if the_choice2=="B":
            break
    if the_choice=="c":
        find_pi()
        while True:
          choice2=["A:TRY AGAIN","B:ExIT"]
          print(choice2)
          the_choice2=input("choose A or B:")
          if the_choice2=="A" or the_choice2=="B":
              break
          else:
              continue
        if the_choice2=="A":
           continue
        if the_choice2=="B":
            break
    if the_choice=="d":
        transfferring()
        while True:
          choice2=["A:TRY AGAIN","B:ExIT"]
          print(choice2)
          the_choice2=input("choose A or B:")
          if the_choice2=="A" or the_choice2=="B":
              break
          else:
              continue
        if the_choice2=="A":
           continue
        if the_choice2=="B":
            break
    if the_choice=="e":
        check2_lists_are_equal_or_not()
        while True:
          choice2=["A:TRY AGAIN","B:ExIT"]
          print(choice2)
          the_choice2=input("choose A or B:")
          if the_choice2=="A" or the_choice2=="B":
              break
          else:
              continue
        if the_choice2=="A":
           continue
        if the_choice2=="B":
            break
    if the_choice=="f":
        find_factors()
        while True:
          choice2=["A:TRY AGAIN","B:ExIT"]
          print(choice2)
          the_choice2=input("choose A or B:")
          if the_choice2=="A" or the_choice2=="B":
              break
          else:
              continue
        if the_choice2=="A":
           continue
        if the_choice2=="B":
            break
    else:
        print("please enter valid choice")
        continue