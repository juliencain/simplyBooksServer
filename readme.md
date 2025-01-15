# Simply Books Assesment 




## About the User

This application is designed for users who wish to manage their book collection. It allows them to easily add, view, update, and remove books from their library, along with detailed information about the authors. The app solves the problem of keeping an organized record of both books and their respective authors, making it simple for users to track and update their literary collections.

## Features
- Manage authors: Create, Read, Update, Delete
- Manage books: Create, Read, Update, Delete

- Manage genres: Create, Read, Update, Delete
- Manage book-genre relationships: Create, Read, Update, Delete (many-to-many relationship between books and genres)



## Links
- Please see the [API Documentation](https://documenter.getpostman.com/view/33976888/2sAYQXpYcK)
- Check out this [LOOM] (https://www.loom.com/share/0f75f2a05f6a49a3984bc1707d03ecf7?sigitd=e1c59be0-567f-4eab-a523-2b0b1aac41f4)



## Contributors
- Julien Smith (https://github.com/juliencain)



## Instructions 

- [Simply Books API-Back End RUBRIC](https://docs.google.com/spreadsheets/d/1Ijb2Z6kY-2s4KmTdAwoMiKZ_CFj_FodfEOvrd3K70yc/edit?usp=sharing)

- [BACK END: Definition of Done](#be-definition-of-done)
- [MVP Guidelines](#mvp-guidelines)
- [Guide to getting started with this project](#guide-to-getting-started)

### BE Definition of Done
A feature or task is considered "done" when:
1. All tasks, features, and fixes must be ticketed and included on the GitHub project board.
Make sure the project board uses columns like Backlog, In Progress, Testing, and Done to track work.
1. The code is fully implemented and meets the requirements defined in the task.
1. The feature passes all AC especially for CRUD functionality.
1. The user can successfully perform Create, Read, Update, and Delete operations for both books and authors using postman.
1. All relationships between authors and books are correctly established and maintained.
1. The API docs are deployed on Postman, and all features work in the deployed environment.
1. The README is updated with any relevant instructions, and a Loom video (max 5 minutes) demonstrates the app's features.
1. For any stretch goals, the feature must be functional and demonstrate proper user interaction (e.g., public/private book functionality, simulated purchase).
1. Any issues or bugs identified during development or testing must be fixed by the developer. All work related to fixes must be ticketed and included on the GitHub project board.
1. The project board must reflect all tasks, bugs, and updates, with each task being moved through the proper columns (Backlog, In Progress, Testing, Done).

### MVP Guidelines
The Minimum Viable Product (MVP) for the Simply Books project includes:
1. **CRUD Functionality for Books and Authors**:
   - Users must be able to create, read, update, and delete books and authors.
   - When viewing an author, all books associated with that author must be visible.
   - When deleting an author, all of their books are also deleted.
   
2. **Author-Book Relationship**:
   - Each book must be associated with an author.
   - When a user views a book, the associated author's details must be accessible.
   
3. **Firebase Integration**:
   - The app must use Firebase for authentication and real-time data management.
   - Books and authors are tied to the logged-in user.

4. **User-Specific Data**:
   - Each user should only see their own books and authors.

#### Stretch Goals:
- **Public/Private Books**:
   - Users can mark books as public or private.
   - Public books are viewable by all users without needing to log in.
   - Private books are only visible to the user who created them.
   
- **Simulated Book Purchases**:
   - Users can add books to a cart and simulate purchasing them.
   - No real transaction will occur, but the UI will allow users to add items to the cart and check out.

### Guide to Getting Started
Follow the deployment guide to get your app live!

1. **Follow the Guide**:
   - Detailed steps for each part of the project can be found in the [Guide to getting started with this project](/project-docs/GET_STARTED.md).

1. **Submit**:
   - Make sure to complete the README, Loom video demonstration, and submit your project with the deployed link.