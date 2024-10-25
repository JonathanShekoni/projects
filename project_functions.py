import time

def avg(average):
     time.sleep(2.5)
     print("\nProcessing information")
     time.sleep(2)
     if average < 0:
          print(f"Go and find yuta")
     elif average > 100:
          print(f"Go and meet the goat kasHIMo")
     elif average < 50:
          print(f"Average: {average}")
          print("Fail")
     elif average >= 50:
          print(f"Average: {average}")
          print(f"Pass")