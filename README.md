# Bungalow Take Home Project for Backend Developer Role

## About This Project

This is a Django based assignment. We have created a base project for you to work from.
You are free to vary from our original base if you would like to. We provide it with the intention of providing
a common base for all candidates to work from and to hopefully save you a bit of time.

If you need an introduction to Django, their docs are an excellent place to start: https://docs.djangoproject.com/en/3.2

We encourage you to use the Django Rest Framework for developing your API. This is a framework that we use extensively
at Bungalow, and it provides some nice functionality out of the box. https://www.django-rest-framework.org/

## What to Build

We would like you to build an API that can be used to query some information about houses.
Sample data is provided in the `sample-data` folder.
We have provided the stub for a Django command to import the data. Finish writing this code.
You should use Django's ORM to model the data and store it in a local database.
Then, utilize the Django Rest Framework to provide an API to query the models.
A very basic API design here would simply return all of the data available.
You can choose to improve and refine this very basic API design, and we encourage you to do so.
This will give us an opportunity to see how you approach API design.
If you are running out of time, you can outline how you would have done things differently given more time.

## How Will This Be Evaluated

We will use this project as our basis for our evaluation of your coding skill level as it relates to our team.
To do this, we will review your code with an eye for the following:

- Design Choices - choice of functionality, readability, maintainability, extendability, appropriate use of language/framework features
- Does it work as outlined
- Testing - have you considered how you'd test your code?
- Documentation - have you provided context around decisions and assumptions that you have made?
- Polish - have you produced something that would be ready to go into a production system?
  if not, have you clearly stated what would be needed to get from where it is to that level of polish?

## Time Expectations

We know you are busy and likely have other commitments in your life, so we don't want to take too much of your time.
We don't expect you to spend more than 2 hours working on this project. That being said, if you choose to put more or
less time into it for whatever reason, that is your choice. Feel free to indicate in your notes below if you worked on
this for a different amount of time and we will keep that in mind while evaluating the project. You can also provide us
with additional context if you would like to. Additionally, we have left a spot below for you to note. If you have ideas
for pieces that you would have done differently or additional things you would have implemented if you had more time,
you can indicate those in your notes below as well, and we will use those as part of the evaluation. For example, if you
would have tested more, you can describe the tests that you would have written, and just provide 1 or 2 actual implemented
tests.

## Public Forks

We encourage you to try this project without looking at the solutions others may have posted. This will give the most
honest representation of your abilities and skills. However, we also recognize that day-to-day programming often involves
looking at solutions others have provided and iterating on them. Being able to pick out the best parts and truly
understand them well enough to make good choices about what to copy and what to pass on by is a skill in and of itself.
As such, if you do end up referencing someone else's work and building upon it, we ask that you note that as a comment.
Provide a link to the source so we can see the original work and any modifications that you chose to make.

## Setup Instructions

1. Fork this repository and clone to your local environment. If you make your fork private, please give access to the `bungalow-engineering` user.
1. Install a version of Python 3 if you do not already have one. We recommend Python 3.8 or newer.
1. You can use the built-in virtual environment creation within Python to create a sandboxed set of package installs.
   If you already have a preferred method of virtualenv creation, feel free to proceed with your own method.
   `python -m venv env`
1. You will need to activate your virtual environment each time you want to work on your project.
   Run the `activate` script within the `env/bin` folder that was generated.
1. We have provided a `requirements.txt` file you can use to install the necessary packages.
   With your virtualenv activated run: `pip install -r requirements.txt`
1. To run the django server run `python manage.py runserver`
1. To run the data import command run `python manage.py import_house_data`
1. You are now setup and ready to start coding.

# Your Notes

## Time Spent

I spent around 3.5 to 4 hours on this project. I had never used Django prior to completing this project so part of that time was spent following a tutorial on Youtube for creating a REST API using Django and also going through the Django REST framework documentation.

## Assumptions

Most of the assumptions I had to make were about the data and how it would be used by a client. This influenced how I designed the House model. I determined what fields are required by the database to be not null by making assumptions about what information would be essential to a house listing. My assumptions about the data also influenced what types I chose for different fields in the House model. For example, I decided to convert the price field from data.csv from a string to a float because I assume that the client may want to retrieve data ordered by price at some point and having the price as a float in the database would make it easier to order data in that way.

## Next Steps

### Features

If I had more time I would add more input validation to the routes. For example, I would ensure that the value provided for the 'link' field is actually a link. I would do something similar for other fields such as address, state, zipcode, etc. The other thing I would do is add pagination to the GET /api/houses route so that you don't have to load hundreds of houses at once when fetching from that route.

### Testing

I added two test modules: one for the GET /api/houses route and one for the GET /api/houses/{pk} route. If I had more time I would add test modules for the other three routes I created and I would add more test cases to each module that focus on edge cases such as when the payload is missing required fields. I would also add some test cases for the import_house_data command.

### Anything else needed to make this production ready?

## How to Use

To populate the database, you can run the following command from the listings directory: `python3 manage.py import_house_data --path='../sample-data/data.csv`
