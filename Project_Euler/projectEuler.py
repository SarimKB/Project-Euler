# List keeping track of all the problems completed
allProbList = ["1. Multiples of 3 and 5",
    "2. Even Fibonacci numbers"
    ]

# Problem 1
def multiplesOf3And5():
    multiples = []

    for x in range(3, 1000):
        if( (x % 3 == 0) or (x % 5 == 0) ):
            multiples.append(x)

    num_sum = sum(multiples)

    print(f"The sum of all multiples of 3 or 5 below 1000 is {num_sum}")

# Problem 2
def evenFibonacciNums():
    f0 = 1
    f1 = 2
    evenFibArr = [f1]
    x = 0

    while(x < 4000000):
        x = f0 + f1
        f0 = f1
        f1 = x
        if(x % 2 == 0):
            evenFibArr.append(x)
    
    even_sum = sum(evenFibArr)

    print(f"The sum of even valued Fibonacci terms under 4,000,000 is {even_sum}")


# MAIN
def main():
    print("\nWelcome to Project Euler\n")
    print("Problems:")
    for prob in allProbList:
        print(prob)

    user_in = input()
    option = {
        '1': multiplesOf3And5,
        '2': evenFibonacciNums
    }
    option[user_in]()

# Main execution
if __name__ == '__main__':
    main()