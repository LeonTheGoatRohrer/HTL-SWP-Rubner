import random

def lotto(number_range, picks):
    """
    Simulates a lottery draw by shuffling a list of numbers and swapping values.
    Returns the picked numbers.
    """
    zahlen_liste = list(range(1, number_range + 1))  # Creates a list of numbers from 1 to number_range
    random.shuffle(zahlen_liste)  # Shuffles the list in place
    pickedNumbers = []  # Initialize an empty list to store picked numbers
    for i in range(picks):
        # Pick a random index from 0 to number_range-1-i
        zufalls_index = random.randint(0, number_range - 1 - i)

        # Swap the number at zufalls_index with the number at index number_range-1-i
        zahlen_liste[zufalls_index], zahlen_liste[number_range - 1 - i] = zahlen_liste[number_range - 1 - i], zahlen_liste[zufalls_index]
        pickedNumbers.append(zahlen_liste[number_range - 1 - i])  # Append the picked number to the list

    return pickedNumbers


def statistic(pickedNumbers, frequency):
    """
    Updates the frequency of picked numbers.
    """
    for number in pickedNumbers:
        frequency[number - 1] += 1  # Increment the count for the picked number


def DisplayStatisticChart(frequency):
    """
    Displays a simple text-based chart of the frequency.
    """
    max_freq = max(frequency)
    scale = max_freq / 50  # Scale to fit in 50 characters width

    print("Zahl | Häufigkeit")
    print("-------------------")
    for i in range(len(frequency)):
        bar_length = int(frequency[i] / scale) if scale > 0 else 0
        print(f"{i + 1:>4} | {'*' * bar_length} ({frequency[i]})")


if __name__ == '__main__':
    number_range = int(input("Enter the range of numbers (e.g., 45): "))
    picks = int(input("Enter the number of picks (e.g., 6): "))
    simulations = int(input("Enter the number of simulations (e.g., 10000): "))

    frequency = [0] * number_range  # Initialize a list to count frequency of each number
    for _ in range(simulations):  # Run the simulation for the specified number of times
        pickedNumbers = lotto(number_range, picks)
        statistic(pickedNumbers, frequency)
    DisplayStatisticChart(frequency)

    print("Statistik der gezogenen Zahlen:")
    print(frequency)