def rastrear_posicao(movimentos):
    # Inicializa as coordenadas
    x, y = 0, 0

    # Itera sobre os movimentos e ajusta as coordenadas
    for movimento in movimentos:
        if movimento == "norte":
            y += 1
        elif movimento == "sul":
            y -= 1
        elif movimento == "leste":
            x += 1
        elif movimento == "oeste":
            x -= 1
    
    # Retorna a posição final otimizada
    return x, y

# Exemplo de uso
movimentos = ["norte", "leste", "sul", "oeste", "norte", "leste"]
posicao_final = rastrear_posicao(movimentos)
print("Posição final otimizada:", posicao_final)
