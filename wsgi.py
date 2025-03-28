import os
import logging

# Configure logging for Vercel environment
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Import the Flask app - this is what Vercel will use as the handler
from app import app

# This file is for WSGI servers like Gunicorn to use
# It's also compatible with Vercel's Python runtime

# For Vercel serverless functions, we need to export the app variable directly
# The name 'app' is important as Vercel looks for this as the handler
app.debug = False

# Log initialization
logger.info("WSGI handler initialized for Vercel")
logger.info(f"Running in Vercel environment: {os.environ.get('VERCEL', 'No')}")
logger.info(f"Python version: {os.environ.get('PYTHON_VERSION', 'unknown')}")

# Need to make sure temp directories exist
temp_dir = "/tmp/app_temp"
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir, exist_ok=True)
    logger.info(f"Created temp directory: {temp_dir}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))