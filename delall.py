import os

def list_directories():
    path = '/data/data/com.termux/files/home/'
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d)) and not d.startswith('.')]
    
    for idx, directory in enumerate(directories, start=1):
        print(f"[{idx}] /{directory}")
    
    print("[A] Author")
    print("[E] Exit")
    
    choice = input("Choose Input: ")
    
    if choice.isdigit() and 1 <= int(choice) <= len(directories):
        os.system(f"rm -rf {os.path.join(path, directories[int(choice) - 1])}")
    elif choice == 'A':
        print("[Blogspot](https://apkntermux.blogspot.com) {hypertext}")
    elif choice == 'E':
        print("CTRL+C")

if __name__ == '__main__':
    user_input = input("Enter 'delall' to run the program: ")
    if user_input == 'delall':
        list_directories()
