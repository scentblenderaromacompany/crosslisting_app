### Full Detailed Setup Guide

This guide will cover everything you need to set up your Cross-Listing Application from scratch, including Docker setup, environment variables, application files, and testing.

---

### 1. Project Directory Structure

Here’s the project directory structure:

```
crosslisting_app/
├── app.py
├── backend/
│   ├── __init__.py
│   ├── config/
│   │   └── config.py
│   ├── controllers/
│   │   └── controllers.py
│   ├── models/
│   │   └── models.py
│   └── routes/
│       └── routes.py
├── integrations/
│   ├── ebay/
│   │   └── ebay_api.py
│   ├── etsy/
│   │   └── etsy_api.py
│   ├── facebook/
│   │   └── facebook_api.py
│   └── offerup/
│       └── offerup_api.py
├── templates/
│   ├── index.html
│   └── create.html
├── static/
│   └── styles.css
├── tests/
│   └── test_crosslisting_app.py
├── Dockerfile
├── docker-compose.yml (optional)
├── requirements.txt
├── README.md
└── .gitignore
```

### 2. Creating the Files

Below is the detailed step-by-step guide for creating each file.

#### 2.1. CSS Styling (`styles.css`)

```bash
cat > ~/crosslisting_app/static/styles.css << 'EOF'
/* General Styling */
body {
    font-family: 'Garamond', serif;
    background-color: #F5F5DC; /* Light beige/cream background */
    color: #4B3A31; /* Dark brown text color */
    margin: 0;
    padding: 0;
}

/* Header Styling */
header {
    background-color: #8B7D6B; /* Medium brown for header background */
    color: #F5F5DC; /* Light beige text */
    padding: 20px;
    text-align: center;
    border-bottom: 3px solid #D2B48C; /* Light brown border */
}

header nav ul {
    list-style: none;
    padding: 0;
    display: flex;
    justify-content: center;
}

header nav ul li {
    margin: 0 20px;
}

header nav ul li a {
    color: #F5F5DC; /* Light beige */
    text-decoration: none;
    font-weight: bold;
    font-size: 18px;
}

header nav ul li a:hover {
    color: #D2B48C; /* Light brown/gold */
}

/* Main Content Styling */
main {
    padding: 40px;
    max-width: 800px;
    margin: auto;
    background-color: #FFF8DC; /* Antique white for main content */
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    font-family: 'Georgia', serif;
    color: #8B4513; /* Saddle brown for headings */
}

/* Listing Style */
.listing-list {
    list-style: none;
    padding: 0;
}

.listing-list li {
    background-color: #FFF5EE; /* Seashell color for listings */
    border: 1px solid #D2B48C; /* Light brown border */
    margin-bottom: 20px;
    padding: 20px;
    border-radius: 8px;
}

.listing-list li h2 {
    margin-top: 0;
    font-size: 24px;
}

.listing-list li p {
    margin: 5px 0;
}

/* Form Styling */
form {
    background-color: #FDF5E6; /* Old Lace for form background */
    padding: 30px;
    border-radius: 10px;
    border: 1px solid #D2B48C; /* Light brown border */
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 8px;
    font-weight: bold;
    color: #8B4513; /* Saddle brown for labels */
}

input, textarea, select, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 16px;
    border-radius: 5px;
    border: 1px solid #D2B48C; /* Light brown border */
    font-family: 'Garamond', serif;
    font-size: 16px;
}

button {
    background-color: #8B7D6B; /* Medium brown */
    color: #F5F5DC; /* Light beige text */
    cursor: pointer;
    font-size: 18px;
}

button:hover {
    background-color: #D2B48C; /* Light brown/gold */
}

/* Footer Styling */
footer {
    background-color: #8B7D6B; /* Medium brown */
    color: #F5F5DC; /* Light beige text */
    text-align: center;
    padding: 15px;
    border-top: 3px solid #D2B48C; /* Light brown border */
    position: fixed;
    bottom: 0;
    width: 100%;
}

footer p {
    margin: 0;
}
EOF
```

#### 2.2. Dockerfile

```bash
cat > ~/crosslisting_app/Dockerfile << 'EOF'
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run the application
CMD ["flask", "run", "--host=0.0.0.0"]
EOF
```

#### 2.3. Requirements File (`requirements.txt`)

```bash
cat > ~/crosslisting_app/requirements.txt << 'EOF'
Flask==2.0.1
Flask-SQLAlchemy==2.5.1
Selenium==3.141.0
ebaysdk==2.1.5
requests==2.25.1
python-dotenv==0.19.0
EOF
```

#### 2.4. README File (`README.md`)

