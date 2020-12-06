# AI-BUS
**What is the problem you are trying to solve using AI?**
- Buses do not arrive on time, or have sufficient capacity to meet the demands during rush-hour periods.
- Bus Bunching (more than one bus arriving at one time) when it is not necessary.

**What is the area of interest, gap or opportunity you are looking at?**
- Predict bus load to determine if the bus deployed is adequate

**What are the reasons that you’re targeting this problem, gap or opportunity?**
- Fuel wastage caused when buses are under-capacity
- Unreliable bus services due to commuter delays may cause passengers to be late, resulting in economic and social losses
- Under-deployment of buses

## Web_App Folder
The web app contains the templates(HTML), styles(CSS) as well as the Python script.
When the python script is executed via the command prompt, it runs on the local host *127.0.0.1:5000/*

It contains the conceptual interface for bus station inspectors to monitor the machine learning algorithm, through live bus maps, a database which dispatches buses via informing bus drivers of a Telegram message as well as a graph for the analysis of bus stop demand.

## Machine_Learning Folder
Originally, we made use of logistic regression to train the model. However, this was based on the limited data which was available previously.

Instead, we simulated data and used two different machine learning algorithms: Keras Functional API and Sequential API with LSTM (Long-Short-Term Memory). Thus, there are two files for the different algorithms.

We have yet to implement it on real-world data.

## Data_Sim Folder
Here lies the files for the data simulation.

*main.py* simulates bus, passengers and travel time and outputs the demand for passengers at the 10 bus stops in the bus_data folder.
Bus stops with “t” at the end of its ID are bus stops that the bus serves when going from terminal bus stop “100” to terminal bus stop “328”, while those with “f” at the end of its ID are bus stops that the bus serves when going from terminal bus stop “328” to terminal bus stop “100”. (i.e. the other way round)

*bus_route.png* shows the simulated bus routes for an artificial route 667.

*visualisation.py* allows us to visualise the passenger patterns, where it is peak/non-peak or “super peak” - where a sudden large amount of people come (e.g. people arriving from the MRT nearing work hours) - and that peak hours during the holidays don’t matter in this scenario.

Here are the conditions simulated:
peak seconds: 23400-32400, 61200-70200
“super peak” seconds: 29700-31800, 61500-65400
holiday(s): day 6, 25
raining: 2, 5, 23 (different timing)

###### Splash Project by AT, SP, KK, September 2, 2019
