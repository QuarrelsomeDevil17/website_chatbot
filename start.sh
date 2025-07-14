#!/bin/bash

# DeepSeek R1 Neural Interface - Development Script
# Cyberpunk RAG Chatbot Launcher

echo "🤖 Starting DeepSeek R1 Neural Interface..."
echo "======================================"

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "⚠️  Virtual environment not found. Creating..."
    python -m venv .venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# Check if requirements are installed
if [ ! -f ".venv/pyvenv.cfg" ] || [ ! "$(pip list | grep flask)" ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  .env file not found!"
    echo "📋 Please copy .env.example to .env and configure your API keys:"
    echo "   cp .env.example .env"
    echo "   nano .env  # Edit with your API keys"
    exit 1
fi

# Check if documents exist
if [ ! "$(ls -A documents/)" ]; then
    echo "📄 No documents found in documents/ folder."
    echo "   Add some PDF or TXT files to get started!"
fi

# Start the application
echo "🚀 Launching Neural Interface..."
echo "🌐 Access at: http://127.0.0.1:5000"
echo "⚡ Press Ctrl+C to stop"
echo ""

python app.py