```bash
cat > ~/crosslisting_app/README.md << 'EOF'
# Cross-Listing Application

## Overview
The Cross-Listing Application allows users to create and manage product listings across multiple online marketplaces, including eBay, Etsy, Facebook Marketplace, and OfferUp. The application provides a unified interface for creating listings, which are then automatically posted to the selected marketplaces.

## Features
- Create and manage listings for multiple marketplaces.
- Unified interface for ease of use.
- Automatic posting to eBay, Etsy, Facebook Marketplace, and OfferUp.
- Responsive design with a vintage theme that aligns with "Eternal Elegance Emporium" branding.

## Technologies Used
- **Flask**: Lightweight web framework for Python.
- **Flask-SQLAlchemy**: ORM for managing database operations.
- **Selenium**: Web automation tool used for Facebook Marketplace and OfferUp.
- **ebaysdk**: Python SDK for interacting with the eBay API.
- **requests**: Simplified HTTP requests for Etsy API integration.
- **Docker**: Containerization tool for easy deployment.

## Setup and Installation

### Prerequisites
- **Docker**: Ensure Docker is installed on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).
- **Git**: Ensure Git is installed for version control and cloning the repository.

### Step-by-Step Guide

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/crosslisting_app.git
   cd crosslisting_app
   ```

2. **Environment Setup**
   - Create a `.env` file in the project root to store environment variables securely:
     ```bash
     touch .env
     ```
   - Add your environment variables (API keys, tokens, etc.):
     ```
     SECRET_KEY=your-secret-key
     DATABASE_URL=sqlite:///site.db
     FLASK_DEBUG=true
     EBAY_APP_ID=your-ebay-app-id
     EBAY_CERT_ID=your-ebay-cert-id
     EBAY_DEV_ID=your-ebay-dev-id
     EBAY_TOKEN=your-ebay-token
     ETSY_API_KEY=your-etsy-api-key
     ```

3. **Building the Docker Container**
   - Build the Docker image:
     ```bash
     docker build -t crosslisting_app .
     ```
   - Run the Docker container:
     ```bash
     docker run -p 5000:5000 crosslisting_app
     ```

4. **Accessing the Application**
   - Open your web browser and navigate to `http://localhost:5000`.

### Usage

- **Create Listings**: Use the form on the `/create` page to input your product details and select the marketplaces you want to post to.
- **View Listings**: View all created listings on the homepage.

### Testing

- Run unit tests to ensure the application functions as expected:
  ```bash
  python -m unittest discover -s tests
  ```

## Deployment

- The application can be deployed using Docker on any platform that supports it, including AWS, Google Cloud, and Azure.

## Contributing

- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Commit your changes (`git commit -m 'Add some feature'`).
- Push to the branch (`git push origin feature-branch`).
- Open a Pull Request.

## License

This project is licensed under the MIT License.
EOF
```

#### 2.5. Docker Compose (Optional)

```bash
cat > ~/crosslisting_app/docker-compose.yml << 'EOF'
version: '3.7'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_APP=app.py
      - FLASK_ENV=development
    volumes:
      - .:/app
    command: flask run --host=0.0.0.0

  db:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: crosslisting
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
EOF
```

#### 2.6. .gitignore File

```bash
cat > ~/crosslisting_app/.gitignore << 'EOF'
*.pyc
__pycache__/
instance/
.env
.DS_Store
EOF
```

#### 2.7. Python Application Files

- **Main Application File (`app.py`)**:

```bash
cat > ~/crosslisting_app/app.py << 'EOF'
from flask import Flask
from backend.routes.routes import main
from backend.models.models import db
from backend.config import Config
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    try:
        db.init_app(app)
        with app.app_context():
            db.create_all()
        app.register_blueprint(main)
        return app
    except Exception as e:
        print(f"Error initializing the app: {e}")
        return None

if __name__ == '__main__':
    app = create_app()
    if app:
        app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')
EOF
```

- **Backend Configuration (`config.py`)**:

```bash
cat > ~/crosslisting_app/backend/config/config.py << 'EOF'
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'sqlite:///dev_site.db')

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL', 'sqlite:///prod_site.db')
EOF
```

- **Models (`models.py`)**:

```bash
cat > ~/crosslisting_app/backend/models/models.py << 'EOF'
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    marketplace = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @validates('price')
    def validate_price(self, key, price):
        if price <= 0:
            raise ValueError("Price must be positive")
        return price

    def __repr__(self):
        return (f"<Listing(id={self.id}, title='{self.title}', price={self.price}, "
                f"marketplace='{self.marketplace}', created_at='{self.created_at}')>")
EOF
```

- **Controllers (`controllers.py`)**:

```bash
cat > ~/crosslisting_app/backend/controllers/controllers.py << 'EOF'
import logging
from backend.models.models import db, Listing
from integrations.ebay.ebay_api import create_ebay_listing
from integrations.etsy.etsy_api import create_etsy_listing
from integrations.facebook.facebook_api import create_facebook_listing
from integrations.offerup.offerup_api import create_offerup_listing

logging.basicConfig(level=logging.INFO)

