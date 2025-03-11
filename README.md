# Online Bookstore API with Payment Integration

## Overview
Build a **Bookstore API** where users can browse, search, purchase, and manage books. This project will involve integrating payment gateways (e.g., Stripe or PayPal), setting up user authentication, and working with a product database.

## Key Concepts
- **API Development**: Design and implement a full-fledged RESTful API.
- **User Authentication & Authorization**: Implement secure authentication and role-based access.
- **Payment Gateway Integration**: Integrate a third-party payment service like Stripe to handle book purchases.
- **Data Validation**: Ensure proper validation and sanitization of user input.
- **Database Management**: Use SQLAlchemy to manage product (book) data, users, and orders.
- **Error Handling**: Robust error handling for various failure scenarios (e.g., payment failure, invalid book ID).
- **Testing**: Write unit and integration tests to ensure system reliability.

## Steps to Build

### 1. Set Up FastAPI
- [x] Install **FastAPI** and **Uvicorn**.
- [x]Create routes and basic structure for your API, including `/books`, `/users`, `/orders`, and `/payments`.

### 2. User Management
- Implement user registration and login with password hashing (e.g., using **bcrypt**).
- Use **JWT** or **OAuth2** for authentication, allowing users to log in and access certain endpoints (e.g., viewing orders).
- Create endpoints for user management, such as:
  - `POST /users/register`
  - `POST /users/login`

### 3. Book Management
- Create a model for books, which includes fields like `title`, `author`, `price`, `description`, and `stock quantity`.
- Implement CRUD endpoints for managing books:
  - [x] `GET /books`: Fetch all books.
  - [x] `GET /books/{id}`: Fetch a single book by ID.
  - [x] `POST /books`: Add a new book (admin-only).
  - [x] `PUT /books/{id}`: Update book details (admin-only).
  - [x] `DELETE /books/{id}`: Delete a book (admin-only).

### 4. Order Management
- Implement an order model that links users to the books they purchase (with quantity and price).
- Create an order placement flow:
  - `POST /orders`: A user places an order for one or more books. This step should not process payments yet but create the order in the database.
  - `GET /orders/{id}`: View an order's status with order details.
- Orders can have different statuses: "pending," "paid," "shipped," etc.

### 5. Payment Gateway Integration
- Integrate **Stripe** or **PayPal** for handling payments.
- Implement a `/payments` endpoint to handle the payment process. When an order is created, the user should be redirected to complete the payment.
- After payment is successful, update the order status to "paid" in the database.
- Handle payment failure scenarios and rollback orders as needed.

### 6. Inventory Management
- When an order is confirmed, reduce the stock quantity of books accordingly.
- Implement a system to check stock levels before an order is placed and return an error if not enough stock is available.

### 7. Error Handling
- Ensure appropriate error responses are given for invalid inputs, missing fields, payment failures, or unavailable books.
  - Example error handling: "Insufficient stock," "Invalid payment," "Unauthorized access," etc.

### 8. Testing
- Write tests for the endpoints, especially for user authentication, order creation, and payment processing.
- Use **pytest** for testing API responses and integration with the payment gateway.

### 9. Deployment
- Consider deploying your API to **Heroku**, **AWS**, or **Docker** for containerization.
- Ensure that sensitive information like API keys (for Stripe/PayPal) is handled securely (e.g., using environment variables).

## Libraries & Tools
- **FastAPI**: For building the API.
- **SQLAlchemy**: ORM for database management (use PostgreSQL or SQLite).
- **Stripe or PayPal API**: For payment integration.
- **JWT**: For user authentication.
- **Pydantic**: For request data validation.
- **pytest**: For testing your API.
- **Docker** (optional): To containerize your application.
- **Uvicorn**: ASGI server for FastAPI.

## Optional Enhancements
- **Search Functionality**: Implement a search feature that allows users to find books by title, author, or genre.
- **Admin Panel**: Create a separate admin route where administrators can manage books, view orders, and view payment history.
- **Email Notifications**: Send an email to the user upon order confirmation or payment success/failure using an email service like **SendGrid**.
- **Discount System**: Implement discount codes or promotions for users at checkout.

## Why This Project?
- You will get to work with real-world integrations, like payment gateways and user authentication.
- You will also deal with practical database management and inventory control.
- This project will introduce you to concepts like user role management, error handling, and data validation that are essential for backend development.
