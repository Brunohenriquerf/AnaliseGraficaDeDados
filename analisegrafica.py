# -*- coding: utf-8 -*-
"""Curso.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lXT2XXQfzV39q47sxaSZkQOMkxYJv3fl
"""

!pip install plotly --upgrade

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credito = pd.read_csv('/content/credit_data.csv')

sns.countplot(x=base_credito['default']);

plt.hist(x=base_credito['age']);

plt.hist(x=base_credito['income']);

plt.hist(x=base_credito['loan']);

grafico = px.scatter_matrix(base_credito, dimensions=['age', 'income', 'loan'], color='default')
grafico.show()
