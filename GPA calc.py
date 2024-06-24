Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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
