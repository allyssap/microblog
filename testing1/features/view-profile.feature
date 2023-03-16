Feature: As a registered user, I want to be able to view my profile information so that I can see the details of my account.

    Scenario: User visits the profile page
        Given the user is on the profile page
        Then the page should have the text to show the username
        And the page should have a text to show the last login information
        And the page should have a text to show the followers number
        And the page should have a text to show the followings number
        And the page should have a button to modify the profile
        And the page should have a place to show the history posts

    Scenario: View profile page
        Given I am signing in to a profile
        When I click the profile button
        Then I will view my profile page