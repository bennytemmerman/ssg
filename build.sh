#!/bin/bash

# Define the GitHub repository name
REPO_NAME="ssg"  # Replace with your actual GitHub repository name

# Run the site generator with the base path for production
echo "Building site for production with base path /$REPO_NAME/"
python3 src/main.py "/$REPO_NAME/"

echo "Build completed successfully!"
