import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Leer el dataset desde un archivo CSV obtenido de Kaggle
ruta_dataset = r'C:\UNIVERSIDAD\8VO SEMESTRE\INTELIGENCIA_ARTIFICIAL\python\spam\archive\spam_ham_dataset.csv'
dataset = pd.read_csv(ruta_dataset, encoding='utf-8')

# Dividir los datos en entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(
    dataset['text'], dataset['label_num'], test_size=0.3, random_state=42
)

# Convertir texto en vectores de características
vectorizador = CountVectorizer()
X_entrenamiento_vec = vectorizador.fit_transform(X_entrenamiento)
X_prueba_vec = vectorizador.transform(X_prueba)

# Entrenar modelo
modelo = MultinomialNB()
modelo.fit(X_entrenamiento_vec, y_entrenamiento)

# Evaluar el modelo en el conjunto de prueba
predicciones_prueba = modelo.predict(X_prueba_vec)
print("Resultados en el conjunto de prueba:")
print(classification_report(y_prueba, predicciones_prueba))

# Evaluar nuevos correos
nuevos_correos = [
    "Haz click aquí para obtener un descuento",
    "Recordatorio: Tu reunión semanal",
    "Hola, ¿cómo estás?",
    "Tu cuenta ha sido bloqueada",
    "Dinero gratis, ¡aprovéchalo ya!"
]

X_nuevos = vectorizador.transform(nuevos_correos)
predicciones = modelo.predict(X_nuevos)

print("\nResultados para nuevos correos:")
for correo, pred in zip(nuevos_correos, predicciones):
    print(f"Correo: {correo} -> {'Spam' if pred == 1 else 'No Spam'}")
