def get_cats_info(path):
    """
    Read cat information from a file and return as a list of dictionaries.
    This function reads a file containing cat data where each line contains
    comma-separated values representing cat id, name, and age. Each line is parsed
    and converted into a dictionary with keys 'id', 'name', and 'age'.
    Args:
        path (str): The file path to the cat data file
    Returns:
        list: A list of dictionaries, where each dictionary contains:
            - 'id' (str): The cat's unique identifier
            - 'name' (str): The cat's name
            - 'age' (str): The cat's age
        Returns an empty list if the file is not found or an error occurs.
    Raises:
        No exceptions are raised. Errors are caught and printed to console.
    """

    cats_result = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_info = line.strip().split(",")
                cats_result.append({
                    "id": cat_info[0],
                    "name": cat_info[1],
                    "age": cat_info[2]
                })

        return cats_result
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except Exception as e:
        print(f"An unknown error occurred: {e}")
        return []


cats_info = get_cats_info("task2/cats_file.txt")
print(cats_info)