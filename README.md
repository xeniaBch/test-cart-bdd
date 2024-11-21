# SimplyTestBDD

This repository contains an automated BDD (Behavior-Driven Development) testing framework using `behave` for testing the
shopping cart functionality of an e-commerce site.

## Table of Contents

- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Feature File](#feature-file)
- [Testing Patterns](#testing-patterns)
- [Potential Challenges](#potential-challenges)

---

## Project Overview

The project tests the following workflow:

1. Navigate to the shop.
2. Verify the shop title.
3. Check that the cart is empty.
4. Add an "Album" to the cart.
5. Go to the cart page.
6. Update the quantity of the album to 2.
7. Verify the total price updates to `30,00 €`.

The framework uses:

- `behave` for BDD scenarios.
- Selenium WebDriver for browser automation.
- The Page Object Model (POM) pattern for test organization.

---

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd SimplyTestBDD
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 - mvenv.venv
   source.venv / bin / activate  # For macOS/Linux
   .venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4.	**Ensure ChromeDriver is Installed:**

•	Download ChromeDriver that matches your Chrome version from ChromeDriver Downloads.
•	Add ChromeDriver to your PATH.

## Usage

1.	**Run Tests with Behave:**
```bash
   behave features/shop_cart.feature
```

2.  **Output Example:**

Successful test execution will display:
```bash
1 feature passed, 0 failed, 0 skipped
6 scenarios passed, 0 failed, 0 skipped
```

## Feature File

The behavior-driven test scenarios are defined in features/shop_cart.feature:

Feature: Shopping Cart Functionality
As a user, I want to ensure the shopping cart behaves correctly.

Scenario: Add an Album to the cart and verify the total price
Given I navigate to the shop
Then I verify the shop title is "Shop"
And I check that the cart is empty
When I add an Album to the cart
And I go to the cart page
And I set the quantity to "2" and update the cart
Then I verify the total price is "30,00 €"

### Testing Patterns

The project follows the Page Object Model (POM) pattern:
   * **Why POM?**
   * POM ensures modular, reusable, and maintainable code.
   * Each web page is represented by a class, encapsulating locators and actions.
   * Test scenarios are written at a high level, improving readability and reducing code duplication.
   * **Classes:**
   * ShopPage: Handles actions and verifications on the shop page.
   * CartPage: Handles actions and verifications on the cart page.
   * BasePage: Provides shared utilities like navigation and element waiting.

### Potential Challenges

	1.	Stale Element References:
	•	Asynchronous updates to the DOM can lead to stale references.
	•	Handled using explicit waits for DOM changes or recalculations.
	2.	Dynamic Locators:
	•	Some elements (e.g., quantity input fields) have dynamic attributes.
	•	Solution: Use stable selectors like CSS classes or data attributes.
	3.	Localization:
	•	Hardcoded strings like “30,00 €” might fail in different regions due to formatting differences.
	•	Possible solution: Parameterize or localize expected values.
	4.	Browser Compatibility:
	•	The framework currently uses Chrome. Extending to other browsers requires adjustments to WebDriver initialization.

Future Improvements

	•	Cross-Browser Testing:
	•	Add support for Firefox, Safari, and Edge.
	•	CI/CD Integration:
	•	Automate test execution with tools like GitHub Actions or Jenkins.
	•	Data-Driven Testing:
	•	Use external data sources (e.g., CSV, JSON) to drive tests with multiple datasets.
