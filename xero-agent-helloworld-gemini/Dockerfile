# Use Python 3.12 slim as base
FROM python:3.12-slim

# Install required system packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy project lockfile and pyproject.toml
COPY uv.lock pyproject.toml ./

# Sync dependencies (will create virtual env)
RUN uv sync --locked

# Copy the rest of the project
COPY . .

# Ensure npx can be used
ENV PATH="/usr/bin:$PATH"

# Default command to run your main.py
CMD ["uv", "run", "main.py"]
