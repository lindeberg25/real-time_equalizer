from __future__ import division
 
import numpy as np
 
def gerarFiltro(FL, FH, B): 

    fL = FL  # frequencia de corte como uma fração da taxa de amostragem (in (0, 0.5)).
    fH = FH  # frequencia de corte como uma fração da taxa de amostragem  (in (0, 0.5)).
    b = B  # Banda de transição como uma fração da taxa de amostragem (in (0, 0.5)).
    N = int(np.ceil((4 / b)))
    n = np.arange(N)
    
    # computa um filtro passa baixa com frequencia de corte fH
    hpassabaixa = np.sinc(2 * fH * (n - (N - 1) / 2))
    hpassabaixa = hpassabaixa * np.blackman(N)
    hpassabaixa = hpassabaixa / np.sum(hpassabaixa)
    
    # Computa um filtro passa alta frequencia fL
    hpassaalta = np.sinc(2 * fL * (n - (N - 1) / 2))
    hpassaalta = hpassaalta * np.blackman(N)
    hpassaalta = hpassaalta / np.sum(hpassaalta)
    hpassaalta = -hpassaalta
    hpassaalta[(N - 1) // 2] += 1
    
    #Convolui ambos os filtros.
    h = np.convolve(hpassabaixa, hpassaalta)
    return h