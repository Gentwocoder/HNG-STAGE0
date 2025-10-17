# HNG Stage 0 - Personal Information API

A Django REST API project that provides personal information along with random cat facts. This project is part of the HNG Internship Stage 0 requirements.

## Features

- RESTful API endpoint that returns user information
- Integration with external cat facts API
- JSON response format
- Environment variable configuration
- SQLite database backend
- Django REST Framework integration

## API Endpoints

### GET `/me/`

Returns user information along with a random cat fact.

**Response Format:**
```json
{
    "status": "success",
    "user": {
        "email": "user@example.com",
        "name": "Your Name",
        "stack": "Backend"
    },
    "timestamp": "2025-10-17T12:00:00.000000+00:00",
    "fact": "A random cat fact from the API"
}
```

**Response Status:** `200 OK`

## Project Structure

```
hngstage0/
├── manage.py              # Django management script
├── db.sqlite3            # SQLite database file
├── details/              # Main Django app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py           # App URL configurations
│   ├── views.py          # API view logic
│   └── migrations/
└── hngstage0/            # Django project settings
    ├── __init__.py
    ├── asgi.py
    ├── settings.py       # Project settings
    ├── urls.py           # Main URL configurations
    └── wsgi.py
```

## Technologies Used

- **Python 3.x** - Programming language
- **Django 4.2.14** - Web framework
- **Django REST Framework** - API development
- **SQLite** - Database
- **python-decouple** - Environment variable management
- **requests** - HTTP library for external API calls

## Prerequisites

- Python 3.x installed
- pip (Python package installer)

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd HNG
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install django djangorestframework python-decouple requests
   ```

4. **Set up environment variables:**
   Create a `.env` file in the `hngstage0/` directory:
   ```env
   SECRET_KEY=your-secret-key-here
   EMAIL=your-email@example.com
   NAME=Your Full Name
   STACK=Backend
   CAT_FACT_URL=https://catfact.ninja/fact
   ```

5. **Navigate to the project directory:**
   ```bash
   cd hngstage0
   ```

6. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```

7. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the API:**
   The API will be available at `http://127.0.0.1:8000/me/`

## Environment Variables

The following environment variables need to be configured:

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key for security | `your-secret-key-here` |
| `EMAIL` | Your email address | `john@example.com` |
| `NAME` | Your full name | `John Doe` |
| `STACK` | Your technical stack | `Backend` |
| `CAT_FACT_URL` | URL for cat facts API | `https://catfact.ninja/fact` |

## Usage Examples

### Using curl:
```bash
curl -X GET http://127.0.0.1:8000/me/
```

### Using Python requests:
```python
import requests

response = requests.get('http://127.0.0.1:8000/me/')
data = response.json()
print(data)
```

## Error Handling

- If the external cat facts API is unavailable, a fallback message is provided
- All responses are in JSON format
- Proper HTTP status codes are returned

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Superuser
```bash
python manage.py createsuperuser
```

### Accessing Admin Panel
Visit `http://127.0.0.1:8000/admin/` after creating a superuser.

## Deployment Considerations

- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` for your domain
- Use a production database (PostgreSQL, MySQL)
- Set up proper environment variable management
- Configure static files serving
- Use HTTPS in production

## API Response Details

The API returns user information with:
- **status**: Always "success" for successful requests
- **user**: Object containing email, name, and stack information
- **timestamp**: Current UTC timestamp in ISO format
- **fact**: Random cat fact from external API or fallback message

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is created for the HNG Internship program.

## Contact

For questions or support, please contact the repository owner.

---

**Note:** This project is part of the HNG Internship Stage 0 requirements and demonstrates basic Django REST API development skills.