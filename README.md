Certainly! Here's the README content formatted in markdown:


FastAPI ADS-B REST API Application

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

### Running the Application

To run the application locally, use the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The FastAPI application will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Building and Running with Docker

You can also run the application in a Docker container. A Dockerfile is provided for this purpose.

Build the Docker image:

```bash
docker build -t ads-b-fastapi-app .
```

Run the Docker container:

```bash
docker run -dp 127.0.0.1:8000:8000 ads-b-fastapi-app
```

The FastAPI application will be accessible at [http://127.0.0.1:8000](http://127.0.0.1:8000) inside the Docker container.

## Usage

- Access tagged aircraft data: [http://127.0.0.1:8000/tagged-aircrafts](http://127.0.0.1:8000/tagged-aircrafts)

- Access both coded endpoints using http://127.0.0.1:8000/docs onces your in the swagger ui click "get", "try it out" and then click "execute" to view the response bodies to view the JSON data.
