def total_salary(path):
    """
    Calculate the total and average salary from a file.
    This function reads a file where each line contains developer information
    with salary data. It parses the salary values and computes both the total sum
    and average salary across all developers.
    Args:
        path (str): The file path to the file containing developer salary data.
    Returns:
        tuple: A tuple containing:
            - total (int): The sum of all salaries from the file.
            - average (int): The average salary rounded down to the nearest integer.
            Returns (0, 0) if the file is not found or an error occurs.
    Raises:
        FileNotFoundError: Handled internally. If the file is not found, prints
                           an error message and returns (0, 0).
        Exception: Catches any other exceptions that may occur, prints an error message, 
                   and returns (0, 0).
    """

    try:
        with open(path, 'r', encoding="utf-8") as file:
            # Read all lines from the file
            lines = file.readlines()
            total = 0
            number_of_developers = 0

            for line in lines:
                if line.strip():
                    salary = int(line.strip().split(',')[1])
                    total += salary
                    number_of_developers +=1
            
            # Calculate average salary
            average = total / number_of_developers if number_of_developers > 0 else 0

            return (total, int(average))
    except FileNotFoundError:
        print("File not found.")
        return 0, 0
    except Exception as e:
        print(f"An unknown error occurred: {e}")
        return 0, 0
    


total, average = total_salary("task1/salary.txt")
print(f"Total salary: {total}, Average salary: {average}")