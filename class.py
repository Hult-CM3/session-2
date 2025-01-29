"""def get_number():
    while True:
        try:
            n = int(input("What's n? "))
            if n > 0:
                return n
        except ValueError:
            print("Invalid input. Please enter a number.")

def meow(n):
    for _ in range(n):
        print("meow")

def main():
    meow(get_number())

if __name__ == "__main__":
    main()