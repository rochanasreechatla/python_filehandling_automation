import os
import shutil

# Read text file
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("sample.txt not found")


# Write new file
with open("output.txt", "w") as file:
    file.write("Python automation successful")

print("output.txt created")


# Read CSV file
try:
    with open("sample.csv", "r") as file:
        csv_content = file.read()
        print(csv_content)

except FileNotFoundError:
    print("sample.csv not found")


# Rename file
os.rename("output.txt", "new_output.txt")
print("File renamed")


# Create folder
if not os.path.exists("output_folder"):
    os.mkdir("output_folder")


# Move file
shutil.move("new_output.txt", "output_folder/new_output.txt")
print("File moved")


# Delete file
os.remove("output_folder/new_output.txt")
print("File deleted")


print("PROJECT COMPLETED")