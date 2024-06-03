
# We use a try block so that we can catch any exception that occurs when reading
# the file contents
try:
    # open the file in 'read mode' so we can read the file contents, the open 
    # function will return a file object
    file = open('file.txt', 'r')

    # the file object has a read() method that will return all the file contents
    # as a string when we call it like we do below 
    content = file.read()

    # print out the contents of the string
    print(content.rstrip('\n'))

    # close the file
    file.close()

# if an exception is raised in the try block we can handle the exception 
# with this except block
except:
    # output an error message for the user
    print("Error reading file.")
