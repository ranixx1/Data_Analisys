import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data =[np.random.normal(0,std,100) for std in range(1,4)]

sns.violinplot(data=data)
plt.title('Grafico Violino')
plt.xlabel('Categoria')
plt.ylabel('Valores')
plt.show()