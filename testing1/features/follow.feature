Feature: Follow/Unfollow
As a user I want to be able to follow and unfollow other users, and see their posts on my timeline. 

    Scenario: Successfully following a user
        Given the user is viewing another user’s profile
        When the user clicks follow user
        Then another user’s followers count should be increased by 1
        And current user’s followings count should be increased by 1

    Scenario: Viewing followed users posts on my timeline
        Given the user is following other users
        When the user is viewing the timeline in Home page
        Then the list should include posts from followed users
    
    Scenario: Successfully Unfollowing a user
        Given the user is viewing another users profile
        When the user clicks Unfollow user
        Then current user’s followings count should be decreased by 1 
        And another user’s followers count should be decreased by 1 
    
    