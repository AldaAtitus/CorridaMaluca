def calc_dist_prim_seg(movXcar1, movXcar2, movXcar3): 
    posicoes = [movXcar1, movXcar2, movXcar3] 
    primeiro = max(posicoes) 
    posicoes.remove(primeiro) 
    segundo = max(posicoes) 
    return primeiro - segundo

def calc_dist_terc_seg(movXcar1, movXcar2, movXcar3): 
    posicoes = [movXcar1, movXcar2, movXcar3] 
    terceiro = min(posicoes) 
    posicoes.remove(terceiro) 
    segundo = min(posicoes) 
    return segundo - terceiro
