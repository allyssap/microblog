Feature: As a registered user, I want to be able to edit my profile’s ‘about me’ so I can personalize it for those who search me up.
    
    Scenario: About me edited
        Given I am on profile page
        When I click ‘edit profile’
        Then change the text in the about me text box
        And click submit
        Then my about me will be edited