#!/bin/bash
# Run the Django Portfolio Website
# This script starts the Django development server

echo "=========================================="
echo "Starting Django Portfolio Server"
echo "=========================================="

# Change to project directory
cd /home/z/my-project

# Activate virtual environment and run server
source /home/z/my-project/portfolio_env/bin/activate
python manage.py runserver 0.0.0.0:8000
