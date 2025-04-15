import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_tesla_revenue():
    # URL de la página de finanzas de Tesla
    url = 'https://finance.yahoo.com/quote/TSLA/financials'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar la tabla con los datos de ingresos
    table = soup.find_all('table')[0]
    
    # Obtener los nombres de las columnas
    columns = [col.text for col in table.find_all('th')]
    
    # Obtener las filas de la tabla
    rows = []
    for row in table.find_all('tr')[1:]:
        rows.append([cell.text.strip() for cell in row.find_all('td')])
    
    # Convertir los datos a un DataFrame
    tesla_revenue = pd.DataFrame(rows, columns=columns)
    return tesla_revenue

def get_gme_revenue():
    # URL de la página de finanzas de GameStop
    url = 'https://finance.yahoo.com/quote/GME/financials'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontrar la tabla con los datos de ingresos
    table = soup.find_all('table')[0]
    
    # Obtener los nombres de las columnas
    columns = [col.text for col in table.find_all('th')]
    
    # Obtener las filas de la tabla
    rows = []
    for row in table.find_all('tr')[1:]:
        rows.append([cell.text.strip() for cell in row.find_all('td')])
    
    # Convertir los datos a un DataFrame
    gme_revenue = pd.DataFrame(rows, columns=columns)
    return gme_revenue