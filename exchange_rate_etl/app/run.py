

#from app import create_app

#app = create_app()

#if __name__ == '__main__':
#    app.run(debug=True)


# revision 2

import sys
import os

# Add the project root directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app  # Import Flask app factory

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


