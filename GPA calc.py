#Brian Hile
#GPA calc
#calculates gpa through user input
>>> def main():
...     while True:
...         last_name = input("Enter student's last name (Enter 'ZZZ' to quit): ")
...         if last_name == 'ZZZ':
...             print("Quitting program...")
...             break
...         
...         first_name = input("Enter student's first name: ")
...         gpa = float(input("Enter student's GPA: "))
...         
...         if gpa >= 3.5:
...             print(f"{first_name} {last_name} has made the Dean's List!")
...         elif gpa >= 3.25:
...             print(f"{first_name} {last_name} has made the Honor Roll!")
...         else:
...             print(f"Unfortunately, {first_name} {last_name} does not qualify for Dean's List or Honor Roll.")
...         
...         print()  # Just for spacing between records
... 
... if __name__ == "__main__":
...     main()
