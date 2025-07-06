import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [25, 40, 30, 20]

plt.bar(categories,values)
plt.title('Grafico de barra')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.show()