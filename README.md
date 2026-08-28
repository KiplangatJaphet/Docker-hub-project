#  Multi-format data reader (Dockerized)

A small Python utility that reads data files of different formats — CSV, Excel, XML, JSON, Parquet — into a pandas DataFrame through a single function, `read_file()`. Packaged with `uv` and shipped as a ready-to-run Docker image on Docker Hub.

## What it does

Instead of remembering which pandas function goes with which file type, `read_file(path)` detects the format from the file extension and returns a DataFrame automatically.

| Extension          | Backend               |
|----------------------|--------------------------|
| `.csv`               | `pandas.read_csv`       |
| `.xls`, `.xlsx`        | `pandas.read_excel`     |
| `.xml`                | `pandas.read_xml`       |
| `.json`               | `pandas.read_json`      |
| `.parquet`             | `pandas.read_parquet`   |

It also validates input up front — a missing file raises `FileNotFoundError`, and an unsupported extension raises `ValueError` — before any parsing is attempted.

## Usage

```python
from main import read_file

data = read_file("data/MOCK_DATA.json")
print(data.head(10))
```

`runfile.py` is a working example that does exactly this against the sample data in `data/`.

## Run locally with uv

```bash
uv sync
uv run runfile.py
```

## Run with Docker

Build and run the image locally:

```bash
docker build -t kip .
docker run kip
```

Or pull the pre-built image directly from Docker Hub — no build required:

```bash
docker pull kiplangot/kip:latest
docker run kiplangot/kip:latest
```

Either way, the container runs the project end-to-end and prints the parsed sample dataset to the console.

## Publishing updates to Docker Hub

After making changes and rebuilding, push the updated image with:

```bash
docker login
docker tag kip:latest kiplangot/kip:latest
docker push kiplangot/kip:latest
```

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) for dependency management
- Docker (only if running/building the container)
- Dependencies: `pandas`, `lxml` (required for XML support)

## Project structure

```
datareader/
├── main.py          # read_file() — format detection and parsing logic
├── runfile.py         # example usage against sample data
├── data/               # sample input files (csv, json, xml, etc.)
├── src/                 # package source
├── Dockerfile            # container build definition
├── pyproject.toml        # project metadata and dependencies
└── uv.lock                # locked dependency versions
```
