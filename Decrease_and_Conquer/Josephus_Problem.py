def josephus(people, step, index=0, eliminated=None):
    #Initialize the list of eliminated people on the first call
    if eliminated is None:
        eliminated = []

    #Base case: only one person remains
    if len(people) == 1:
        print("Elimination order:", eliminated)
        print("Survivor:", people[0])
        return

    #Calculate the next person to eliminate
    index = (index + step) % len(people)

    #Add eliminated person to the list and remove them from the circle
    eliminated.append(people.pop(index))

    #Recursive call for the remaining people
    josephus(people, step, index, eliminated)

def main():
    # Get the total number of people in the circle
    n = int(input("Enter the total number of people(N): "))

    # Every k-th person will be eliminated
    k = int(input("Enter the number on which every person is selected(k): "))

    # Create a list of people numbered from 1 to n
    circle = list(range(1, n + 1))

    # Start the Josephus process with step adjusted for 0-based index
    josephus(circle, k - 1)

if __name__ == "__main__":
    main()
