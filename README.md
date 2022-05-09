# Stem
## Web Logging Server for Daisy

### Installation
Developed and tested in Python 3.7 and 3.9, but anything past 3.3 or 3.5 should probably work. Uses the Flask and SQLAlchemy packages, both of which are installable via requirements.txt

1. Install Packages
    `pip install -r requirements.txt`
2. *(optional)* Seed database with dummy data
    ```sh
    cd utils
    python3 create_db.py
    python3 seed_db.py
    cp log.db .. 
    cd ..
    ```
3. Start development server
    ```sh
    export DAISY_FLOWER_SECRET=someSecretKey
    export DAISY_ROOTS_SECRET=someOtherSecretKey
    python3 app.py
    ```


### Implementation

We have had success following [this guide](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04) to serve the log server via nginx. Alternatively, you can just run app.py to serve on port 5000 on all bindable interfaces.