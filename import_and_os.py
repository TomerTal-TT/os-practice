import os
import re

def get_current_working_directory():
    current_path = os.getcwd()
    
    with open("file_in_python_dir.txt", "w") as file1:
        file1.write("This is a test file.")
        
    return f"Current working directory: {current_path}"

cwd = get_current_working_directory()
print(cwd)


def navigate_to_a_new_dir():
    new_path = r"C:/Users/tomer/Desktop/tmp/"  # Change this to any valid directory path
    if not(os.path.exists(new_path)):
        print(f"The dir not found: {new_path}")
        return
    os.chdir(new_path)
    
    with open("file_in_tmp_dir", "w") as file1:
        file1.write("This is a test file.")
        
    return f"Changed working directory to: {new_path}"

new_dir = navigate_to_a_new_dir()
print(new_dir)


def list_content_of_dir():
    current_path = os.getcwd() # current working path
    other_path = "C:/Users/tomer/Desktop/tmp/"  # Change this to any valid directory path
    dir_contents = os.listdir(other_path)

    for file in dir_contents:
            print(file)
    print(f"Reading content from {other_path} completed!.. ")
    return f"Contents of the directory '{other_path}': {dir_contents}"

list_dir = list_content_of_dir()
print(list_dir)


def create_new_directory():
    current_path = os.getcwd()  # current working path
    
    while True:
        new_dir_name = input("Enter the name for the new directory: ")
        new_directory_path = f'{current_path}\\{new_dir_name}' # new directory path
        
        try:
            os.mkdir(new_directory_path) # 'C:/Users/tomer/Desktop/tmp/new_folder'
            print('Directory created successfully at:', new_directory_path)
            break
        
        except FileExistsError:
            print('Directory already exists at:', new_directory_path)
            
        except Exception as error1:
            print('Error creating directory:', error1)
        
    return f"Attempted to create directory at: {new_directory_path}"

    
new_dir = create_new_directory()
print(new_dir)


def create_directories():
    current_path = os.getcwd()  # current working path
    dir1 = 'dir1'
    dir2 = 'dir2'
    
    new_directory_path = f"{current_path}\\{dir1}\\{dir2}" # new directory path
    try:
        os.makedirs(new_directory_path) # 'C:/Users/tomer/Desktop/tmp/dir1/dir2'
        print('Directories created successfully at:', new_directory_path)
        
    except FileExistsError:
        print('Directories already exist at:', new_directory_path)
        
    except Exception as error2:
        print('Error creating directories:', error2)
        
    
    return f"Attempted to create directories at: {new_directory_path}"

results = create_directories()
print(results)


def remove_directory():
    current_path = os.getcwd()  # current working path
    dir_to_remove = input('Enter the name of the directory to remove: ')
    
    dir_path = f"{current_path}\\{dir_to_remove}" # directory path to remove
    try:
        os.rmdir(dir_path) # 'C:/Users/tomer/Desktop/tmp/dir_to_remove'
        print('Directory removed successfully from:', dir_path)
        
    except FileNotFoundError:
        print('Directory does not exist at:', dir_path)
        
    except OSError as error3:
        print('Error removing directory (might not be empty):', error3)
        
    
    return f"Attempted to remove directory at: {dir_path}"

results = remove_directory()
print(results)



def execute_system_command(): 
    total_commands = [] # to store all commands executed
    
    while True:
        command_to_run = input("Enter a system command to execute: ")
        
        if command_to_run.lower() == 'q':
            print("Exiting command execution.")
            break
        
        else:
            try:
                os.system(command_to_run)  # execute the command
                total_commands.append(command_to_run) 
                
            except Exception as eroor1:
                print(f"Error executing command {command_to_run}: {eroor1}")            
        
    return total_commands

# all_commands = execute_system_command()
# print(all_commands)


#CMD inside Python:
def cmd_inside_python():
    file_to_search = input('File > ') #pass.txt
    start_path = input('Path > ') # C:/Users/tomer/Desktop

    for path, dirs, files in os.walk(start_path):
        # path = current path
        # dirs = list of directories in the current path
        # files = list of files in the current path
        if file_to_search in files:
            print(f"In path {path} there is a file named {file_to_search}")
            print(path, files)


def search_in_filenames(start_path, search_pattern):    
    for path, dirs, files in os.walk(start_path):
        for file in files:
            # re.search() finds the pattern anywhere in the filename
            try:
                
                if re.search(search_pattern, file, re.IGNORECASE): # R r - ignore case sensitivity ex: Pass/pasS
                    print(f"Found match: {os.path.join(path, file)}")
                    
            except Exception as error2:
                print(f"Error searching file {file} in path {path}: {error2}")
            

def filename():
    print('Enter file name to search for: ')
    print('Or press \'q\' to quit.')
    
    file_to_search = input('File > ') #pass.txt
    start_path = input('Path > ') # C:/Users/danc/Desktop
    search_pattern = rf"{file_to_search}"  # The regex pattern to look for
    
    if file_to_search.lower() == 'q':
        print("Exiting the search.")
    else:
        main(start_path, search_pattern)
    
    
def main(start_path, search_pattern):
    print('Welcolme.. Walking through the directory structure...')
    print('-------------------------------------------')
    search_in_filenames(start_path, search_pattern)


def tool_logic():
    options = '''
    1 - Get Current Working Directory\n
    2 - Navigate to a New Directory\n
    3- List Content of a Directory\n
    4-  Create a New Directory\n
    Press 'q' to Quit.'''
    
    print(options)

    while True:
        what_to_do = input("What do you willing to accomplish today?\nPlease insert the right number: ")
        
        if what_to_do == 'q':
            print("Exiting the tool. Goodbye!")
            break
        elif what_to_do == '1':    
            current_dir_result = get_current_working_directory()
            print(current_dir_result)
            
        elif what_to_do == '2':
            change_dir_msg = navigate_to_a_new_dir()
            print(change_dir_msg)
        elif what_to_do == '3':
            list_content = list_content_of_dir()
            print(list_content)
        elif what_to_do == '4':
            create_new_dir = create_new_directory()
            print(create_new_dir)
        else:
            print('Invalid input. Please try again.')

            

def main2():
    tool_logic()
    
    
if __name__ == "__main__":
    main2()