import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.hist(data, bins=30, edgecolor='black')
plt.title('Gráfico de histograma')
plt.xlabel('Values')
plt.ylabel('Frequência')
plt.show()