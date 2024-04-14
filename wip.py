def puz1():
    print("You stand in front of a large, imposing computer terminal. The screen is dark, and the system appears to be offline.")
    print("The Power Switch: You notice a small, red switch on the side of the terminal.")
    print("It seems to be the power switch. However, it's locked in place with a rusty padlock.")
    print("You need to find the key. Where will you look?")
    print("a. Search the desk nearby.")
    print("b. Check the drawers under the desk.")
    print("c. Inspect the shelves on the wall.")

    choice = input("Enter your choice (a, b, or c): ")

    if choice == "a":
        search_desk()
    elif choice == "b":
        check_drawers()
    elif choice == "c":
        inspect_shelves()
    else:
        print("Invalid choice. Please try again.")
        puz1()

def search_desk():
    print("Finding the Key: You choose to search the desk nearby.")
    print("After rummaging through some papers and office supplies, you find a key hidden under a stack of old manuals.")
    print("You use it to unlock the padlock and flip the power switch. The computer hums to life.")
    login_screen()

def check_drawers():
    print("Checking the drawers under the desk: You search through the drawers under the desk, but find nothing of interest.")
    puz1()

def inspect_shelves():
    print("Inspecting the shelves on the wall: You find a dusty old book, but no key.")
    puz1()

def login_screen():
    print("The Login Screen: The computer boots up, and you're greeted with a login screen.")
    print("It requires a username and password to proceed. Where will you look for this information?")
    print("a. Check the sticky notes on the monitor.")
    print("b. Look through the papers on the desk.")
    print("c. Try 'admin' as the username and 'password' as the password.")

    choice = input("Enter your choice (a, b, or c): ")

    if choice == "a":
        check_sticky_notes()
    elif choice == "b":
        look_through_papers()
    elif choice == "c":
        try_login("admin", "password")
    else:
        print("Invalid choice. Please try again.")
        login_screen()

def check_sticky_notes():
    print("Username and Password: You decide to check the sticky notes on the monitor.")
    print("Among various reminders and memos, you find a note with the username 'sysadmin' and a password scribbled underneath.")
    try_login("sysadmin", "password")

def look_through_papers():
    print("Looking through the papers on the desk: You find some interesting documents, but no login information.")
    login_screen()

def try_login(username, password):
    print("Attempting login with username: {} and password: {}".format(username, password))
    # Add your logic here to check if the login is successful
    # For example, you can compare the entered username and password with the expected values
    # If the login is successful, proceed to system initialization
    # Otherwise, display an error message and prompt for login again

def system_initialization():
    print("System Initialization: With access granted, the computer begins to initialize its systems.")
    print("However, it prompts you to complete a final authentication step: solving a captcha puzzle to prove you're not a bot.")
    print("The captcha reads: 'What is the capital of France?'")
    print("a. Enter 'Paris' as the answer.")

    choice = input("Enter your choice (a): ")

    if choice == "a":
        solve_captcha()
    else:
        print("Invalid choice. Please try again.")
        system_initialization()

def solve_captcha():
    print("Captcha Puzzle: You correctly enter 'Paris' as the answer to the captcha puzzle.")
    print("The computer accepts your response and completes its initialization process.")
    print("Congratulations! You've successfully turned on the computer and found a way to log in.")




def explore_file_system():
    print("Exploring the File System: You navigate through the computer's file system, examining directories and folders for any signs of a program to open.")
    print("Where will you start your search?")
    print("a. Explore the 'Applications' folder.")
    print("b. Check the 'System' folder for hidden files.")
    print("c. Investigate the 'User Documents' directory.")

    choice = input("Enter your choice (a, b, or c): ")

    if choice == "a":
        explore_applications_folder()
    elif choice == "b":
        check_system_folder()
    else:
        print("Invalid choice. Please try again.")
        explore_file_system()

def explore_applications_folder():
    print("Exploring the 'Applications' folder: You search through the 'Applications' folder for any programs of interest.")
    print("After some time, you come across a hidden directory named 'GTW1983'.")
    print("Inside, you discover a program titled 'Global Thermonuclear War'.")
    print("Congratulations! Your boring!.")
    # Add your logic here to interact with the program

