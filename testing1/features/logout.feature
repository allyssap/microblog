Feature: Logout the account
  As a registered user, I want to be able to logout my account so that I can be offline when I don’t want to stay in Microblog
    
    Scenario: Successfully logout the account
        Given I am a registered user
        When I try to logout my account
        And I click the “Logout” button on the top-right corner
        Then I get a notification tells me my account successfully logout
        And I stay in the main page of Microblog as I haven’t login status