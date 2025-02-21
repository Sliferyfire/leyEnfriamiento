# Ajuste de Curva Exponencial con Python

Este repositorio contiene un script en Python que ajusta una curva exponencial a un conjunto de datos experimentales utilizando la biblioteca `scipy.optimize.curve_fit`. El ajuste se basa en un modelo exponencial y los parámetros obtenidos se utilizan para graficar la curva junto con los datos originales.

## Requisitos

Para ejecutar el script, necesitas instalar las siguientes bibliotecas de Python:

```bash
pip install numpy scipy matplotlib
```

## Uso

Ejecuta el script con:

```bash
python main.py
```

El script:
1. Define un modelo exponencial.
2. Usa datos de tiempo y temperatura como ejemplo.
3. Ajusta la curva con `curve_fit`.
4. Imprime los parámetros óptimos.
5. Genera una gráfica comparando los datos con la curva ajustada.

## Modelo Matemático

La función utilizada para el ajuste es:

\[ T(t) = A \cdot e^{-B \cdot t} + C \]

donde:
- \( A \) es el coeficiente inicial.
- \( B \) es el coeficiente de decaimiento.
- \( C \) es el valor asintótico de la temperatura.

## Resultados

El script muestra los valores óptimos de \( A \), \( B \) y \( C \) y genera una gráfica que compara los datos experimentales con la curva ajustada.



