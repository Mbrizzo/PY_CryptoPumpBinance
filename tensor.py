# https://www.tensorflow.org/install?hl=pt-br

import tensorflow as tf
import pandas as pd
import numpy as np

# Ler o arquivo CSV gerado em volume.py
#df = pd.read_csv('teste.csv', names=['coluna1', 'coluna2', 'coluna3'])

# Extrair as colunas do DataFrame
x_data = df[['coluna1', 'coluna2']].values
y_data = df['coluna3'].values

# Definir um modelo simples de regressão linear
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_shape=[2])
])

# Compilar o modelo
model.compile(optimizer=tf.keras.optimizers.Adam(1),
              loss='mean_squared_error')

# Treinar o modelo
model.fit(x_data, y_data, epochs=1000)

# Fazer uma previsão com o modelo treinado
prediction = model.predict([2409.0763699999998])
print(prediction)