# main.py

def greet(name):
    return f"Hello, {name}!"

def main():
    user_name = input("Enter your name: ")
    message = greet(user_name)
    print(message)

if __name__ == "__main__":
    main()
