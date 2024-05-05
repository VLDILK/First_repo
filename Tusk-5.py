def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def find_telephone(username, contacts):
    if username in contacts:
        phone_number = contacts[username]
        print(f"Phone number for {username}: {phone_number}")
    else:
        print(f"User {username} not found in the phone book.")

def change_phone(username, new_phone, contacts, old_phone=None):
    if username in contacts:
        old_phone = contacts[username] if old_phone is None else old_phone
        contacts[username] = new_phone
        print(f'Phone number for {username} changed from: {old_phone} to: {new_phone} ')
    else:
        print(f"User {username} not found in the phone book.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
               
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'all':
            print(contacts)
        elif command == 'change':
            if len(args) != 2:
                print('Please provide exactly one username and one new phone number separated by a space.')
            else:
                username, new_phone = args
                old_phone = contacts.get(username)
                change_phone(username, new_phone, contacts, old_phone)

                
        elif command == "phone":
            if len(args) != 1:
                print('After the "phone" command, enter the username with a space.')
            else:    
                username = args[0]
                find_telephone(username, contacts)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

