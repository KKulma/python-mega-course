my_file = open("11-file-processing/fruits.txt")
content = my_file.read()
# read the first 10 chars of the content
content10 = my_file.read(10)

my_file.close()
print(content)

### opening file with 'with'
# no need to close the file manually, it will happen automatically

with open("11-file-processing/fruits.txt") as my_file2:
    content2 = my_file2.read()

print(content2)

### writing a new file

with open("11-file-processing/veg.txt", "w") as new_file:
    new_file.write("Tomato\nOnion\nCucumber")
    new_file.write("\nAvocado")

## ASSIGNMENT
# write a function that read a file and returns the number of occurences of specified word
def read_func(character, filepath):
    with open(filepath) as file:
        content = file.read()
    return content.count(character)


read_func("apple", "11-file-processing/fruits.txt")
read_func("a", "11-file-processing/fruits.txt")


### appending text to an existing file
with open("11-file-processing/veg.txt", "a") as new_file:
    new_file.write("\nOkra")

# append a file and read it
with open("11-file-processing/veg.txt", "a+") as new_file:
    new_file.write("\nGarlic")
    new_file.seek(0)  # resets the cursor to the beginning of the fle
    new_content = new_file.read()

print(new_content)

## ASSIGNMENT
# add the current of the file two more times

# create a test file
with open("11-file-processing/exp-content.txt", "w") as new_file:
    new_file.write("1.3, 1.5")
    new_file.write("\n2.3, 2.7")

with open("11-file-processing/exp-content.txt", "a+") as new_file:
    new_file.seek(0)
    content = new_file.read()
    new_file.write("\n")
    new_file.write(content)
    new_file.write("\n")
    new_file.write(content)