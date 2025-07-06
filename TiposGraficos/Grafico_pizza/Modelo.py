import matplotlib.pyplot as plt

labels =['Categoria A','Categoria B','Categoria C']
sizes = [30, 45, 25]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Grafico de pizza')
plt.show()