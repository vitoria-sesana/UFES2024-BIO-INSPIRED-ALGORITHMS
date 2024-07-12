import pandas as pd

previsores = pd.read_csv('entradas_breast.csv')
classe = pd.read_csv('saidas_breast.csv')

previsores_shape = previsores.shape
classe_shape = classe.shape

print(f"Previsores - Linhas{previsores_shape[0]}, Colunas: {previsores_shape[1]}")
print(f"Previsores - Linhas{classe_shape[0]}, Colunas: {classe_shape[1]}")

print('Análise descritiva')
print(previsores.describe())

from sklearn.model_selection import train_test_split
previsores_treinamento, previsores_teste, classe_treinamento, classe_teste = train_test_split(previsores, classe, test_size=0.30)

print("Previsores de treinamento: " + str(len(previsores_treinamento)))
print("Previsores de treinamento: " + str(len(previsores_teste)))

print("Classe de treinamento: " + str(len(classe_treinamento)))
print("Classe de treinamento: " + str(len(classe_teste)))

# Configuração da RNA

import keras
from keras.models import Sequential 
from keras.layers import Dense
from keras.metrics import Precision, Recall
import tensorflow as tf

classificador = Sequential()
classificador.add(Dense(units= 16,activation="relu",kernel_initializer="random_uniform",input_dim=30))
classificador.add(Dense(units= 16,activation="relu",kernel_initializer="random_uniform"))
classificador.add(Dense(units= 1,activation="sigmoid",kernel_initializer="random_uniform"))

otimizador=keras.optimizers.Adam(learning_rate=0.001)
classificador.compile(optimizer=otimizador, loss="binary_crossentropy",metrics= ["accuracy",tf.keras.metrics.Precision() ,tf.keras.metrics.Recall()])

classificador.fit(previsores_treinamento,classe_treinamento,batch_size=10,epochs=100)

resultado = classificador.evaluate(previsores_teste, classe_teste)
print('Resultado: ' + str(resultado))