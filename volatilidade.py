import numpy as np
import pandas as pd
import requests

# Normalmente se usa volatilidade histórica para fazer esse cálculo, mas para o que eu* pretendo fazer é mais viável calcular o desvio padrão das últimas velas.
fechamento = pd.Series([10.00, 10.50, 11.00, 10.75, 10.80, 10.90, 11.20, 11.50, 11.80, 12.00])

# Cálculo do desvio padrão dos preços de fechamento
volatilidade= np.std(fechamento)

print("Desvio padrão dos preços de fechamento: ", volatilidade)

