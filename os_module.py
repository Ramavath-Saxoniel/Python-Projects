import os
import datetime

def get_all_files():
    path = input("Enter your path: ")
    for (root, directories, files) in os.walk(path):
        for file in files:
            print(os.path.join(root,file))

def get_files_with_extension():
    path = input("Enter your path: ")
    extension = input("Enter the file extension: ")
    for (root, directories, files) in os.walk(path):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root,file))

def get_files_created_yesterday():
    start_date = today_date - datetime.timedelta(days=1)
    end_date = today_date
    get_files_between_range(start_date, end_date)

def get_files_between_range(start_date, end_date):
    path = input("Enter your path: ")
    for (root, directories, files) in os.walk(path):
        for file in files:
            file_path = os.path.join(root,file)
            created_date = get_created_date(file_path)
            if created_date >= start_date and created_date <= end_date:
                print(file_path, created_date)
    
def get_created_date(file_path):
    created_time = os.path.getctime(file_path)
    created_date = datetime.date.fromtimestamp(created_time)
    return created_date

def get_files_between_dates():
    start_date = convert_to_date(input("Enter the start date(in yyyy-mm-dd): "))
    end_date = convert_to_date(input("Enter the end date(in yyyy-mm-dd): "))
    get_files_between_range(start_date, end_date)

def convert_to_date(datestring):
    year, month, day = map(int,datestring.split('-'))
    date  = datetime.date(year,month,day)
    return date

today_date = datetime.date.today()
while True:
    print("What would you like to search ?")
    print("all files\nfiles with extension\ncreated yesterday\ncreated between dates\nexit")
    user_choice = input("Enter your choice\n>>>")
    if user_choice == "all files":
        get_all_files()
    elif user_choice == "files with extension":
        get_files_with_extension()
    elif user_choice == 'created yesterday':
        get_files_created_yesterday()
    elif user_choice == 'created between dates':
        get_files_between_dates()
    elif user_choice == "exit":
        break
    else:
        print("Invalid choice")
