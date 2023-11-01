import numpy as np

# Ejemplo de uso de números complejos
vector1 = np.array([0.3-0.2j, 0.7+0.1j, 0.5-0.4j, 0.6-0.3j, 0.2+0.5j])
position = 3
initial_vector = np.array([0.1+0.4j, 0.2-0.3j, 0.3-0.2j, 0.4-0.1j])
final_vector = np.array([0.7-0.3j, 0.5+0.2j, 0.4-0.5j, 0.3+0.6j])

# 1. Calcular la probabilidad
def calculate_probability(vector, position):
    amplitude = vector[position]
    probability = np.abs(amplitude)**2
    return probability

# 2. Calcular la probabilidad de transición
def calculate_transition_probability(initial_vector, final_vector):
    inner_product = np.vdot(initial_vector, final_vector)
    transition_probability = np.abs(inner_product)**2
    return transition_probability

print(f"La probabilidad de encontrar la partícula en la posición {position} es: {calculate_probability(vector1, position)}")
print(f"La probabilidad de transición de un vector inicial a otro es: {calculate_transition_probability(initial_vector, final_vector)}")

# 1. Amplitud de Transición
def transition_amplitude(vector1, vector2):
    transition = np.dot(np.conjugate(vector1), vector2)
    return np.abs(transition)**2

# 2. Media y Varianza del Observable
def calculate_mean_variance(observable_matrix, state):
    if np.allclose(observable_matrix, np.conjugate(np.transpose(observable_matrix))):
        mean = np.dot(np.conjugate(state), np.dot(observable_matrix, state))
        variance = np.dot(np.conjugate(state), np.dot(observable_matrix**2, state)) - np.abs(mean)**2
        return mean, variance
    else:
        return "La matriz no es hermitiana"

# 3. Cálculo de Valores Propios y Probabilidad de Transición a Vectores Propios
def calculate_eigenvalues_transition_probability(observable_matrix, state):
    if np.allclose(observable_matrix, np.conjugate(np.transpose(observable_matrix))):
        eigenvalues, eigenvectors = np.linalg.eigh(observable_matrix)
        transition_probability = np.abs(np.dot(np.conjugate(state), eigenvectors))**2
        return eigenvalues, transition_probability
    else:
        return "La matriz no es hermitiana"

# 4. Dinámica del Sistema
def dynamic_evolution(operation_matrices, initial_state):
    current_state = initial_state
    for operation_matrix in operation_matrices:
        current_state = np.dot(operation_matrix, current_state)
    return current_state

# Ejemplos de uso
# Números complejos se representan como a + bi, donde a y b son números reales y i es la unidad imaginaria.

# Para los puntos 1, 2 y 3
complex_vector1 = np.array([0.4-0.3j, 0.9+0.2j])
complex_vector2 = np.array([0.5-0.2j, 0.3+0.4j])
observable_matrix = np.array([0.6-0.6j, 0.7-0.2j],
                            [0.2-0.2j, 0.9-0.5j])
state = np.array([0.8+0.1j, 0.7-0.3j])

# Para el punto 4
operation_matrix1 = np.array([0.4+0.4j, 0.3+0.2j],
                            [0.2-0.4j, 0.7+0.1j])
operation_matrix2 = np.array([0.5-0.2j, 0.1+0.5j],
                            [0.6+0.3j, 0.4+0.7j])
operation_matrices = [operation_matrix1, operation_matrix2]

# Ejecutar las funciones
print("Amplitud de transición:", transition_amplitude(complex_vector1, complex_vector2))

mean, variance = calculate_mean_variance(observable_matrix, state)
print("Media del observable:", mean)
print("Varianza del observable:", variance)

eigenvalues, eigen_transition_probabilities = calculate_eigenvalues_transition_probability(observable_matrix, state)
print("Valores propios del observable:", eigenvalues)
print("Probabilidad de transición a vectores propios:", eigen_transition_probabilities)

final_state = dynamic_evolution(operation_matrices, state)
print("Estado final después de la dinámica del sistema:", final_state)
