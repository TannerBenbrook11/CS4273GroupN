# CS4273 Capstone Project Group N

## Project Description:
The goal of this project is to track power consumption of servers and switches on the OSCAR supercomputer in real-time and predict future power consumption for planning.

## Project Tasks:
Data Collection (Task 1): Develop a script that can periodically gather power consumption data on hundreds of different switches and servers on the OSCAR supercomputer.

Data Preperation (Task 2): Develop software to clean, normalize, format and transform data for modeling, and provide documentation of the data transformation process.

Data Modeling (Task 3): Develop software to model the transformed data to predict future power consumption. This software will highlight the tradeoff of computational expenses and training error.

Model Testing (Task 4): Compare predicted value from the model with actual value along with the level of accuracy.

## Technologies and Tools: 
Python is an essential programming language to use in this project. Python's flexibility to read in data from multiple different file types makes this a good candidate. There are many different libraries 
in Python that help with data extraction, such as the built in csv module or pandas. Since data from OSCAR can be presented in different formats, using Python's built in re library for regular expressions 
allows for complex pattern matching in raw text files.

React is a frontend framework that allows you to easily create UI components. React is technically a JavaScript library and previous javascript experience would help. It lets you compose complex UIs from small and isolated pieces of code called “components." Components are reusable which allows you to recycle previously created UIs.

Since this project will be using React as a frontend and Python for the backend and data handling, there needs to be a way for these two things to communicate. There are many different ways to do this, like using flask or fastAPI to create a REST API that can read data from this .csv file and give this data to the React frontend. REST is essentially a way for a frontend tool like React to communicate with a backend tool like Python over HTTP. It uses HTTP commands such as GET, POST, PATCH, and DELETE.

## Key Feature for Unit Testing
A key feature pertaining to this project is related to Data Collection. Since the data that we will be reading in is from a standard format file, test cases checking file handling in python is a good first step.

## Goals and Project Timeline:
Progress report 1 (Feb. 14th): Finish Task 1 and all testing related to Task 1.
Progess report 2 (Mar. 7th): Finish Task 2 and all testing related to Task 2.
Progress report 3 (Apr. 11th): Finish Task 3 and all testing related to Task 3.
Progess report 4 (May 2nd): Finish Task 4 and all testing related to Task 4.
