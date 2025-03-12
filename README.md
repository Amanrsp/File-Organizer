# File Organizer

A simple Python script to automatically organize files in a specified directory based on their file types.

## Features

- Organizes files into categorized folders such as **Images, Documents, Videos, Music, Archives, and Others**.
- Automatically detects file extensions and moves files accordingly.
- Ensures the target folders exist before moving files.
- Moves unrecognized files to an "Others" folder.
- Simple and easy-to-use command-line interface.

## How It Works

The script scans a given directory, identifies file types based on their extensions, and moves them into predefined folders.

### File Categories:
- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`
- **Documents**: `.pdf`, `.docx`, `.txt`, `.xlsx`, `.pptx`
- **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`
- **Music**: `.mp3`, `.wav`, `.flac`
- **Archives**: `.zip`, `.rar`, `.tar`, `.gz`
- **Others**: Any file that does not match the above categories.

## Example Usage
```
Enter the folder path where you want to organize files: /Users/John/Downloads
```
After execution, files in `/Users/John/Downloads` will be sorted into relevant folders.

## Notes
- The script **does not delete any files**, it only moves them.
- Ensure that the script has the necessary permissions to modify the target directory.

## Future Enhancements
- Add support for custom file type categories.
- GUI-based version for non-tech users.
- Option to undo file movements.
