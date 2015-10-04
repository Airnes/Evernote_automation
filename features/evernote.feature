Feature: Displaying a list of available functions
  As an iOS developer
  I want to be able to check my resent code changes
  So I can guarantee a height quality

Scenario: As iOS user I want to be able to login in the app
  Given I am on the Welcome Screen
  Then I touch the "Authenticate" button
  And I wait for 2 seconds
  And I should see login screen
  And I scroll down to Password field
  When I enter my credentials
  And I press Sign In button
  And I authorize app
  Then I wait to see "Evernote SDK"

Scenario: As iOS user I want to be able to check my Notebooks
  Given I going to login
  And I wait for 1 seconds
  And I wait to see "List Notebooks"
  When I touch "List Notebooks"
  Then I wait to see "First Notebook"

 Scenario: As iOS user I want to be able to open Note Browser
   Given I going to login
   And I wait for 1 seconds
   And I wait to see "List Notebooks"
   When I touch "Note browser"
   Then I wait to see "Next"
