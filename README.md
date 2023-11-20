# FastAPI ADS-B REST API Application

This is a FastAPI-based REST API application that provides access to ADS-B (Automatic Dependent Surveillance–Broadcast) data. It fetches tagged aircraft data from the ADS-B Exchange API and serves it through a FastAPI web server.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- [Python](https://www.python.org/downloads/) (3.9 or later)
- [Docker](https://docs.docker.com/get-docker/)
- [API Key](#getting-an-api-key)

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/ads-b-rest-api-app.git
cd ads-b-rest-api-app
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Getting an API Key

To use the ADS-B Exchange API, you need to obtain an API key. You can get one by signing up at [RapidAPI](https://rapidapi.com/adsbx/api/adsb-exchange-com1/).

### Configure Environment Variables

Create a `.env` file in the project root directory and add your API key:

```env
API_KEY=your_api_key_here
```

```env.docker
API_KEY=your_api_key_here
```

### Running the Application

To run the application locally, use the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The FastAPI application will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Building and Running with Docker

You can also run the application in a Docker container. A Dockerfile and docker-compose file are provided for this purpose.

Build the Docker image (with docker-compose.yaml):

```bash
docker-compose build
```

Run the Docker container:

```bash
docker-compose up -d
```

The FastAPI application will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000) inside the Docker container.

## Usage

- Access all coded endpoints using [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). Once you're in the Swagger UI, click "GET," "Try it out," and then click "Execute" to view the response bodies and see the JSON data.