Feature: Creating posts
	As a registered user, I want to create posts for products so that I can share my thinking about this product

	Scenario: Successfully create posts
		Given I am a registered user who is signed in
		When I am at the index
		And I write the product that I want to create post for
		And I write the company that makes the product
		And I select the category of the product
		And I finish write the post
		And I click the submit button
		Then a notification should be given that tells me the post has been successfully created
		And I should see my new post on the “Home” page
		Then I sign out

	Scenario: Unsuccessfully create posts
		Given I am a registered user who is signed in
		When I am at the index
		And I choose the product that I want to create post for
		And I leave my post as blank
		And I click the submit button 
		Then a notification should be given that tells me the post should not be blank
		And I stay in the creation post session
		Then I sign out
