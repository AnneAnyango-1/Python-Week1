#Create a file called input.txt and write at least five lines of text into it.
#Write a Python script to:
#Read the contents of input.txt.
#Count the number of words in the file.
#Convert all text to uppercase.
#Write the processed text and the word count to a new file called output.txt.
#Print a success message once the new file is created.

with open("input.txt", "r") as File:
    content = File.read()
    print(content)
    word_count = len(content.split())
    print(word_count)
    content_upper = content.upper()
    print(content_upper)

with open("output2.txt", "w") as file:
    file.write(word_count = len(content.split()), content_upper = content.upper())
    
    print("Success! The file 'output.txt' has been created with the processed text.")

try:
    with open("input.txt", "r") as file:
        print(file.read())
except:
    print("Something went wrong. File may not exist or can't be read.")


