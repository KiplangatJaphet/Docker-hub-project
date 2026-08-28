FROM python:3.14.4-slim


WORKDIR /app

#Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

#Copy dependencies
COPY pyproject.toml uv.lock ./

#Install python dependecies
RUN uv sync --locked --no-install-project

# Copy application files
COPY main.py .
COPY runfile.py .
COPY data ./data
COPY src ./src

#Run the application
CMD ["uv", "run", "python", "runfile.py"]