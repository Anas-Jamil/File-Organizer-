# File Organizer

## Overview

**File Organizer** is a simple Python script that automatically organizes files in your `Downloads` directory by moving them into folders based on their file extensions. This script helps keep your Downloads folder tidy by categorizing files like images, documents, and executables into their respective folders.

## Features

- Automatically creates folders for specified file extensions.
- Moves files into corresponding folders based on their extension.
- Easily customizable to add or remove file types.

## Requirements

- Python 3.x

## Installation

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Anas-Jamil/File-Organizer-.git
cd File-Organizer-
```

### Step 2: Ensure Python is Installed
Make sure Python 3.x is installed on your system. You can check by running:
```bash
python --version
```

## Usage

### Step 1: Place the Script in Your Downloads Folder
Copy the organizer.py script to the Downloads directory you want to organize, or specify a different directory by modifying the target_destination variable in the script.


### Step 2: Run the Script
```bash
python organizer.py
```

### Step 3: View the Organized Files
After running the script, your Downloads folder will be organized into subfolders based on the file extensions you specified.


## Customization
You can customize the list of extensions that the script organizes by modifying the specified_extensions list in the organizer.py file:
```python
specified_extensions = ['jpg', 'png', 'txt', 'pdf', 'docx', 'zip', 'jar', 'exe']
```

## Contributing
If you want to contribute to this project, feel free to fork the repository and submit a pull request. Contributions such as bug fixes, new features, and documentation improvements are welcome.




