import os
import inquirer
import time
import random
import json


book_list = []
users_list = []


def clear_terminal():
  os.system('cls')

def add_book():
  clear_terminal()
  while True:
    try:
      book_name = str(input("Book name: "))
      if any(book_list["book name"] == book_name for book in enumerate(book_list)):
        print("Book already exists!")
        time.sleep(2)
        break
      book_author = str(input("Book author: "))
      book_year = int(input("Book year: "))
      book_publisher = str(input("Book publisher: "))
      book_price = float(input("Book price: "))
      book_pages = int(input("Book pages: "))
      book_genre = str(input("Book genre: "))
    except:
      print("Woah! looks like you typed an invalid input, please, try again")
      time.sleep(2)
      continue

    book = {
    'book name': book_name,
    'author': book_author,
    'year': book_year,
    'publisher': book_publisher,
    'price': book_price,
    'pages': book_pages,
    'genre': book_genre,
    'times borrowed': int(),
    'is borrowed?': "Available",
  }
    try:
      book_list.append(book)
      print(f"Book {book['book name']} added successfully!")
      time.sleep(2)
      break
    except:

      print("Error adding book.")
      time.sleep(2)
      break
def set_book_list(book_name):
  print(f"Title: {book['book name']} \n"
                  f"Author: {book_name['author']} \n"
                  f"Genre: {book_name['genre']} \n"
                  f"Year: {book_name['year']} \n"
                  f"Is borrowed? {book_name['is borrowed?']} \n"
                  f"Times borrowed: {book_name['times borrowed']} \n"
                  f"Price: {book_name['year']} \n")


def delete_book():
  clear_terminal()
  name_book_to_remove = str(input("Name of the book that you want to delete: "))

  for i, book in enumerate(book_list):

    if book["book name"] == name_book_to_remove:

      confirmation = input("Book found, are you sure that you want to remove {name_book_to_remove}? [Y/N]: ").upper()  
      if confirmation == "Y":
        del book_list[i]
        print(f"Book {name_book_to_remove} deleted successfully!")
        break
      else:
        print("Operation cancelled.")
        break

    else:
      print("Book not found.")
      break

  return book_list

def create_user():
  while True:
    clear_terminal()
    username = str(input("Username: "))
    if any(user["username"] == username for user in users_list):
        print("This username is already taken, try another one!")
        time.sleep(2)
        break
    else:
      pass
        
    email = str(input("Email: "))
    if any(user["email"] == email for user in users_list):
      print("This email is already taken, try another one!")
      time.sleep(2)
      break
    else:
      pass
    
    try: 
      age = int(input("Age: "))
    except:
      print("Invalid input. Please enter a valid age.")
      time.sleep(2)
      continue
    


    user = {
      'username': username,
      'email': email,
      'age': age,
      'books borrowed': '',
      'book currently borrowed': '',
    }

    try:
      users_list.append(user)
      print(f"User {username} added successfully!")
      time.sleep(2)
      break
    except:
      print("Error adding user.")
      time.sleep(2)
      break

def locate_user():
  clear_terminal()
  username = str(input("Username: "))
  for i, user in enumerate(users_list):
    if user['username'] == username:
      print(f"User {username} found!")
      print(f"Email: {user['email']} \n"
            f"Age: {user['age']} \n"
            f"Books borrowed: {user['books borrowed']} \n"
            f"book currently borrowed: {user['book currently borrowed']}")
    else:
      print("User not found.")
      input('#')


def delete_user():
  clear_terminal()
  username_to_remove = str(input("Username of the user that you want to delete: "))
  

  for i, user in enumerate(users_list):
    if user["username"] == username_to_remove:
      confirmation = input(f"User {username_to_remove} found, are you sure that you want "
                           f"to remove it? [Y/N]: ").upper()
      if confirmation == "Y":
        del users_list[i]
        print(f"User {username_to_remove} deleted successfully!")
        time.sleep(2)
        break
      else:
        print("Operation cancelled.")
        time.sleep(2)
        break


def borrow_book():
  clear_terminal()
  username = str(input("Enter the username: "))

  for i, user in enumerate(users_list):
    if user["username"] == username:
      if user["book currently borrowed"] != "":
        print("You already have a book borrowed.")
        time.sleep(2)
        break
      # try:
      book_title = str(input("Enter the title of the book you want to borrow: "))
      for i, book in enumerate(book_list):
        if book["book name"] == book_title:
          user["books borrowed"] += book_title + ", "
          user["book currently borrowed"] = book_title
          book["times borrowed"] += 1
          book["is borrowed?"] = book["is borrowed?"].replace(book["is borrowed?"], "borrowed")
          print(f"Book {book_title} borrowed successfully!")
          input("#")
          return book_list
      # except:
        print("Error borrowing book.")
        time.sleep(2)
    else:
      print("User not found.")
      time.sleep(2)


def return_book():
  clear_terminal()
  username = str(input("Enter the username: "))
  for i, user in enumerate(users_list):
    if user["username"] == username:
      book_return = input(f"You are currently with {user["book currently borrowed"]}, would you like to return it? [Y/N]: ").upper()
      if book_return == "Y":
        user["book currently borrowed"] = user["book currently borrowed"].replace(user["book currently borrowed"], "")
        for x, book in enumerate(book_list):
          book["is borrowed?"] = book["is borrowed?"].replace(book["is borrowed?"], "Available")
          time.sleep(2)
      elif book_return == "N":
        print("Action canceled")
        time.sleep(2)
      else:
        print("Invalid input")
        time.sleep(2)
  return book_list

