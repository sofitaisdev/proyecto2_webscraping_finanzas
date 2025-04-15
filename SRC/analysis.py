import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(tesla_data, gme_data):
    # Convertir la columna de 'Revenue' a tipo numérico
    tesla_data['Revenue'] = tesla_data['Revenue'].astype(float)
    gme_data['Revenue'] = gme_data['Revenue'].astype(float)

    # Gráfico de Tesla
    plt.figure(figsize=(10,6))
    plt.plot(tesla_data['Date'], tesla_data['Revenue'], label='Tesla Revenue')
    plt.title('Tesla Revenue')
    plt.xlabel('Fecha')
    plt.ylabel('Ingresos')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Gráfico de GameStop
    plt.figure(figsize=(10,6))
    plt.plot(gme_data['Date'], gme_data['Revenue'], label='GameStop Revenue')
    plt.title('GameStop Revenue')
    plt.xlabel('Fecha')
    plt.ylabel('Ingresos')
    plt.legend()
    plt.grid(True)
    plt.show()
