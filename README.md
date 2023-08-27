# Startup Portfolio Website

This is a Django-based web application that allows users to manage a portfolio of startups. It offers full CRUD (Create, Read, Update, Delete) functionality for startups, as well as the ability to categorize and filter them. Users can easily add, edit, and remove startups and organize them into categories. The application is built using Django, HTML, CSS, and Bootstrap for the frontend, providing a clean and responsive user interface.

## Features

- **Create, Read, Update, Delete (CRUD) Functionality**: Easily manage your startup portfolio by adding new startups, editing their details, viewing startup information, and removing startups when needed.

- **Categorization and Filtering**: Categorize your startups into different categories or tags for better organization. You can also filter startups by category to quickly find the ones you're interested in.

- **User-Friendly Interface**: The frontend is built using HTML, CSS, and Bootstrap to provide a clean and intuitive user experience.

## Technology Stack

- **Django**: The web framework used for the backend development.

- **HTML and CSS**: Used for creating the frontend user interface.

- **Bootstrap**: Provides responsive design and styling for the web application.

## Setup

To set up and run this application locally, follow these steps:

1. Clone the repository to your local machine:


2. Navigate to the project directory:


3. Create a virtual environment to isolate dependencies:


4. Activate the virtual environment:

- On Windows:

  ```
  env\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source env/bin/activate
  ```

5. Install the required dependencies:


6. Configure your database settings in `settings.py`. You can use a database like PostgreSQL for production or SQLite for development purposes.

7. Apply database migrations:


8. Open your web browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

## Usage

- Visit the homepage to view your startup portfolio.
- Use the navigation menu to add new startups, categorize them, and apply filters as needed.
- Click on a startup to view its details or make updates.
- Enjoy managing your startup portfolio with ease!
