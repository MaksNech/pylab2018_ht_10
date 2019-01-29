# Home task 10 (Werkzeug Ads App)

## 1: Initial Setup

#### Clone project in a new directory:
```bash
cd path/to/a/new/directory
git clone https://github.com/MaksNech/pylab2018_ht_10.git
```
#### Install MongoDB:
```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```
The MongoDB instance stores its data files in /var/lib/mongo.
Creating unit-file for MongoDB service control:
```bash
sudo touch /etc/systemd/system/mongodb.service
```
Inside '/etc/systemd/system/mongodb.service' adding code:
```bash
[Unit]
Description=High-performance, schema-free document-oriented database
After=network.target

[Service]
User=mongodb
ExecStart=/usr/bin/mongod --quiet --config /etc/mongod.conf

[Install]
WantedBy=multi-user.target
```

## 2: Getting Started
#### Start MongoDB:
Starting mongod.Mongod is the primary daemon process for the MongoDB system:
```bash
sudo systemctl start mongodb
sudo systemctl status mongodb
```
Access to MongoDB shell:
```bash
sudo mongo
```
Stoping mongod:
```bash
sudo systemctl stop mongodb
sudo systemctl status mongodb
```
#### Start backend:
Inside project create virtual environment:
```bash
virtualenv -p python3 env
```
Then start virtual environment:
```bash
source env/bin/activate
```
Install packages using pip according to the requirements.txt file:
```bash
pip install -r requirements.txt
```
Inside project directory run app with terminal command:
```bash
python3 main.py
```
