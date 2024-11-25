import sys
file_name = input("File name: ").strip()
file_name = file_name.lower()

#name, extension = file_name.split('.', 1)

if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".png"):
    print("image/png")
elif file_name.endswith(".txt"):
    print("text/plain")
elif file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
    print("image/jpeg")
elif file_name.endswith(".pdf"):
    print (f"application/pdf")
elif file_name.endswith(".zip"):
    print (f"application/zip")
else:
    print("application/octet-stream")
