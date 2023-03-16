Feature: As a registered user, I want to be able to log in to my account so that I can access the site's features.

    Scenario: User visits the login page
        Given the user is on the login page
        Then the page should have a text field to enter the existing username
        And the page should have a text field to enter the existing password
        And the page should have a button to signin
        And the page should have an option allows user to register
        And the page should have an option allows user to reset password

    Scenario: Successful login
        Given I have registered an account
        When I attempt to fill in the login info
        And click the login button
        Then I will log in to my account 
        And I will view my home page