

# Writing code for a file organizer in python.

# Importing the required libraries.
import os #os module
import shutil 

# Verifiying if the directory exists
def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory path doesn't exist. Provide a valid path")
        return
# Using disctionaries to store file types and its extensions. 
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov"],
        "Music": [".mp3", ".wav", ".flac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Others": []  
    }
    # Using os.path() to establish complete path of the file
    for category in file_types.keys():
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):  
            os.makedirs(folder_path)
    
    # Visiting each file in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name) 
        if os.path.isfile(file_path):
            moved = False 
     # Checking the category of extension to which the file belongs to
            for category, extensions in file_types.items():
                if any(file_name.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(directory, category, file_name))
                    moved = True
                    break  

            # If file does not match any aforemention extensions, move it to "Others"
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", file_name))

    print("Organization of files are done")

# Main function to run the script
def main():
    directory = input("Enter the folder path where you want to organize files: ")
    organize_files(directory)

# If you want to execute the file directly
if __name__ == "__main__":
    main()
