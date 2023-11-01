### Raquel Selma

## Ejemplo de Cálculos con Números Complejos en Python
Este es un ejemplo de código en Python que realiza varios cálculos utilizando números complejos. Los cálculos se dividen en cuatro partes principales:

## 1. Cálculo de Probabilidad
En esta sección, calculamos la probabilidad de encontrar una partícula en una posición específica en un vector dado. También calculamos la probabilidad de transición de un vector inicial a otro.
import numpy as np

# Ejemplo de uso de números complejos

- vector1 = np.array([0.3-0.2j, 0.7+0.1j, 0.5-0.4j, 0.6-0.3j, 0.2+0.5j])
- position = 3
- initial_vector = np.array([0.1+0.4j, 0.2-0.3j, 0.3-0.2j, 0.4-0.1j])
- final_vector = np.array([0.7-0.3j, 0.5+0.2j, 0.4-0.5j, 0.3+0.6j])

- Función para calcular la probabilidad de encontrar una partícula en una posición
def calculate_probability(vector, position):
    ...

- Función para calcular la probabilidad de transición de un vector inicial a otro
def calculate_transition_probability(initial_vector, final_vector):
    ...

- Resultados
print(f"La probabilidad de encontrar la partícula en la posición {position} es: {calculate_probability(vector1, position)}")
print(f"La probabilidad de transición de un vector inicial a otro es: {calculate_transition_probability(initial_vector, final_vector)}")

## 2. Amplitud de Transición
En esta sección, calculamos la amplitud de transición entre dos vectores complejos.
- Función para calcular la amplitud de transición entre dos vectores
def transition_amplitude(vector1, vector2):
    ...

- Resultado
print("Amplitud de transición:", transition_amplitude(complex_vector1, complex_vector2))

## 3. Media, Varianza y Valores Propios
En esta sección, calculamos la media y la varianza de una matriz observable con números complejos. También calculamos los valores propios de la matriz observable y la probabilidad de transición a los vectores propios.
- Función para calcular la media y la varianza de una matriz observable
def calculate_mean_variance(observable_matrix, state):
    ...

- Función para calcular los valores propios y la probabilidad de transición a los vectores propios
def calculate_eigenvalues_transition_probability(observable_matrix, state):
    ...

- Resultados
print("Media del observable:", mean)
print("Varianza del observable:", variance)
print("Valores propios del observable:", eigenvalues)
print("Probabilidad de transición a vectores propios:", eigen_transition_probabilities)

## 4. Dinámica del Sistema
En esta sección, realizamos la evolución dinámica de un sistema utilizando matrices de operación.

- Función para la evolución dinámica del sistema
def dynamic_evolution(operation_matrices, initial_state):
    ...

- Resultado
print("Estado final después de la dinámica del sistema:", final_state)
