import tensorflow as tf
from tensorflow import keras
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from keras.utils.vis_utils import plot_model
import matplotlib.style as style
pd.options.display.max_columns = 10


all_cols = ['Int Mean','Int Std',' Int Kurtosis','Int Skewness','DM-SNR Mean',
            'DM-SNR Std','DM-SNR Kurtosis','DM-SNR Skesness','Class']

ds = pd.read_csv('htru2_data.csv', names=all_cols)
ds = ds.dropna()
ds = ds.reindex(np.random.permutation(ds.index))

train = ds


train_features = train.values
train_label = train.pop('Class').values


input_dim = train_features.shape[1]
model = keras.models.Sequential()
model.add(keras.layers.Dense(16, input_dim = input_dim, activation=tf.keras.layers.LeakyReLU()))
model.add(keras.layers.Dense(1, activation=tf.keras.layers.LeakyReLU()))
model.add(keras.layers.Dense(16,  activation=tf.keras.layers.LeakyReLU()))
model.add(keras.layers.Dense(1, activation='sigmoid'))


model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics = 'binary_accuracy')


history = model.fit(train_features, train_label, epochs=30, validation_split=0.7)

metrics = np.mean(history.history['val_binary_accuracy'])
results = model.evaluate(train_features, train_label)
print('\nLoss, Binary_accuracy: \n',(results))


style.use('dark_background')
pd.DataFrame(history.history).plot(figsize=(11, 7),linewidth=4)
plt.title('Binary Cross-entropy',fontsize=14, fontweight='bold')
plt.xlabel('Epochs',fontsize=13)
plt.ylabel('Metrics',fontsize=13)
plt.show() 