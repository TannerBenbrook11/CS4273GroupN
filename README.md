# CS4273 Capstone Project Group N

## Project Overview

### Group Members

- Dylan Zemlin - Product Owner
- Tanner - Quality Assurance
- Ben Yokell - Sprint Master 1
- Ameer Ghazal - Sprint Master 2
- Xin Lai - Sprint Master 3
- Sahil Tamboli - Sprint Master 4

### Description:
The goal of this project is to track power consumption of servers and switches on the OSCAR supercomputer in real-time and predict future power consumption for planning.

### Tasks:
Data Collection (Task 1): Develop a script that can periodically gather power consumption data on hundreds of different switches and servers on the OSCAR supercomputer.

Data Preparation (Task 2): Develop software to clean, normalize, format and transform data for modeling, and provide documentation of the data transformation process.

Data Modeling (Task 3): Develop software to model the transformed data to predict future power consumption. This software will highlight the tradeoff between computational expenses and training error.

Model Testing (Task 4): Compare the predicted value from the model with the actual value along with the level of accuracy.

### Technologies and Tools: 
Python is an essential programming language to use in this project. Python's flexibility to read in data from multiple different file types makes this a good candidate. There are many different libraries in Python that help with data extraction, such as the built in csv module or pandas. Since data from OSCAR can be presented in different formats, using Python's built in re library for regular expressions allows for complex pattern matching in raw text files.

React is a frontend framework that allows you to easily create UI components. React is technically a JavaScript library and previous javascript experience would help. It lets you compose complex UIs from small and isolated pieces of code called “components." Components are reusable which allows you to recycle previously created UIs.

Since this project will be using React as a frontend and Python for the backend and data handling, there needs to be a way for these two things to communicate. There are many different ways to do this, like using flask or fastAPI to create a REST API that can read data from this .csv file and give this data to the React frontend. REST is essentially a way for a frontend tool like React to communicate with a backend tool like Python over HTTP. It uses HTTP commands such as GET, POST, PATCH, and DELETE.

### Key Feature for Unit Testing
A key feature pertaining to this project is related to data collection. Since the data that we will be reading in is from a standard format file, test cases checking file handling in python is a good first step. We will also be testing a very basic data normalization technique, as we will be receiving data in various formats from the super computers devices.

### Goals and Project Timeline:
Progress report 1 (Feb. 14th): Finish Task 1 and all testing related to Task 1.

Progress report 2 (Mar. 7th): Finish Task 2 and all testing related to Task 2.

Progress report 3 (Apr. 11th): Finish Task 3 and all testing related to Task 3.

Progress report 4 (May 2nd): Finish Task 4 and all testing related to Task 4.

## Installation and Building

### Installing Python

Our code was tested and ran on Python 3.11.9. You can download this verison, and others, from the [Python Website](https://www.python.org/downloads/). We cannot guarantee results on any other version of python. Note, depending on your operating system and how it installs python you may have to use the standard `python` command to invoke python instead of `python3`.

### Create a virtual environment

Before you get started, it is standard practice to create a virtual environment for each project you are working on. To do that, run the following command while in the root directory of the project
```bash
# Create a virtual environment in the .venv directory
python3 -m venv .venv
```

Then activate your virtual environment. This will depend on your operating system, but the following two should work for Windows and Linux respectively
```bash
# Windows
./.venv/Scripts/activate.bat

# Linux
source .venv/bin/activate
```

### Installing Dependencies

To install dependencies, use the included `requirements.txt` file which will include all dependencies needed to run our project. To install them, run the following command while in the root directory of the project
```bash
# Install all dependencies from requirements.txt
python3 -m pip install -r requirements.txt
```

### Running Unit Tests

To run all of our unit tests, simply run the following command while in the root directory of the project
```bash
# Run all unit tests
python3 -m unittest discover -s tests -v
```

The `discover` argument allows unittest to discover tests, the `-s` flag tells it which directory to search in, and the `-v` flag enables more verbose output.

### Running the Application

There is currently no application to run yet.
