import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def display_folder_structure(path, indent=0):
    """
    Recursively display the folder structure of a given path.
    This function prints a tree-like representation of a folder and its contents,
    with directories displayed in blue and files displayed in green. Directories
    are indented by 4 spaces for each nesting level, and all items are sorted
    alphabetically by name (case-insensitive).
    Args:
        path (str or Path): The path to the folder to display. Can be a string or
            a Path object.
        indent (int, optional): The number of spaces to indent the output. Used
            internally for recursive calls to show nesting levels. Defaults to 0.
    Returns:
        None
    Raises:
        Prints an error message to the console if the specified path does not exist
        or is not a directory.
    Example:
        >>> display_folder_structure('/home/user/documents')
        documents/
            file1.txt
            subfolder/
                file2.txt
    """

    folder = Path(path)

    # Check if the specified path exists and is a directory
    if not folder.exists() or not folder.is_dir():
        print(Fore.RED + "Error: The specified path does not exist or is not a directory.")
        return

    # Print the current folder name
    print(" " * indent + Fore.BLUE + folder.name + "/")

    # Recursively display the contents of the folder
    # Sort the items in the folder by name before displaying
    for item in sorted(folder.iterdir(), key=lambda p: p.name.lower()):
        # If the item is a directory, call the function recursively to display its contents
        if item.is_dir():
            display_folder_structure(item, indent + 4)
        else:
            print(" " * (indent + 4) + Fore.GREEN + item.name )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python task3.py <absolute_folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    display_folder_structure(folder_path)




    
