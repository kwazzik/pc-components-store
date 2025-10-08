# PC Components Store

PC Components Store is a web application for managing a store of PC components. The project includes lists of brands, products, and employees.

## Features

- Manage brands of PC components
- Manage products available in the store
- Manage employees working in the store

## Requirements

- Python 3.x
- Django (as specified in `requirements.txt`)

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    cd pc-components-store
    ```

2. **(Optional) Create and activate a virtual environment**:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run migrations**:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

6. **Open your browser** and go to `http://127.0.0.1:8000/` to see the app.

---

## Usage

- Navigate through brands, products, and employees.
- Manage data via the Django admin or custom views.

---

## Test

You can use the following test account to log in and explore the application:

| Field       | Value       |
|-------------|-------------|
| **Username**| `user`      |
| **Password**| `user12345` |

---

## Notes

- Remember to set up your `SECRET_KEY` as an environment variable before running the project.
- Static and media files are configured as per Django defaults.
