# MDX-Food-Safety-Hackathon
This repository is a part of my submission for the Food Safety Hackathon organized by Middlesex University,Dubai.

There are 4 parts to my submission:

Part 1: EDA

Part 2: Logistic Regression model

Part 3: Automating alert cases as whatsapp messages

Part 4: Deploying the logistic regression model on a web app (Link here: https://alert-model.herokuapp.com/)

## Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

## Repository Structure
This repository has four major parts :

MDX Hackathon - Github.ipynb - This contains the Jupyter notebook for Exploratory Data Analysis, Logistic Regression which will predict which cases are "Alert" and by what probability. This file also contains the automation of sending alert cases as whatsapp notification using Twilio API and python.

app.py - This contains Flask APIs that receives user input details through our website, computes the precited value based on our model and returns it.

templates - This folder contains the HTML template to allow user to enter case details and display if the case is an alert case or not.

Procfile - tells Heroku what kind of app you are running and how to serve it to users.

requirements.txt - this tells Heroku which packages to install for your web app.

MDX Hackathon.pkl - this contains our trained classifier model which we saved to disk using pickle. It can then be reloaded later on and used exactly as if we had trained it.
