first_side = int(input("Enter the length of the first side: "))
second_side = int(input("Enter the length of the second side: "))
third_side = int(input("Enter the length of the third side: "))
if first_side == second_side == third_side: 
    print("The triangle is equilateral.")
elif first_side == second_side or second_side == third_side or first_side == third_side:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")