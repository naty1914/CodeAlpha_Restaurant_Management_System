# CodeAlpha Restaurant Management System

The CodeAlpha Restaurant Management System is a comprehensive solution designed to streamline the operations of a restaurant. It includes features for managing menu items, orders, tables, reservations, inventory, and sales reporting.

## Features

- **Order Management**: Easily manage customer orders, track order status, and manage payments.
- **Inventory Tracking**: Monitor stock levels in real-time, manage suppliers, and avoid running out of essential items.
- **Reservation System**: Allow customers to make reservations online, manage table availability, and track reservation details.
- **Sales Reporting**: Generate detailed sales reports to gain insights into your restaurant's performance.
- **User Authentication**: Secure login and logout functionality for staff members.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/naty1914/CodeAlpha_Restaurant_Management_System.git
    cd CodeAlpha_Restaurant_Management_System
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- **Home Page**: The main landing page of the application.
- **Menu Items**: View the list of menu items available in the restaurant.
- **Orders**: Manage customer orders (accessible to staff members only).
- **Tables**: Manage table availability and status (accessible to staff members only).
- **Reservations**: Manage customer reservations (accessible to staff members only).
- **Inventory**: Track inventory levels and manage supplies (accessible to staff members only).
- **Sales Report**: Generate and view sales reports (accessible to staff members only).
- **Admin Page**: Access the Django admin interface for advanced management tasks.



## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
