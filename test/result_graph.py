import matplotlib.pyplot as plt

# Sample data
x_values = ["Kecil", "Sedang", "Besar"]
y_values = [0, 1, 217523]
y_values2 = [1968, 10276, 71146]
# Create a line graph
plt.plot(x_values, y_values, label='Hamiltonian Cycle')
plt.plot(x_values, y_values2, label='Hamiltonian Path')
# Add labels and title
plt.xlabel('Tipe dataset')
plt.ylabel('Waktu (dalam ms)')
plt.title('Perbandingan waktu Hamiltonian Algorithm')

# Add legend
plt.legend()

# Display the graph
plt.show()
