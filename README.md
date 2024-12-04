# Monitoring Weather App

This project is a comprehensive weather forcast application built using a microservices architecture. It includes a frontend interface, a backend API and monitoring tools integrated with Prometheus and Grafana. 
The application is containerized and managed using Docker Compose.

---

## Table of Contents

1. [📌 Project Overview](#-project-overview)
2. [✨ Features](#-features)
3. [📋 Prerequisites](#-prerequisites)
4. [🛠️ Services Overview](#-services-overview)
5. [🚀 How to Run](#-how-to-run)
6. [📊 Usage](#-usage)

---

## 📌 Project Overview

The **Monitoring Weather App** demonstrates a scalable solution for monitoring and managing weather data using microservices. The application stack includes:

- **Prometheus**: For monitoring and alerting.
- **Grafana**: For visualization of metrics.
- **Weather UI**: A React-based user interface.
- **Backend API**: Provides weather data services.
- **Nginx**: Acts as a reverse proxy for efficient traffic management.

---

## ✨ Features

- **Real-Time Monitoring**: Track application performance and metrics using Prometheus and Grafana.
- **Interactive Dashboard**: Visualize application metrics and system health on Grafana.
- **Scalable Architecture**: Built with modular services for easy maintenance and expansion.
- **Frontend and Backend Integration**: Seamless data flow between the UI and backend API.
- **Containerized Deployment**: Use Docker Compose to deploy and manage services efficiently.

---

## 📋 Prerequisites

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/) 

---

## 🛠️ Services Overview

### 1. **Prometheus**
- **Purpose**: Monitors system metrics and generates alerts.
- **Configuration**: `prometheus.yml`
- **Access**: [http://localhost:9090](http://localhost:9090)

### 2. **Grafana**
- **Purpose**: Visualizes metrics and creates dashboards.
- **Persistent Storage**: Configured at `./grafana`
- **Access**: [http://localhost:3000](http://localhost:3000)

### 3. **Weather UI**
- **Purpose**: A React-based frontend for users to view weather data.
- **Source Code**: `./weather-ui`
- **Access**: [http://localhost](http://localhost)

### 4. **Backend**
- **Purpose**: Provides weather data via REST APIs.
- **Source Code**: `./backend`
- **Default Port**: 5000

### 5. **Nginx**
- **Purpose**: Acts as a reverse proxy to manage traffic between services.
- **Source Code**: `./nginx`
- **Default Port**: 80

---

## 🚀 How to Run

### Step 1: Clone the Repository
```bash
git clone https://github.com/omerapp99/Prometheus.git
cd Prometheus
```
### Step 2: Build and Start Services
```bash
docker-compose up --build
```

### Step 3: Access Services
```bash
Prometheus: http://localhost:9090
Grafana: http://localhost:3000
Weather UI: http://localhost
```

## 📊 Usage
1. Prometheus

    Open http://localhost:9090 to view metrics.
    Modify prometheus.yml to add custom alert rules and metrics.

2. Grafana

    Access http://localhost:3000.
    Log in with default credentials (admin/admin) and set a new password.
    Add Prometheus as a data source:
        Go to Configuration > Data Sources.
        Select Prometheus and set the URL as http://prometheus:9090.
    Import or create dashboards to visualize metrics.

3. Weather UI

    Open http://localhost to view the weather forecast interface.


📂 Project Structure

├── backend/          # Flask backend code
├── weather-ui/       # React frontend code
├── nginx/            # Nginx configuration
├── prometheus.yml    # Prometheus configuration
├── grafana/          # Persistent Grafana data
├── docker-compose.yml # Docker Compose file
├── README.md         # Project documentation
