def alterarPosicao(changePosition, change):
    """This looks complicated but I'm doing this:
    Current_pos == (x, y)
    change == (a, b)
    new_position == ((x + a), (y + b))
    """
    return (changePosition[0] + change[0]), (changePosition[1] + change[1])


posicaoAtual = (10, 1)

posicaoAtual = alterarPosicao(posicaoAtual, [-4, 2])
print(posicaoAtual)
# Prints: (6, 3)

posicaoAtual = alterarPosicao(posicaoAtual, [2, 5])
print(posicaoAtual)
# Prints: (8, 8)