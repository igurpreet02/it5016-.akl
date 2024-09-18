Shopping List Application
Overview
The Shopping List Application allows users to create a list of items and their corresponding prices. The program calculates the total price of all items entered. This application is built with simplicity and maintainability in mind, adhering to key software design principles.

Features
Input items and their prices.
Calculate the total price of the shopping list.
User-friendly prompts and error handling.
Code Structure
The application is composed of two main functions:

get_shoppinglist(): Gathers user input for items and prices.
main(): Controls the flow of the program, providing a welcoming interface and displaying results.
Software Design Principles
KISS (Keep It Simple, Stupid)
The code is designed to be straightforward, with clear input prompts and a simple flow. Complexity is minimized, making it easy for users to understand and interact with the application.

DRY (Don't Repeat Yourself)
Common messages are defined in variables to avoid repetition. This makes the code cleaner and easier to maintain.

YAGNI (You Aren't Gonna Need It)
The application focuses only on the core functionalities required for a shopping list. Future enhancements are considered but not implemented unless necessary.

Single Responsibility Principle
Each function has a single responsibility:

get_shoppinglist(): Responsible for collecting item names and prices.
main(): Responsible for program execution and output.
Separation of Concerns
The application separates input handling, processing, and output, enhancing clarity and maintainability. Error messages are contextually relevant to provide better feedback.

Usage
To run the application, simply execute the script. Follow the prompts to enter items and their prices. Type "done" when you finish entering items.

Future Enhancements
Implement options to edit or delete items from the shopping list.
Add persistent storage to save shopping lists for future use.
Conclusion
This Shopping List Application demonstrates the application of software design principles to create a maintainable, user-friendly tool. By adhering to these principles, the code remains clean, efficient, and easy to extend.

