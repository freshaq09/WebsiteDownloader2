from app import app

# This file is for WSGI servers like Gunicorn to use
# It's also compatible with Vercel's Python runtime
if __name__ == "__main__":
    app.run()