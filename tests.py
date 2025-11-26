from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

# FOR TESTING get_files_info
# print(get_files_info("calculator", "."))
# print(" ")
# print(get_files_info("calculator", "pkg"))
# print(" ")
# print(get_files_info("calculator", "/bin"))
# print(" ")
# print(get_files_info("calculator", "../"))
# print(" ")

# FOR TESTING get_file_content
# print(get_file_content("calculator","lorem.txt"))
print(get_file_content("calculator", "main.py"))
print(" ")
print(get_file_content("calculator", "pkg/calculator.py"))
print(" ")
print(get_file_content("calculator", "/bin/cat"))
print(" ") 
print(get_file_content("calculator", "pkg/does_not_exist.py")) 