def create_listing(data):
    try:
        new_listing = Listing(
            title=data['title'],
            description=data['description'],
            price=data['price'],
            image_url=data['image_url'],
            marketplace=', '.join(data['marketplace']),
            category=data['category'],
            condition=data['condition']
        )
        db.session.add(new_listing)
        db.session.commit()

        logging.info(f"Listing created: {new_listing}")

        # Cross-listing logic
        for marketplace in data['marketplace']:
            try:
                if marketplace == 'ebay':
                    create_ebay_listing(new_listing)
                elif marketplace == 'etsy':
                    create_etsy_listing(new_listing)
                elif marketplace == 'facebook':
                    create_facebook_listing(new_listing)
                elif marketplace == 'offerup':
                    create_offerup_listing(new_listing)
                logging.info(f"Successfully listed on {marketplace}")
            except Exception as e:
                logging.error(f"Error listing on {marketplace}: {e}")

        return new_listing
    except Exception as e:
        logging.error(f"Error creating listing: {e}")
        raise

def get_all_listings():
    return Listing.query.all()
EOF
```

- **Routes (`routes.py`)**:

```bash
cat > ~/crosslisting_app/backend/routes/routes.py << 'EOF'
from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.controllers.controllers import create_listing, get_all_listings

main = Blueprint('main', __name__)

@main.route('/')
def index():
    listings = get_all_listings()
    return render_template('index.html', listings=listings)

@main.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        try:
            data = {
                'title': request.form['title'],
                'description': request.form['description'],
                'price': request.form['price'],
                'image_url': request.form['image_url'],
                'marketplace': request.form.getlist('marketplace'),
                'category': request.form['category'],
                'condition': request.form['condition']
            }
            create_listing(data)
            flash('Listing created successfully!', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            flash(f'Error creating listing: {e}', 'danger')
    return render_template('create.html')
EOF
```

#### 2.8. HTML Templates

- **index.html**:

```bash
cat > ~/crosslisting_app/templates/index.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listing Dashboard</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/create">Create Listing</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <h1>All Listings</h1>
        <ul class="listing-list">
        {% for listing in listings %}
            <li>
                <h2>{{ listing.title }}</h2>
                <p>{{ listing.description }}</p>
                <p>Price: ${{ listing.price }}</p>
                <p>Marketplaces: {{ listing.marketplace }}</p>
            </li>
        {% endfor %}
        </ul>
    </main>

    <footer>
        <p>&copy; 2024 Cross-Listing App. All rights reserved.</p>
    </footer>
</body>
</html>
EOF
```

- **create.html**:

```bash
cat > ~/crosslisting_app/templates/create.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create a New Listing</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    <script>
        function validateForm() {
            const price = document.getElementById('price').value;
            if (price <= 0) {
                alert('Price must be a positive number.');
                return false;
            }
            return true;
        }
    </script>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/create">Create Listing</a></li>
            </ul>
        </nav>
    </header>
    
    <main>
        <h2>Create a New Listing</h2>
        <form action="/create" method="post" onsubmit="return validateForm();">
            <label for="title">Title:</label>
            <input type="text" id="title" name="title" required>

            <label for="description">Description:</label>
            <textarea id="description" name="description" required></textarea>

            <label for="price">Price:</label>
            <input type="number" id="price" name="price" step="0.01" required>

            <label for="image_url">Image URL:</label>
            <input type="text" id="image_url" name="image_url" required>

            <label for="marketplace">Marketplace:</label>
            <select id="marketplace" name="marketplace" multiple required>
                <option value="ebay">eBay</option>
                <option value="etsy">Etsy</option>
                <option value="facebook">Facebook Marketplace</option>
                <option value="offerup">OfferUp</option>
            </select>

            <label for="category">Category:</label>
            <input type="text" id="category" name="category" required>

            <label for="condition">Condition:</label>
            <input type="text" id="condition" name="condition" required>

            <button type="submit">Create Listing</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2024 Cross-Listing App. All rights reserved.</p>
    </footer>
</body>
</html>
EOF
```

#### 2.9. Testing

- **Unit Tests (`test_crosslisting_app.py`)**:

```bash
cat > ~/crosslisting_app/tests/test_crosslisting_app.py << 'EOF'
import unittest
from flask import Flask
from backend.models.models import db, Listing
from backend.controllers.controllers import create_listing

class TestCrossListingApp(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_listing(self):
        with self.app.app_context():
            data = {
                'title': 'Test Product',
                'description': 'This is a test product.',
                'price': 19.99,
                'image_url': 'http://example.com/test.jpg',
                'marketplace': ['ebay', 'etsy', 'facebook', 'offerup'],
                'category': 'Electronics',
                'condition': 'New'
            }
            listing = create_listing(data)
            self.assertIsNotNone(listing)
            self.assertEqual(listing.title, 'Test Product')
            self.assertEqual(listing.price, 19.99)
            self.assertIn('ebay', listing.marketplace)

if __name__ == '__main__':
    unittest.main()
EOF
```

### 3. Running the Application

#### 3.1. Build and Run the Docker Container

1. Build the Docker image:

```bash
docker build -t crosslisting_app .
```

2. Run the Docker container:

```bash
docker run -p 5000:5000 crosslisting_app
```

3. Access the application at `http://localhost:5000`.

#### 3.2. Running the Tests

You can run the tests using:

```bash
python -m unittest discover -s tests
```

### Final Step

I'll save everything into a single text file for download:

```python
with open("/mnt/data/crosslisting_full_setup.txt", "w") as file:
    file.write(detailed_guide)
```		