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

React is a frontend framework that allows you to easily create UI components. React is technically a JavaScript library and previous javascript experience would help. It lets you compose complex UIs from small and isolated pieces of code called “components." Each components are reusable allows you to recycle previously created UIs.
