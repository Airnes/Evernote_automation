Feature: Login to Evernote

@Android	
Scenario: As a valid user I want to be able to login in the App
	Given user on the Welcome screen
	When I click on the Sign In button
	Then Login Screen should be presented
	When I enter my Valid credentials
	When I touch Sing In button
	Then I should see All my Notes
	Then I reset my App

@Android
Scenario: As a logged in user I should be able to create a Note
	Given I going to login on Android
	When I touch Plus button
	Then I should be able to write my Text Note
	When I entered my Note
	Then I should be able to save it
	Then I reset my App

@Android
Scenario: As a logged in user I should be able to retrive saved Note
	Given I going to login on Android
	Then I should see my saved Note
	When I touch one of saved Notes
	Then I should see it

@iOS
Scenario: As iOS user I want to be able to login to the Evernote
	Given I tap Authenticate button to authorise user
	Then I need to enter my credentials
	Then I reset my App

@iOS
Scenario: As iOS user I want to be able to check my Notebooks
	Given I going to login on iOS
	When I touch List of Notebooks
	Then I should see a my First Notebook
	Then I reset my App

@iOS
Scenario: As iOS user I want to be able to check my Notes
	Given I going to login on iOS
	When I touch Note Browser
	Then I should see a Browser with Notes