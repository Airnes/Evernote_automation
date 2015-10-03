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