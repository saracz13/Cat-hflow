# Class bank
## App Requiriments
- **Total and current balance:** There must be a main section (on the home screen) that displays the available amount of money, which updates automatically with every income or expense registered in the app.

- **Transaction history:** Every income or expense must be recorded in a section that includes the amount, date, type of transaction, and category.

- **Expense categories (CRUD):** There must be a section where the user can create, read, update, and delete categories to classify their money. These categories will be linked to financial transactions.

- **Transaction reason (incomes and expenses):** Each transaction must include a the option for ashort description entered freely by the user.

- **Balance and category charts:**

    - *Categories:* If classified by category, a pie chart is recommended. It can vary based on week, month, or year (or any selected period).

    - *Balance:* To view changes over time without category filtering, line or bar charts should be used to show the variation of balance over time.

- **Search filters:** Main filters should include week, month, and year. Additional filters such as biweekly or semiannual can be included to improve user experience. Filters will help display transactions by selected frequency or show all transactions from one or more categories, including amount, date, and type.

- **Transaction confirmation:** Every income or expense must show a confirmation message with the amount and all entered details to prevent errors. In the savings section, this confirmation can subtly motivate users to reconsider withdrawing money.

- **Savings section and savings types:** Users can separate savings into categories. Motivational messages (congratulatory or warning) should be displayed based on whether money is added or withdrawn.

- **Home and login page:** The home page should follow a standard app structure, allowing login via email and storing user data in files. This will allow management of multiple user profiles within the app.
## Technologies
- Python 3.13
- Figma
- Visual Studio Code
## Prototype
Figma link.
## How to run the app?
1. Open the terminal and write: "python -B main.py"
2. Choose one of the options displayed in the main menu
## Git commands to store the changes
- `git status`: Check which files are pending to track
- `git add`: Add the files to track
- `git commit`: Create the message to create the log of tracked files
- `git push origin`:Store the changes in github repository

**Comands**

```
git status
git add .
gid commit -m ""
git push
```


