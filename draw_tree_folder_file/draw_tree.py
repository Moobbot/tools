import os
from pathlib import Path


def list_files(directory):
    # Function to check if a path is ignored by gitignore rules
    def is_ignored(path):
        gitignore_path = Path(path)
        while gitignore_path != gitignore_path.parent:
            gitignore_path = gitignore_path.parent
            gitignore_file = gitignore_path / '.gitignore'
            if gitignore_file.exists():
                with open(gitignore_file, 'r') as f:
                    gitignore_content = f.read().splitlines()
                    for pattern in gitignore_content:
                        if pattern.startswith("#") or pattern.strip() == "":
                            continue
                        if Path(path).match(pattern):
                            return True
        return False

    # Recursive function to list files in directory
    def list_files_recursively(directory, indent=''):
        file_list = []
        for root, dirs, files in os.walk(directory):
            # Filter out ignored files and directories
            dirs[:] = [d for d in dirs if not is_ignored(
                os.path.join(root, d))]
            files = [f for f in files if not is_ignored(os.path.join(root, f))]
            # Add remaining files to the list
            for f in files:
                print(indent + '|- ' + f)
                output_file.write(indent + '|- ' + f + '\n')
            for d in dirs:
                print(indent + '- ' + d)
                output_file.write(indent + '- ' + d + '\n')
                file_list.extend(list_files_recursively(
                    os.path.join(root, d), indent + '  '))
        return file_list

    return list_files_recursively(directory)


# Replace 'your_directory' with the directory you want to list files from
directory = os.getcwd()
with open('directory_tree.txt', 'w') as output_file:
    output_file.write(directory + '\n')
    files = list_files(directory)