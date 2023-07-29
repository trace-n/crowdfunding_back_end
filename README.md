# DRF SheCodes Project - {{Name of }} - Crowdfunding website
by Tracey Nguyen
- She Codes crowdfunding project - DRF Backend.

## About
{{ A paragraph detailing the purpose and target audience for your website. }}

## Features
{{ The features your MVP will include. (Remember this is a working document, you can change these as you go!) }}
* [] User can Login/Logout 
    - [ ] Username
    - [ ] Email
    - [ ] Password
    - [ ] Image
    - [ ] Bio
            
* [] User can create, edit, display a project
    - [ ] Title
    - [ ] Owner (a user)
    - [ ] Description
    - [ ] Image
    - [ ] Target amount to fundraise
    - [ ] Whether it is currently open to accepting new supporters or not
    - [ ] When the project was created
    - [ ] When the project ends
    - [ ] School Name
    - [ ] Website


* [] User can make a Pledge
    - [ ] An amount
    - [ ] The project the pledge is for
    - [ ] The supporter/user (i.e. who created the pledge)
    - [ ] Whether the pledge is anonymous or not
    - [ ] A comment to go along with the pledge
    - [ ] Other
        
* [] User can display/change/cancel Pledge
* [] User can load avatar image and images related to project



### Stretch Goals
{{ Outline three features that will be your stretch goals if you finish yo*ur MVP }}

* [] Display statistics on the home page # projects, pledges, $
* [] Add categories for projects
* [] Search project function
* [] Change currency/language
* [] Remind me
* [] Like / Dislike
* [] Percentage funded
* [] Days to go/left for deadline
* [] Last donation



## API Specification

| HTTP Method | Url | Purpose | Request Body | Successful Response Code | Authentication <br /> Authorization
| --- | ------- | ------ | ---- | -----| ----|*
| GET | projects/ | Return all projects | N/A | 200 | N/A |
| POST | projects/ | Create a new project | project object | 201 | User must be logged in. |

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
![image info goes here](./docs/image.png)
