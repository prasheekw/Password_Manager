def writes(webname, username, password):
    with open('PasswordFile.txt', 'a') as PasswordFile:
        info = {
            'website' : f'{webname}',
            'Username' : f'{username}',
            'Password': f'{password}'
        }
        for key, value in info.items():
            PasswordFile.write(f"{key}: {value}, ")
        PasswordFile.write("\n")

def add_cred():
    print("****Enter the Web cred****")
    website = input("")
    username = input("")
    password = input("")
    writes(website, username, password)

def display_cred():
    with open('PasswordFile.txt', 'r') as PasswordFile:
        while True:
            dets = PasswordFile.readline()
            if not dets:
                break
            parts = dets.split(",")
            web = parts[0].split(":")[1].strip()
            user = parts[1].split(":")[1].strip()
            Pass = parts[2].split(":")[1].strip()
            print("-------------------")
            print(f'''website:{web}
username: {user}
password: {Pass}''')
            print("-------------------")

def search_cred():
  while True:
      pointer = input("Enter website name to search for credentials: ").lower()
      if pointer == 'exit':
        break
      with open('PasswordFile.txt', 'r') as pf:
            found = False
            for line in pf:
              obj = line.split(',')
              cursor = obj[0].split(':')
              m = cursor[1].strip()
              if m == pointer:
                found = True
                username = obj[1].split(":")[1].strip()
                password = obj[2].split(":")[1].strip()
                print(f"website : {m}, username: {username}, password: {password}")
                break

            if not found:
                print("search crediential not found!!")
if __name__ == '__main__':
  while True:
      try:
          print("""
0. Exit
1. Add Credential
2. Search Credential
3. Display Credentials
""")
          choice = int(input("Enter your choice: "))
          match(choice):
            case 0:
              break
            case 1:
              add_cred()
            case 2:
              search_cred()
            case 3:
              display_cred()
            case _:
              print("Invalid input, please give valid input within the range of 1 to 3")
    
      except ValueError as e:
          print(f"Oops! Something went wrong: {e}")