# DRF SheCodes Project - {{Name of }} - Crowdfunding website
by Tracey Nguyen
- She Codes crowdfunding project - DRF Backend.

## About
{{ A paragraph detailing the purpose and target audience for your website. }}

## Features
{{ The features your MVP will include. (Remember this is a working document, you can change these as you go!) }}
* [] User can Login/Logout 
    - [X] Username
    - [X] Email
    - [X] Password
    - [ ] Image
    - [ ] Bio

* [X] User can change account profile details

            
* [X] User can create, edit, display a project
    - [X] Title
    - [X] Owner (a user)
    - [X] Description
    - [X] Image
    - [X] Target amount to fundraise
    - [X] Whether it is currently open to accepting new supporters or not 
    - [X] When the project was created (auto filled on initial creation)
    - [X] When the project was changed (auto filled on create/update)
    - [X] When the project ends (user defined)
    - [X] User can edit project if they are the owner of the project    
    - [ ] School Name
    - [ ] Website

* [] User can make a Pledge
    - [X] An amount
    - [X] The project the pledge is for
    - [X] The supporter/user (i.e. who created the pledge)
    - [ ] Whether the pledge is anonymous or not
    - [X] If the supporter is not the project owner, pledge can be created
           - [X] If the project is not currently open, pledge cannot be created               
    - [X] A comment to go along with the pledge
    - [X] User can Change pledge if the project is open and they are the supporter   
    - [X] User can delete pledge if the project is open and they are the supporter       
    - [ ] Other??


### Stretch Goals
{{ Outline three features that will be your stretch goals if you finish your MVP }}

* [X] Display statistics on the home page # projects, pledges, $
* [] Add categories for projects
* [] Search project based on categories or title/description
* [] Change currency/language
* [] Remind me
* [] Like / Dislike
* [] Percentage funded - display as graph
* [] Days to go/ left for deadline
* [] Last donation



## API Specification

| HTTP Method | URL | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization |
| :---: | :--- | :--- | :--- | :---: | :--- |
| GET | projects/ | Return all projects | N/A | 200 | N/A |
| POST | projects/ | Create a new project | Project object | 201 | User must be logged in. |
| GET | projects/1/ | Return the project with ID of "1" | N/A | 200 | N/A |
| PUT | projects/1/ | Update the project with ID of "1" | Project object | 200 | User must be logged in.<br> User must be the project owner |
| GET | pledges/ | Return all pledges | N/A | 200 | N/A |
| POST | pledges/ | Create a new pledge | Pledge object | 201 | User must be logged in.<br> User must not be the owner of the project<br>Project must be open|
| GET | pledges/1/ | Return the pledge with ID of "1" | N/A | 200 | N/A |
| PUT | pledges/1/ | Update the pledge with ID of "1" | Pledge object | 200 | User must be logged in.<br> User must be the pledge owner<br>Project must be open |
| DELETE | pledges/1/ | Deletes the pledge with ID of "1" | Project object | 200 | User must be logged in.<br> User must be the pledge owner<br>Project must be open |
| POST | users/ | Create a new user | User object | 201 | N/A |
| GET | users/1/ | Return the user with ID of "1" | User object | 200 | User must be logged in |
| PUT | users/1/ | Update the user with ID of "1" | User object | 200 | User must be logged in |

## Database Schema
{{ Insert your database schema }}

![image info goes here](./docs/image.png)

## Wireframes
{{ Insert your wireframes }}

![image info goes here](./docs/image.png)

## Colour Scheme
{{ Insert your colour scheme }}

![image info goes here](./docs/image.png)

## Fonts
{{ outline your heading & body font(s) }}

## Submission Documentation
{{ Fill this section out for submission }}

Deployed Project: [Deployed website](http://linkhere.com/)

### How To Run
{{ What steps to take to run this code }}
get/post end url what is the json body

### Updated Database Schema
{{ Updated schema }}

![image info goes here](./docs/image.png)

### Updated Wireframes
{{  Updated wireframes }}

![image info goes here](./docs/image.png)

### How To Register a New User
{{ Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data). }}

### Screenshots
* [] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
![image info goes here](./docs/image.png)

* [] A screenshot of Insomnia, demonstrating a token being returned.
![User token](./docs/image.png)

