Feature: As a new user, I want to be able to register for an account so that I can access the site's features.

    Scenario: Successful account creation
        Given I am a new user
        When I fill in a unique username in the username field
        And do the same for the email field
        And the password field
        And confirm the password
        And click the register button
        Then the account will be registered