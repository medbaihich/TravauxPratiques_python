import shutil
import os


with open("journal.txt", "w") as file:
    file.write("hi\nhow \nare you")

shutil.copy("journal.txt", "journal_copie.txt")

os.makedirs("archives", exist_ok=True)
shutil.move("journal_copie.txt", "archives/journal_copie.txt")
