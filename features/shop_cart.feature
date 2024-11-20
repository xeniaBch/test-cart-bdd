Feature: Shopping Cart Workflow
  As a user
  I want to add an item to the cart, update the quantity, and verify the total price
  So that I can complete my shopping smoothly.

  Scenario: Adding an item and verifying the cart functionality
    Given I open the shop page
    Then I verify the shop title is "Shop"
    And I verify the cart is empty
    When I add "Album" to the cart
    And I navigate to the cart page
    And I set the item quantity to "2" and update the cart
    Then I verify the total price is "30,00 €"