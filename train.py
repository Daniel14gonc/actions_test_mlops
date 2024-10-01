# train.py
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar dataset de ejemplo
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

# Definir modelo
clf = RandomForestClassifier()

# Entrenar modelo
clf.fit(X_train, y_train)

# Evaluar modelo
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Imprimir resultado
print(f"Accuracy: {accuracy * 100:.2f}%")