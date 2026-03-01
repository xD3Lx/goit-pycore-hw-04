def parse_input(user_input):
    """
    Parse user input into a command and its arguments.
    Args:
        user_input (str): The raw user input string to be parsed.
    Returns:
        tuple: A tuple containing the command (str) as the first element,
               followed by any number of arguments (str) as remaining elements.
    """

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.
    Args:
        args (tuple): A tuple containing two elements:
            - name (str): The name of the contact to add.
            - phone (str): The phone number of the contact.
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: A message indicating whether the contact was successfully added or if it already exists.
            - "Contact added." if the contact was successfully added.
            - "Contact {name} already exists." if a contact with the same name already exists.
    """

    name, phone = args
    if name in contacts:
        return f"Contact {name} already exists."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    """
    Update an existing contact's phone number.
    Args:
        args (tuple): A tuple containing two elements:
            - name (str): The name of the contact to update.
            - phone (str): The new phone number for the contact.
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: A message indicating whether the contact was successfully updated
             or if the contact does not exist.
    """

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:        
        return f"Contact {name} does not exist."

def show_phone(args, contacts):
    """
    Retrieve and display the phone number for a given contact.
    Args:
        args (list): A list containing the contact name as the first element.
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: The phone number associated with the contact name, or an error message 
             if the contact does not exist.
    """

    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact {name} does not exist."

def all(contacts):
    """
    Display all contacts from the contacts dictionary.
    Args:
        contacts (dict): A dictionary storing contacts.
    Returns:
        str: A string containing all contacts in the format "name: phone" separated by newlines,
             or "No contacts found." if the contacts dictionary is empty.
    """

    output = []

    if (len(contacts) == 0):
        return "No contacts found."
    else:
        for name, phone in contacts.items():
            output.append(f"{name}: {phone}")
        return "\n".join(output)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        # Get user input and parse it into a command and arguments
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        # Check if the command is "close" or "exit" to terminate the chat
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()