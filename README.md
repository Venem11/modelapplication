# ApplyToModel - Descriptions, current functionality, and changelog 

## Description

This website is to be used for applications for ApplyToModel, and event management (e.g. event creation, event reminders, push notification for events that users have subscribed to etc)

## Current Functionality 

### Applications

Current user setup allows for information about the user's application to be stored within the user profile, no other funcionality so far, working on the HTML for the main applicatoin front

### Events

This portion has not been started yet, please refer to changelog for updates on when this section gets started

## Changelog 

### 21/03/2023

Initialised the django project, and done hand drawings of designs for the website, and started a bootstrap file to create the templates ready for the website to streamline deployment 

Applied some admin functions that require a real name and date of birth, and changed the sign up form on the admin side 

Added in comments all over the code to remind myself what lines of code do 

I have started to create the photo's field, one will be required upon sign up

### 29/03/2023

Created function in models (implimented in views) to create an object using a function, this will be initialised in the website quite alot

Added HTML for the Admin Views (only the dashboard) just so that admins can see the applications easier without having to trapse into the django admin views (so then django admin views are maintenance only)

### 03/04/2023

Edited User model to ensure that the bio is able to be edited at the user's will edit 

Added the event model, without the venue and the hotel fields (these will be added once the models have been made)