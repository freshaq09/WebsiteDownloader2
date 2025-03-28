#!/bin/bash

# This script runs during Vercel build to prepare the app for deployment

echo "Setting up environment for Vercel deployment..."

# Create required directories
mkdir -p /tmp/app_temp

# Display python version
python --version

# Install additional dependencies if needed
# pip install -r requirements.txt

# Create a file to indicate we're running on Vercel
touch .vercel_build_completed

echo "Build completed successfully!"