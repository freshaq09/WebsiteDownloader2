#!/bin/bash

# This script runs during Vercel build to prepare the app for deployment

echo "Setting up environment for Vercel deployment..."

# Create required directories
mkdir -p /tmp/app_temp

# Display python version
python --version

# Install required dependencies
pip install beautifulsoup4 email-validator flask flask-login flask-socketio flask-sqlalchemy flask-wtf gunicorn psycopg2-binary requests socketio trafilatura werkzeug eventlet redis

# Create a file to indicate we're running on Vercel
touch .vercel_build_completed

echo "Build completed successfully!"