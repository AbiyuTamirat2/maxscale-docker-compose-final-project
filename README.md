# MaxScale Docker Compose Final Project

## Introduction

Welcome to the Sharded Database Setup guide using MaxScale and Docker Compose! This README.md provides comprehensive instructions for configuring and deploying a sharded database environment with MariaDB MaxScale. It covers setting up MaxScale using Docker Compose, configuring MaxScale with example.cnf for managing two master databases, and interacting with the setup using a Python script.

## Getting Started

Follow these instructions to set up and run the project on your local system.

### Prerequisites

Ensure you have the following software installed on your system:

1. [Ubuntu 22.04.4 LTS (Jammy Jellyfish)] (https://releases.ubuntu.com/jammy/)
2. [Python 3] (https://www.python.org/downloads/)
3. [PyCharm IDE] (https://www.jetbrains.com/pycharm/download/?section=windows)
4. Install required Python packages using PyCharm, such as:
 - MySQL Connector for Python: import mysql.connector
5. Docker Compose
6. MariaDB Server

You can install Docker, Docker Compose, and MariaDB Server with the following commands:

```
sudo apt install docker-compose
```
```
sudo apt install mariadb-server
```

### Setup

1. Create a directory for your project and navigate into it:

```
mkdir final
```
```
cd final
```

2. Clone the MaxScale Docker repository from GitHub:

```
git clone https://github.com/AbiyuTamirat2/maxscale-docker-compose-final-project
cd maxscale-docker-compose-final-project/maxscale
```


3. Edit the docker-compose.yml file to configure your MaxScale setup:
```
sudo nano docker-compose.yml
```

4. Start the MaxScale setup with Docker Compose:
```
sudo docker-compose up -d
```

5. Check the status of MaxScale and the servers:
```
sudo docker-compose exec maxscale maxctrl list servers
```

6. Access MariaDB through MaxScale:
```
sudo mariadb -umaxuser -pmaxpwd -h 127.0.0.1 -P 4000
```

### Tear Down

To stop and remove the containers:
```
sudo docker-compose down --volumes --remove-orphans
```

### Configuration

#### Maxscale Docker-Compose Setup

The docker-compose.yml file in the maxscale directory defines the MaxScale setup with:
- Two Master databases (dbmaster1, dbmaster2)
- One MaxScale instance (maxscale)

#### Configuring MaxScale

Edit the example.cnf file inside the maxscale.cnf.d directory to configure MaxScale's connection to the two master database shards:
```
sudo nano maxscale.cnf.d/example.cnf
```

Ensure the configuration aligns with your setup and save the file.

#### Running the Python Script
Ensure Python is installed, and use the provided script to connect to MaxScale and execute the queries.



Output of sudo docker-compose exec maxscale maxctrl list servers:

```
┌─────────┬──────────┬──────┬─────────────┬─────────────────┬──────────┬─────────────────────┐
│ Server     │ Address     │ Port   │ Connections     │ State               │ GTID         │ Monitor                   │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────────┼─────────────────────┤
│ dbmaster1  │ dbmaster1   │ 3306   │ 0              │ Master, Running      │              │ MariaDB-Monitor           │
├─────────┼──────────┼──────┼─────────────┼─────────────────┼──────────┼─────────────────────┤
│ dbmaster2  │ dbmaster2   │ 3306   │ 0              │ Running              │             │ MariaDB-Monitor            │
└─────────┴──────────┴──────┴─────────────┴─────────────────┴──────────┴─────────────────────┘
```

## Credits

Special thanks to Christine Sutton for her valuable guidance throughout this project, and to Zak for providing the original codebase that we adapted to meet our needs. Your support and contributions have been crucial to our success.