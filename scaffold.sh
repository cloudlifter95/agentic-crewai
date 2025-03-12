#!/bin/bash

# Define the base project folder
PROJECT_DIR="./"

# Create the base directory structure
mkdir -p "$PROJECT_DIR/.github/workflows"
mkdir -p "$PROJECT_DIR/app"

# Create the necessary files within each folder
touch "$PROJECT_DIR/.github/workflows/crewai-ci.yml"
touch "$PROJECT_DIR/app/__init__.py"
touch "$PROJECT_DIR/app/agents.py"
touch "$PROJECT_DIR/app/tasks.py"
touch "$PROJECT_DIR/app/crew.py"
touch "$PROJECT_DIR/app/main.py"
touch "$PROJECT_DIR/requirements.txt"
touch "$PROJECT_DIR/Dockerfile"
touch "$PROJECT_DIR/docker-compose.yml"
touch "$PROJECT_DIR/.gitignore"
touch "$PROJECT_DIR/README.md"

# Optionally, print out the structure
echo "Folder structure created for crewai-multi-agent-poc:"
find "$PROJECT_DIR"
