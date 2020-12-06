import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import sklearn
from keras.models import Model, Sequential
from keras.layers import Input, Dense
from keras.callbacks import EarlyStopping

#fake data read
df = pd.read_csv('splashcitynoeather1.csv', names = ['Bus Timings','day_1','day_2'
,'day_3','day_4'], sep = ',')

bustopdemand = df.dropna()
time = bustopdemand['Bus Timings']
deman = bustopdemand['day_1']

model = Sequential()

#get number of columns in training data
n_cols = train_X.shape[1]

#add model layers
#based on bus
model.add(Dense(40, activation='relu', input_shape=(n_cols,)))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))

input_layer_1 = Input(shape=(1,), name = 'Bus')
input_layer_2 = Input(shape=(1,), name = 'weather')

model.compile(some input, some output, optimizer = 'adam', loss = 'mse')
print("Training started on ",some_input, " ", some_output, "".., this can take a while:")


output_layer = Dense(shape=(1,))

#fitting model
model.fit(validation_split=2, epochs=1)
