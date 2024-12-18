

# run.py

from app import create_app  # Import the create_app function from the app package.

# Create an instance of the Flask application.
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)  # Run the application in debug mode.