def check_system_folder():
    print("Scanning System Logs: You decide to check the 'System' folder for hidden files.")
    print("Among the various system logs and configuration files, you come across a suspicious entry in the log file labeled 'Access Denied'.")
    print("Perhaps there's something hidden within this entry. What will you do?")
    print("a. Open the 'Access Denied' log file and investigate further.")
    print("b. Ignore the log file and continue searching elsewhere.")
    print("c. Run a search command to find all instances of 'Access Denied' in the system logs.")

    choice = input("Enter your choice (a, b, or c): ")

    if choice == "a":
        open_access_denied_log()
    elif choice == "b":
        continue_searching()
    elif choice == "c":
        search_access_denied_logs()
    else:
        print("Invalid choice. Please try again.")
        check_system_folder()

def open_access_denied_log():
    print("Deciphering the Log Entry: You open the 'Access Denied' log file and examine its contents.")
    print("Among the cryptic messages, you notice a recurring sequence of characters that seem out of place.")
    print("It reads: 'G-T-W-1-9-8-3.' Could this be a clue to the hidden program's location? What do you make of it?")
    print("a. Try to decode the sequence of characters to reveal its meaning.")
    print("b. Search for any files or directories with a name resembling the decoded sequence.")
    print("c. Consult the computer's user manual or help documentation for any references to 'G-T-W-1-9-8-3'.")

    choice = input("Enter your choice (a, b, or c): ")

    if choice == "a":
        decode_sequence()
    elif choice == "b":
        search_files_directories()
    elif choice == "c":
        consult_user_manual()
    else:
        print("Invalid choice. Please try again.")
        open_access_denied_log()

def decode_sequence():
    print("Decoding the Clue: After some thought, you realize that the sequence of characters corresponds to 'GTW1983', which could be an acronym or abbreviation.")
    print("With this revelation, you proceed to search for any files or directories with a similar name.")
    print("Where will you look next?")
    print("a. Search the entire file system for files containing 'GTW1983' in their names.")
    print("b. Look specifically within the 'Applications' folder for any matching files.")
    print("c. Check if there's a hidden directory or subfolder where the program might be located.")

    choice = input("Enter your choice (a, b, or c): ")

    if choice == "a":
        search_file_system()
    elif choice == "b":
        search_applications_folder()
    elif choice == "c":
        check_hidden_directory()
    else:
        print("Invalid choice. Please try again.")
        decode_sequence()

def search_file_system():
    print("Searching the File System: You initiate a search for files containing 'GTW1983' in their names.")
    print("After a thorough scan of the entire file system, you discover a hidden directory named 'GTW1983'.")
    print("Inside, you find the program titled 'Global Thermonuclear War'.")
    print("Congratulations! You've found the hidden program.")
    # Add your logic here to interact with the program

def search_applications_folder():
    print("Searching the 'Applications' folder: You search specifically within the 'Applications' folder for any files or directories with a name resembling 'GTW1983'.")
    print("After some time, you come across a hidden directory named 'GTW1983'.")
    print("Inside, you discover a program titled 'Global Thermonuclear War'.")
    print("Congratulations! You've found the hidden program.")
    # Add your logic here to interact with the program

def check_hidden_directory():
    print("Checking for Hidden Directory: You investigate if there's a hidden directory or subfolder where the program might be located.")
    print("After a thorough search, you discover a hidden directory named 'GTW1983'.")
    print("Inside, you find the program titled 'Global Thermonuclear War'.")
    print("Congratulations! You've found the hidden program.")
    # Add your logic here to interact with the program

def continue_searching():
    print("Continuing the Search: You decide to ignore the 'Access Denied' log file and continue searching elsewhere.")
    # Add your logic here to continue the search

def search_access_denied_logs():
    print("Searching Access Denied Logs: You run a search command to find all instances of 'Access Denied' in the system logs.")
    print("After analyzing the search results, you don't find any additional useful information.")
    print("It seems like the 'Access Denied' log entry was a dead end.")
    # Add your logic here to continue the search

def search_files_directories():
    print("Searching Files and Directories: You search for any files or directories with a name resembling the decoded sequence 'GTW1983'.")
    print("After some time, you come across a hidden directory named 'GTW1983'.")
    print("Inside, you discover a program titled 'Global Thermonuclear War'.")
    print("Congratulations! You've found the hidden program.")
    # Add your logic here to interact with the program

def consult_user_manual():
    print("Consulting User Manual: You decide to consult the computer's user manual or help documentation for any references to 'G-T-W-1-9-8-3'.")
    print("After some research, you find a section in the manual that mentions 'GTW1983' as a hidden program.")
    print("The manual provides instructions on how to locate and access the program.")
    # Add your logic here to interact with the program

# Start the game
puz1()
print("Now that you've gained access to the computer's systems, you decide to look for any programs or files of interest.")
explore_file_system()
