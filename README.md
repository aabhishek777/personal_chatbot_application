# Anout Me Chatbot

A chatbot application built with Python.

## Installation

```bash
# Install uv if you haven't already
pip install uv

# Install dependencies
uv sync

# Install in development mode (includes dev dependencies)
uv sync --dev
```

## Usage

```bash
# Run the application
uv run app.py

# Or after installation
anout-me-chatbot
```

## Development

```bash
# Run tests
uv run pytest

# Format code
uv run black .

# Sort imports
uv run isort .

# Type checking
uv run mypy .
```

## Requirements

- Python 3.8+
- uv package manager
