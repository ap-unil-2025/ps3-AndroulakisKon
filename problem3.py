"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        # TODO: Get input from user
        s = input("Enter a number: ").strip().lower()
        # TODO: Check if user typed 'done'
        if s =="done":
            break
        # TODO: Try to convert to float and add to list
        try:
            val = float(s)
            numbers.append(val)

        except ValueError:
            print("not a number, try again or type 'done' ")

    return numbers

                



def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None


    # TODO: Calculate count
    count = len(numbers)
    # TODO: Calculate sum
    total = sum(numbers)
    # TODO: Calculate average
    average_v = total / count
    # TODO: Find minimum
    min_v = min(numbers)
    # TODO: Find maximum
    max_v = max(numbers)
    # TODO: Count even numbers (hint: use modulo operator)
    even_count = 0
    odd_count = 0

    for x in numbers:
        if float(x).is_integer():
            xi = int()
        if xi % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    # TODO: Count odd numbers
    analysis = {"count": count,
        "sum": total,
        "average": average_v,
        "minimum": min_v,
        "maximum": max_v,
        "even_count": even_count,
        "odd_count": odd_count,}

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return

    print("\nAnalysis Results:")
    print("-" * 20)

    # TODO: Display all analysis results in a nice format
    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")
    # Example:
    # Count: 5
    # Sum: 25
    # Average: 5.00
    # etc.
    pass


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()