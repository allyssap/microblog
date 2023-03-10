Feature: As a new user, I want to be able to register for an account so that I can access the site's features.

    Scenario: User visits the register page
        Given the user is on the register page
        Then the page should have a text field to enter the username
        And the page should have a text field to enter the email
        And the page should have a text field to enter the password
        And the page should have a text field to confirm the password
        And the page should have a button to register

    Scenario: Successful account creation
        Given I am a new user
        When I fill in a unique username in the username field
        And do the same for the email field
        And the password field
        And confirm the password
        And click the register button
        Then the account will be registered

    Scenario: Successful login
        Given I have registered an account
        When I attempt to fill in the login info
        And click the login button
        Then I will log in to my account 
        And I will view my home page