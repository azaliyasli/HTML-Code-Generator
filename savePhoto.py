from msConnection import conn, cursor 

title = input("Photo title: ")
description = input("Photo description: ")
choice = input("""1: Link 
OR
2: File 
""")

photo_url = None
photo_file = None

if choice == "1":
    photo_url = input("Enter the photo URL: ")
elif choice == "2":
    file = input("Enter the file path: ")
    with open(file, "rb") as f:
        photo_file = f.read()
else:
    print("Invalid choice!")

#Save to database
cursor.execute("""
    INSERT INTO photos (title, description, photo_url, photo_file, created_at)
    VALUES (%s, %s, %s, %s, NOW())
""", (title, description, photo_url, photo_file))

conn.commit()
cursor.close()
conn.close()

print("Photo has been saved succesfully!")