Feature: As a registered user, I want to be able to edit my username so that I can change it if I have thought of a better one.
    
    Scenario: Edit username
        Given I am on my profile page
        When I click on ‘edit your profile’
        Then I can change my user name
        And when I click submit
        Then my username will be updated