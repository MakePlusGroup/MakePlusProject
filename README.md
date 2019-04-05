# PyScan3D
Uses data gathered from an iPad and the Structure Sensor by Occipital to classify things into their respective shapes. 
Python is required to be able to run this program.


## Table of Contents
1. [Features](#Features)
2. [Known Application Bugs](#Known-Application-Bugs)
3. [Installation](#Installation)
4. [Run the PyScan virtual environment](#Run-the-PyScan-virtual-environment)
5. [Running the PyScan Application](#Running-the-PyScan3D-Application)
6. [Troubleshooting](#Troubleshooting)



## Features:
**Mail Parser** - Log in to your email to select and download scans <br>
**Object Classifier** - Load a .obj or .ply file to classify its shape


## Known Application Bugs
- Histogram is slow to load due to tkinter limitations
- Mail parser does not show the correct errors
- If show model window is open, the main GUI window will not update until the show model window is closed
- If show model window is open,  application will not classify properly
- When the classify button is repeatedly pressed multiple times, the application will become not responding
- When classifying is processing and user clicks any button before processing is complete will cause the program to not function properly
- Prone to crash when histogram and show model window are open at the same time
- When logged into mail parser, if you leave screen or close application an error will show

## Installation:

### Install Python
Refer to the [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/) to properly configure and install Python. \
For our program, we used Python 3.6. 

### Install Git
Download Git from [here](https://git-scm.com/downloads). You will need this to clone the GitHub repository.

In a terminal window, cd to a location you want to save the repository to. Run one of the following commands:

### Clone the repository using HTTPS:
```
git clone https://github.com/emilieez/pyscan.git
```

### Clone the repository using SSH:

```
git clone git@github.com:emilieez/pyscan.git
```

### Installing Dependencies
A [virtual environment](#Run-the-PyScan-virtual-environment) is provided if the dependencies are not installed.
However, all dependencies can be installed using this command in the root folder of the repository:
#### Windows
```
pip install -r requirements.txt
```

#### Linux/MacOS
```
pip3 install -r requirements.txt
```

## Run the PyScan virtual environment
A virtual environment is provided if the dependencies are not installed, allowing you to use all of the 
libraries needed without having to install it on your computer. Keep the environment
active when running the application.
### Windows:

Run the following line in Command Prompt:
```
PyScan\Scripts\activate
```

The terminal should now look something like this:
```
(PyScan) D:\pyscan>
```
Proceed to: [Running the PyScan3D Application](#Running-the-PyScan3D-Application).

### Linux or MacOS: 

Run the following line in the terminal:
```
source /PyScan/bin/activate
```

The terminal should now look something like this:
```
(PyScan) root@localhost:~/pyscan$
```
Proceed to: [Running the PyScan Application](#Running-the-PyScan-Application).

### Deactivate the Virtual Environment
To terminate the application, you will need to deactivate the virtual environment.<br>
To deactivate, type:
```
PyScan\Scripts\deactivate
```
or on Linux/MacOS:
```
deactivate
```

## Running the PyScan Application
In the root folder of the repository type:
```
python pyscan.py
```

## Using PyScan

### Main Screen

<img src="https://raw.githubusercontent.com/BCIT-MakePlus/pyscan/master/screenshots/main_screen.png" width="400" height="400" />

### Downloading Scans

<img src="https://raw.githubusercontent.com/BCIT-MakePlus/pyscan/master/screenshots/download_screen.png" width="400" height="400" />

##### Once the scans have been sent to your email from the iPad, you can directly download the file here.
##### Currently, only Gmail and Outlook are supported for this application.


### Classify the downloaded scans

<img src="https://raw.githubusercontent.com/BCIT-MakePlus/pyscan/master/screenshots/classify_results_screen.png" width="400" height="400" />

##### This allows you to load in a single .obj or .ply file to compare it to the data saved in the object_data.csv file.

##### Click the "Classify" button to see how well the loaded file matches the stored data.

##### Click the "Show Model" button to view the file.

##### Click the "Show Comparison" button to visualize the classification output. 

### Show Model

<img src="https://raw.githubusercontent.com/BCIT-MakePlus/pyscan/master/screenshots/Show_Model.png" position="relative" width="800" height="400" />

##### Press 'W' to switch to wireframe view (right image)

### Show Comparison

<img src="https://raw.githubusercontent.com/BCIT-MakePlus/pyscan/master/screenshots/show_comparison_screen.png" width="400" height="400" />

##### The blue colored histogram is the data stored in the object_data.csv.

## Troubleshooting

Refer to [Known Application Bugs](#Known-Application-Bugs) if the problem is not listed here.

### 1.) The system cannot find the path specified.
Ensure you are in the root folder. This is the main folder that houses all the files. 
If you cloned from GitHub, the root/main folder is called pyscan.

### 2.) Missing Dependencies
Install a dependency using this command:

#### Windows
```
pip install <dependency name>
```

#### Linux/MacOS
```
pip3 install <dependency name>
```

Alternatively, all dependencies can be reinstalled: [Installing Dependencies](#Installing-Dependencies)