def search_book():
  global book
  clear_terminal()
  while True:
    search_question = input("Do you want to search for a book title? [Y/N]: ").upper()
    if search_question == "Y":
      clear_terminal()
      try:
        book_title = str(input("Enter the title of the book you want to search: "))
      except:
        print("Invalid input, try again")
        continue
      
      for i, book in enumerate(book_list):
        if book["book name"] == book_title:
          print(f"Book {book_title} found!")
          time.sleep(1)
          more_infos_book = input(f"Do you want to see more infos about {book_title}? [Y/N]: ").upper()
          if more_infos_book == "Y":
            clear_terminal()



            set_book_list(book)



            input("#")
          elif more_infos_book == "N":
            print("Operation canceled")
            break
        else:
          print(f"Book {book_title} not found")
          time.sleep(2)
          break
    else:
      
      break

def search_books_by_attribute(book_list, attribute, search_term):
  global book
  clear_terminal()
  results = []
  
  for book in book_list:
    if book[attribute] == search_term:
      results.append(book)
  
  for i, result in enumerate(results, start=1):
    set_book_list(result)
    
    input('#')
    break


def save_lists():
  clear_terminal()
  print("Saving...")
  time.sleep(2)
  files = {
    "books": book_list,
    "users": users_list,
  }
  
  with open("library.json", "w") as archive:
    json.dump(files, archive, indent=2)
  print("Files Saved!")
  time.sleep(2)
  
def read_lists():
  global book_list, users_list
  clear_terminal()
  
  try:
    with open("library.json", "r") as archive:
      new_files = json.load(archive)
      
      book_list = new_files["books"]
      users_list = new_files["users"]
      print("Files loaded!")
      time.sleep(0)
  except:
    print("No files found, starting with empty lists")
    book_list = []
    users_list = []
    time.sleep(2)
  
    #######start########
    
read_lists()
while True:
  clear_terminal()
  questionMenu = [
    inquirer.List(
      "selectionMenu",
      message="=== Library Managment ===",
      choices=[
        "User managment",
        "Book managment",
        "Exit",
      ],
    )
  ]
  answer = inquirer.prompt(questionMenu)
  selectionMenu =answer.get("selectionMenu")

  if selectionMenu == "User managment":

    while True:
      clear_terminal()
      questionUser = [
        inquirer.List(
          "selectionUser",
        message="Create account",
        choices=[
          "Create a new user",
          "Locate user",
          "Delete user",
          "Back",
        ],
      )
    ]
      answer = inquirer.prompt(questionUser)
      selectionUser = answer.get("selectionUser")

      if selectionUser == "Create a new user":
        create_user()

      elif selectionUser == "Locate user":
        locate_user()

      elif selectionUser == "Delete user":
        delete_user()
      elif selectionUser == "Back":
        break

  elif selectionMenu == "Book managment":
    while True:
      clear_terminal()
      questionBook = [
        inquirer.List(
          "SelectionBook",
          message="Book managment",
          choices=[
            "Add a new book",
            "Delete a book",
            "Search a book",
            "Borrow a book",
            "Return a book",
            "Back",
          ],
        )
      ]
      answer = inquirer.prompt(questionBook)
      selectionBook = answer.get("SelectionBook")

      if selectionBook == "Add a new book":
        add_book()    
      elif selectionBook == "Delete a book":
        delete_book()
      elif selectionBook == "Borrow a book":
        borrow_book()
      elif selectionBook == "Return a book":
        return_book()
      elif selectionBook == "Search a book":
        while True:
          clear_terminal()
          questionSearch = [
            inquirer.List(
              "SearchBook",
              message="Search Book",
              choices=[
                "Smart Search",
                "Normal Search",
                "Back"
              ]
            )
          ]
          answer = inquirer.prompt(questionSearch)
          selectionSearchTypes = answer.get("SearchBook")

          if selectionSearchTypes == "Smart Search":
            while True:
              clear_terminal()
              questionSearch = [
                inquirer.List(
                  "SearchBook",
                  message="Search methods",
                  choices=[
                    "By author",
                    "By genre",
                    "Most borrowed",
                    "Random Book",
                    "Back",
                  ]
                )
              ]
              answer = inquirer.prompt(questionSearch)
              selectionSearch = answer.get("SearchBook")

              if selectionSearch == "By author":
                clear_terminal()
                author = input("Enter the author's name: ")
                search_books_by_attribute(book_list, "author", author)
                input("#")

              elif selectionSearch == "By genre":
                clear_terminal()
                genre = input("Enter the genre: ")
                search_books_by_attribute(book_list, "genre", genre)
                input("#")

              elif selectionSearch == "Most borrowed":     
                n = 3 
                try: 
                  sorted_books = sorted(book_list, key=lambda x: x.get("times borrowed", 0), reverse=True)
                  for i, book in enumerate(sorted_books):           
                    set_book_list(book)
                    i += 1
                    if i == 3:
                      input("#")
                      break
                  
                except:
                  print("You must have at least 3 already borrowed books")
                  time.sleep(2)

              elif selectionSearch == "Random Book":
                clear_terminal()
                random_book = random.choice(book_list)
                set_book_list(random_book)
                input("#")

              elif selectionSearch == "Back":
                break

              # else:
              #   print("Invalid search method.")

          elif selectionSearchTypes == "Normal Search":
            search_book() #part of selection book type

          elif selectionSearchTypes == "Back":
            break #part of selection book type

      elif selectionBook == "Back":
        break #part of book managment system

  elif selectionMenu == "Exit":
    save_lists()
    print("Exiting the program.")
    break #part of the menu system

