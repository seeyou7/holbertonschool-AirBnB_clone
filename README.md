# AirBnB Clone Command Interpreter

## Background Context

The console is the initial segment of the AirBnB project at Holberton School, aiming to cover fundamental concepts of higher-level programming. The overarching goal of the AirBnB project is to deploy a server, essentially creating a simplified copy of the AirBnB website (HBnB). In this segment, a command interpreter is developed to manage objects for the AirBnB (HBnB) website.

## Welcome to the AirBnB Clone Project! (The Holberton B&B)

### Project Overview

#### First Step

The primary objective is to write a command interpreter to manage AirBnB objects. This is a crucial step towards building the complete web application, covering HTML/CSS templating, database storage, API, and front-end integration in subsequent projects.

### Task List

1. Implement a parent class (BaseModel) to handle the initialization, serialization, and deserialization of future instances.
2. Create a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> file.
3. Develop classes for AirBnB objects (User, State, City, Place) that inherit from BaseModel.
4. Establish the first abstracted storage engine for the project: File storage.
5. Create unit tests to validate all classes and the storage engine.

#### What's a Command Interpreter?

Similar to the Shell but tailored to a specific use-case, the command interpreter allows the management of project objects. It facilitates:

- Creating new objects (e.g., User, Place).
- Retrieving objects from files or databases.
- Performing operations on objects (count, compute stats, etc.).
- Updating attributes of an object.
- Destroying an object.

## Installation

Clone this repository in your terminal:

```bash
$ git clone https://github.com/seeyou7/holbertonschool-AirBnB_clone.git
$ git clone https://github.com/Aicha-ch/holbertonschool-AirBnB_clone.git
$ cd AirBnB_clone


##Execution

In interactive mode:

$ ./console.py
(hbnb) help

Non-interactive mode:

$ echo "help" | ./console.py
(hbnb)


##Examples
Create a file named "test_base_model.py" in the AirBnB_clone directory with the provided code.

Grant execution permissions:


$ chmod u+x test_base_model.py

Execute the file:

$ ./test_base_model.py


The expected output:

[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'Holberton', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}
{'my_number': 89, 'name': 'Holberton', '__class__': 'BaseModel', 'updated_at': '2017-09-28T21:05:54.119572', 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119427'}
JSON of my_model:
    my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - Holberton
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427


Feel free to explore and enhance the AirBnB clone project. If you have any questions or need assistance, don't hesitate to reach out!

made by: Aicha CHOUIKHI & Younes SABER. 
