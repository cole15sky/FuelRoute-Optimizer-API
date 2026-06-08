# FuelRoute Optimizer API

## Overview

FuelRoute Optimizer API is a Django REST Framework application that determines the most cost-effective fueling strategy for long-distance travel across the United States.

Given a starting location and destination, the system:

* Generates the driving route
* Identifies fuel stations along the route
* Respects a maximum vehicle range of 500 miles
* Selects optimal fueling stops based on fuel prices
* Calculates total fuel consumption and fuel cost
* Returns route information, recommended fuel stops, and trip cost

This project was developed as a backend engineering assessment focused on API design, route optimization, geospatial processing, and algorithmic problem solving.

---

## Problem Statement

Fuel prices vary significantly between truck stops and regions.

Drivers traveling long distances often pay more than necessary because they do not know where the cheapest fueling opportunities exist along their route.

This API solves that problem by automatically identifying cost-effective fuel stops while ensuring the vehicle can complete the trip within its fuel range limitations.

---

## Features

### Route Optimization

* Accepts start and destination locations within the USA
* Generates driving routes using a routing provider
* Returns route distance and duration

### Fuel Cost Optimization

* Analyzes fuel stations along the route
* Selects optimal fueling locations
* Minimizes total fuel expense

### Vehicle Constraints

* Maximum vehicle range: 500 miles
* Fuel efficiency: 10 MPG

### Cost Estimation

Calculates:

* Total fuel consumption
* Cost per fueling stop
* Total trip fuel cost

### Performance Optimization

* Route caching
* Efficient station lookup
* Minimal external API calls

---

## Tech Stack

### Backend

* Python 3.12+
* Django 5+
* Django REST Framework

### Database

* SQLite (Development)
* PostgreSQL (Production Ready)

### Data Processing

* Pandas

### Routing Provider

* OpenRouteService API

### Documentation

* DRF Spectacular
* Swagger UI

---

## Project Structure

```text
fuel-route-optimizer-api/
│
├── core/
│
├── fuel/
│   ├── models/
│   ├── services/
│   ├── repositories/
│   └── management/
│       └── commands/
│
├── routing/
│   ├── providers/
│   └── services/
│
├── trips/
│   ├── serializers/
│   ├── services/
│   └── views/
│
├── requirements.txt
├── .env
├── README.md
└── manage.py
```

---

## Fuel Dataset

The application uses a fuel pricing dataset containing:

| Column            |
| ----------------- |
| OPIS Truckstop ID |
| Truckstop Name    |
| Address           |
| City              |
| State             |
| Rack ID           |
| Retail Price      |

Since latitude and longitude are not provided, stations will be geocoded and stored for route-based searches.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/cole15sky/FuelRoute-Optimizer-API

cd FuelRoute-Optimizer-API
```

### Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file:

```env
DEBUG=True

SECRET_KEY=your-secret-key

OPENROUTESERVICE_API_KEY=your-api-key
```

### Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

---

## Import Fuel Data

Import the fuel station dataset into the database.

```bash
python manage.py import_fuel_data
```

Expected result:

```text
Fuel stations imported successfully.
```

---

## API Documentation

Swagger UI:

```text
http://localhost:8000/api/docs/
```

OpenAPI Schema:

```text
http://localhost:8000/api/schema/
```

---

## Main Endpoint

### Optimize Trip

**POST**

```http
/api/trips/optimize/
```

### Request

```json
{
  "start": "Dallas, TX",
  "destination": "Chicago, IL"
}
```

### Response

```json
{
  "distance_miles": 967,
  "duration_minutes": 840,
  "fuel_cost": 291.32,
  "fuel_stops": [
    {
      "station_name": "Love's Travel Stop",
      "city": "Oklahoma City",
      "state": "OK",
      "fuel_price": 2.85
    }
  ],
  "route_geometry": []
}
```

---

## Optimization Workflow

```text
User Request
      │
      ▼
Route Service
      │
      ▼
Generate Route
      │
      ▼
Locate Stations Near Route
      │
      ▼
Apply Vehicle Range Constraints
      │
      ▼
Fuel Cost Optimization
      │
      ▼
Calculate Trip Cost
      │
      ▼
Return Results
```

---

## Fuel Cost Formula

Fuel Consumption:

```text
Fuel Used = Distance / MPG
```

Trip Cost:

```text
Fuel Cost = Fuel Used × Fuel Price
```

Vehicle Assumptions:

```text
Range = 500 Miles
Fuel Efficiency = 10 MPG
```

---

## Assessment Objectives

This project demonstrates:

* REST API Design
* Django Development
* Data Processing
* Geospatial Analysis
* Route Optimization
* Algorithmic Problem Solving
* System Design
* Performance Optimization

---
