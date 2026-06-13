#!/bin/bash
# Auto-setup script for Mac/Linux users

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo ""
echo "Initializing database..."
python init_db.py

echo ""
echo "Setup complete! Starting the application..."
python app.py
