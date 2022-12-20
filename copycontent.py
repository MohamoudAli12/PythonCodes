
new_file = open("string.docx", "wb")  # copy to this file
with open("value.txt", "rb") as f:   #copy from this file
    new_file.write(f.read())
new_file.close()
