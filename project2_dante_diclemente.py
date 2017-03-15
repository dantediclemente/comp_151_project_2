#Dante DiClemente, Pi Project, 3-1-17

import random
from random import uniform

def dart_board():
    square_size = int(input("What is the square size?: "))
    iterations = int(input("How many iterations?: "))
    print_board = int(input("Would you like to print the board? (1 = yes / 0 = no) "))
    iteration_count = 0
    hit_count = 0

    while (iterations > iteration_count):
       x_cordinate = random.uniform(-(square_size / 2), square_size / 2)
       y_cordinate = random.uniform(-(square_size / 2), square_size / 2)
       approx = 4 * (hit_count / iterations)

       if (x_cordinate**2 + y_cordinate**2 <= (square_size / 2)**2):
           print(f"(Dart lands at {x_cordinate}, {y_cordinate}): A Hit")
           print(f"Pi approximation: {approx}" + "\n")
           hit_count +=1
       else:
           print(f"(Dart lands at {x_cordinate}, {y_cordinate}): A Miss")
           print(f"Pi approximation: {approx}" + "\n")
       print_count = 0
       if (print_board == 1):
           print("*" * square_size + "***")
           while (print_count < square_size):
              if (print_count == (square_size / 2) + int(y_cordinate) * -1):
                  end_star = square_size / 2 - int(+x_cordinate)
                  new_x_cordinate = square_size / 2 + int(x_cordinate)
                  print("*" + " " * int(new_x_cordinate) + "<" + " " * int(end_star) + "*")
                  print_count += 1
              else:
                  print("*" + " " * square_size + " *")
                  print_count += 1
              if (print_count == (square_size / 2) - int(y_cordinate)):
                  end_star = square_size / 2 - int(+x_cordinate) - 1
                  new_x_cordinate = square_size / 2 + (int(x_cordinate) * 1)
                  print("*" + " " * int(new_x_cordinate) + "<" + " " * int(end_star) + " *")
                  print_count += 1
              else:
                  print("*" + " " * square_size + " *")
                  print_count += 1
           print("*" * square_size + "***" + "\n\n")
                
       iteration_count += 1

    print(f"The dart hit the board {hit_count} out of {iterations} times.")

dart_board()




