Feature: Add to Cart Feature
  Scenario: Add two products to the cart and then quit one
    Given the user is loged in the page
    When the user add two products to the cart, go to the cart, and then quit one
    Then the cart should have just one product