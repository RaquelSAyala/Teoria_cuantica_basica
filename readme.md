### Raquel Selma

# Simulador de Posición y Dinámica Cuántica

Este es un programa que realiza cálculos y simulaciones relacionados con conceptos de física cuántica, como probabilidad, amplitud de transición, media y varianza del observable, cálculo de valores propios y probabilidad de transición a vectores propios, y dinámica de sistemas cuánticos.

## Uso
El programa incluye varias funciones que puedes utilizar. Aquí hay un resumen de lo que hace cada función:

### 1. Calcular la Probabilidad
- calculate_probability(vector, position)

Esta función calcula la probabilidad de encontrar una partícula en una posición dada en un vector de amplitudes.

### 2. Calcular la Probabilidad de Transición
- calculate_transition_probability(initial_vector, final_vector)

Esta función calcula la probabilidad de transición entre dos vectores iniciales y finales.

### 3. Amplitud de Transición
- transition_amplitude(vector1, vector2)

Calcula la amplitud de transición entre dos vectores.

### 4. Media y Varianza del Observable
- calculate_mean_variance(observable_matrix, state)

Calcula la media y la varianza del observable representado por una matriz hermitiana y un estado.

### 5. Cálculo de Valores Propios y Probabilidad de Transición a Vectores Propios
- calculate_eigenvalues_transition_probability(observable_matrix, state)

Calcula los valores propios de una matriz hermitiana y la probabilidad de transición a los vectores propios correspondientes.

### 6. Dinámica del Sistema
- dynamic_evolution(operation_matrices, initial_state)

Simula la dinámica de un sistema cuántico utilizando una lista de matrices de operación y un estado inicial.

## Ejemplos de Uso
El archivo de código contiene ejemplos de uso de estas funciones para que puedas comprender cómo funcionan.


- Resultado
print("Estado final después de la dinámica del sistema:", final_state)
