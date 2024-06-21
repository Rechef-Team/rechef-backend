# Rechef API

## Features

- **Predictive Analysis**: Use machine learning models to make predictions.
- **Recipe Management**: Manage and retrieve recipes efficiently.

## File Structure

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. The recommended version is Python 3.8 or higher.

### Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd rechef-backend
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, execute the `main.py` script:

```bash
fastapi dev app/main.py
```

The application will start running on `http://127.0.0.1:8000`.

## API Endpoints

The API endpoints are documented using Swagger UI. You can access the documentation by visiting `http://127.0.0.1:8000/docs`.