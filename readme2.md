# AIBUS
**What is the problem you are trying to solve using AI?**
- Buses do not arrive on time, or have sufficient capacity to meet the demands during rush-hour periods.
- Bus Bunching (more than one bus arriving at one time) when it is not neccessary.

## Extracting files via Extractdata.py
Using an API call made to the LTA bus stop dataset, we would then make use of the json data, as well as some python code to retrieve the relevant data of the bus crowding on the bus.

The data was ran on a Python Anywhere script which collected bus stop data over two bus stops, Bef Wilkinson Road Bus Stop and Mountbatten Mrt Bus stop over a few days. It is stored in a csv format.

The various loads (crowding level) on the bus are reflected as follows:
- SEA (for Seats Available)
- SDA (for Standing Available)
- LSD (for Limited Standing)

## Machine Learning
We made use of logistic regression to train the model.

The data was split up into training and test sets.

The model has a 90% accuracy.

###### Project by AT, SP, KK
