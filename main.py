url = input("Guess the URL: ")

while True:
    if url.startswith('b'):
        print("You have access to the backrooms. You are now infinitely stuck.")
        exit_sequence = input("Enter the exit sequence to leave the backrooms: ")
        if exit_sequence == "exit":
            print("You have left the backrooms.")
            break
        else:
            print("Still stuck. Keep searching for the exit sequence.")
    elif url == "google.com":
      print(" You gained access to the internet.")
      break
    else:
        print("Access denied")
        break