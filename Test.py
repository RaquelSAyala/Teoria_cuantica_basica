import unittest
from Simulador_posicion import calculate_probability, calculate_transition_probability, transition_amplitude, calculate_mean_variance, calculate_eigenvalues_transition_probability, dynamic_evolution
import numpy as np

class TestComplexCalculations(unittest.TestCase):

    def test_calculate_probability(self):
        vector = np.array([0.3-0.2j, 0.7+0.1j, 0.5-0.4j, 0.6-0.3j, 0.2+0.5j])
        position = 3
        result = calculate_probability(vector, position)
        self.assertAlmostEqual(result, 0.09, places=2)

    def test_calculate_transition_probability(self):
        initial_vector = np.array([0.1+0.4j, 0.2-0.3j, 0.3-0.2j, 0.4-0.1j])
        final_vector = np.array([0.7-0.3j, 0.5+0.2j, 0.4-0.5j, 0.3+0.6j])
        result = calculate_transition_probability(initial_vector, final_vector)
        self.assertAlmostEqual(result, 0.25, places=2)

    def test_transition_amplitude(self):
        vector1 = np.array([0.3-0.2j, 0.7+0.1j, 0.5-0.4j, 0.6-0.3j, 0.2+0.5j])
        vector2 = np.array([0.4-0.3j, 0.9+0.2j])
        result = transition_amplitude(vector1, vector2)
        self.assertAlmostEqual(result, 0.0225, places=4)

    def test_calculate_mean_variance(self):
        observable_matrix = np.array([[0.6-0.6j, 0.7-0.2j], [0.2-0.2j, 0.9-0.5j]])
        state = np.array([0.8+0.1j, 0.7-0.3j])
        mean, variance = calculate_mean_variance(observable_matrix, state)
        self.assertAlmostEqual(mean, 0.63, places=2)
        self.assertAlmostEqual(variance, 0.0315, places=4)

    def test_calculate_eigenvalues_transition_probability(self):
        observable_matrix = np.array([[0.6-0.6j, 0.7-0.2j], [0.2-0.2j, 0.9-0.5j]])
        eigenvalues, eigen_transition_probabilities = calculate_eigenvalues_transition_probability(observable_matrix, state)
        self.assertAlmostEqual(eigenvalues[0], 0.3, places=2)
        self.assertAlmostEqual(eigenvalues[1], 1.2, places=2)
        self.assertAlmostEqual(eigen_transition_probabilities[0], 0.92, places=2)
        self.assertAlmostEqual(eigen_transition_probabilities[1], 0.08, places=2)

    def test_dynamic_evolution(self):
        operation_matrix1 = np.array([[0.4+0.4j, 0.3+0.2j], [0.2-0.4j, 0.7+0.1j]])
        operation_matrix2 = np.array([[0.5 - 0.2j, 0.1 + 0.5j], [0.6 + 0.3j, 0.4 + 0.7j]])
        operation_matrices = [operation_matrix1, operation_matrix2]
        initial_state = np.array([0.8+0.1j, 0.7-0.3j])
        result = dynamic_evolution(operation_matrices, initial_state)
        expected_result = np.array([0.945-0.385j, 0.85+0.41j])
        self.assertTrue(np.allclose(result, expected_result, rtol=1e-2))

if __name__ == '__main__':
    unittest.main()
