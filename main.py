"""
Projecto #1 - JOGO DO GALO

FUNDAMENTOS DA PROGRAMACAO

EDSON DA VEIGA - IST1100731
"""


# Certifica se o argumento introduzido eh um tabuleiro
def eh_tabuleiro(tab):  # eh tabuleiro: universal -> booleano
    if not isinstance(tab, tuple) or len(tab) != 3:
        return False
    for indice_1 in tab:
        if not isinstance(indice_1, tuple) or len(indice_1) != 3:
            return False
        for indice_2 in indice_1:
            if not isinstance(indice_2, int) or indice_2 < -1 or indice_2 > 1 or isinstance(indice_2, bool):
                return False
    else:
        return True


# Certifica se o argumento introduzido eh uma posicao
def eh_posicao(numero):  # eh posicao: universal -> booleano
    if not isinstance(numero, int) or isinstance(numero, bool) or numero < 1 or numero > 9:
        return False
    else:
        return True


# Devolve um vector com os valoes da coluna solicitada
def obter_coluna(tab, numero):  # obter coluna: tabuleiro x inteiro -> vector
    if eh_tabuleiro(tab) and not isinstance(numero, bool) and 1 <= numero <= 3:
        return tab[0][numero - 1], tab[1][numero - 1], tab[2][numero - 1]
    else:
        raise ValueError("obter_coluna: algum dos argumentos e invalido")


# Devolve um vector com os valoes da linha solicitada
def obter_linha(tab, numero):  # obter linha: tabuleiro x inteiro -> vector
    if eh_tabuleiro(tab) and not isinstance(numero, bool) and numero in (1, 2, 3):
        return tab[numero - 1][0], tab[numero - 1][1], tab[numero - 1][2]
    else:
        raise ValueError("obter_linha: algum dos argumentos e invalido")


# Devolve um vector com os valoes da diagonal solicitada
def obter_diagonal(tab, numero):  # obter diagonal: tabuleiro x inteiro -> vector
    if eh_tabuleiro(tab) and not isinstance(numero, bool) and numero in (1, 2):
        if numero == 1:
            return tab[0][0], tab[1][1], tab[2][2]
        else:
            return tab[2][0], tab[1][1], tab[0][2]
    else:
        raise ValueError("obter_diagonal: algum dos argumentos e invalido")


# Rebece um tuplo e devolve um dicionario
def transforma_tuplo_em_dicionario(tab):  # transforma_tuplo_em_dicionario: tabuleiro -> dicionario
    return {1: tab[0][0], 2: tab[0][1], 3: tab[0][2], 4: tab[1][0], 5: tab[1][1],
            6: tab[1][2], 7: tab[2][0], 8: tab[2][1], 9: tab[2][2]}


# Recebe um tabuleiro e devolve a cadeia de caracteres que o representa
def tabuleiro_str(tab):  # tabuleiro str: tabuleiro -> cad. carateres
    if eh_tabuleiro(tab):
        tab_dict = transforma_tuplo_em_dicionario(tab)
        for key in tab_dict:
            if tab_dict[key] == -1:
                tab_dict[key] = 'O'
            elif tab_dict[key] == 1:
                tab_dict[key] = 'X'
            elif tab_dict[key] == 0:
                tab_dict[key] = ' '
        return " " + tab_dict[1] + " | " + tab_dict[2] + " | " + tab_dict[3] + " " + "\n-----------\n" + \
               " " + tab_dict[4] + " | " + tab_dict[5] + " | " + tab_dict[6] + " " + "\n-----------\n" + \
               " " + tab_dict[7] + " | " + tab_dict[8] + " | " + tab_dict[9] + " "
    else:
        raise ValueError("tabuleiro_str: o argumento e invalido")


# Recebe um tabuleiro e uma posicao, e verifica se corresponde a uma posicão livre do tabuleiro
def eh_posicao_livre(tab, numero):  # eh posicao livre: tabuleiro x posicao -> booleano
    if eh_tabuleiro(tab) and eh_posicao(numero):
        tab_dict = transforma_tuplo_em_dicionario(tab)
        if tab_dict[numero] == 0:
            return True
        else:
            return False
    else:
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido")


# Devolve um vector ordenado com todas as posicoes livres do tabuleiro
def obter_posicoes_livres(tab):  # obter posicoes livres: tabuleiro -> vector
    posicoes_livres = []
    if eh_tabuleiro(tab):
        tab_dict = transforma_tuplo_em_dicionario(tab)
        for key in tab_dict:
            if eh_posicao_livre(tab, key):
                posicoes_livres.append(key)
        return tuple(posicoes_livres)
    else:
        raise ValueError("obter_posicoes_livres: o argumento e invalido")


# Confere a igualde entre tres argumentos
def comparador(numeros):  # comparador: tuplo -> booleano
    if numeros[0] == numeros[1] == numeros[2]:
        return True


# devolve um valor inteiro a indicar o jogador que ganhou a partida
def jogador_ganhador(tab):  # jogador ganhador: tabuleiro -> inteiro
    indice_1 = 1
    if eh_tabuleiro(tab):
        while indice_1 < 4:
            coluna = obter_coluna(tab, indice_1)
            linha = obter_linha(tab, indice_1)
            if indice_1 < 3:
                diagonal = obter_diagonal(tab, indice_1)
                if comparador(diagonal):
                    return diagonal[0]
            if comparador(coluna):
                return coluna[0]
            elif comparador(linha):
                return linha[0]
            indice_1 += 1
        else:
            return 0
    else:
        raise ValueError("jogador_ganhador: o argumento e invalido")


# devolve um novo tabuleiro modificado com uma nova marca do jogador nessa posicao
def marcar_posicao(tab, jogador, posicao):  # marcar posicao: tabuleiro x inteiro x posicao -> tabuleiro
    tab_dict = transforma_tuplo_em_dicionario(tab)
    if eh_tabuleiro(tab) and eh_posicao(posicao) and tab_dict[posicao] != jogador \
            and not isinstance(jogador, bool) and -1 <= jogador <= 1:
        tab_dict[posicao] = jogador
        return (tab_dict[1], tab_dict[2], tab_dict[3]), (tab_dict[4], tab_dict[5], tab_dict[6]), \
               (tab_dict[7], tab_dict[8], tab_dict[9])
    else:
        raise ValueError("marcar_posicao: algum dos argumentos e invalido")


# Le a posicao introduzida manualmente por um jogador e devolve esta posicao escolhida
def escolher_posicao_manual(tab):  # escolher posicao manual: tabuleiro -> posicao
    if eh_tabuleiro(tab):
        posicao = int(input("Turno do jogador. Escolha uma posicao livre: "))
        if eh_posicao(posicao) and eh_posicao_livre(tab, posicao):
            return posicao
        else:
            raise ValueError("escolher_posicao_manual: a posicao introduzida e invalida")
    else:
        raise ValueError("escolher_posicao_manual: o argumento e invalido")


# Verifica se existem dois elementos iguais em um tuplo
def comparador_2(conjunto, jogador, tab):  # comparador_2: tuplo x jogador x tabuleiro -> posicao
    tab_dict = transforma_tuplo_em_dicionario(tab)
    jog = 0
    for i in conjunto:
        if tab_dict[i] == jogador:
            jog += 1
    if jog == 2:
        return True
    else:
        return False


# De acordo com as posicoes vazias analiza verifica existencia
# de uma jogoda que implica vitoria ou bloquiar a vitoria do adversario
def vitoria_bloqueio(tab, jogador):  # vitoria_bloqueio: tabuleiro x jogador -> posicao
    vazios = obter_posicoes_livres(tab)
    for indice_1 in vazios:
        # linha
        if indice_1 < 4:
            if comparador_2((1, 2, 3), jogador, tab):
                return indice_1
        if indice_1 in (4, 5, 6):
            if comparador_2((4, 5, 6), jogador, tab):
                return indice_1
        if indice_1 in (7, 8, 9):
            if comparador_2((7, 8, 9), jogador, tab):
                return indice_1
        # coluna
        if indice_1 in (1, 4, 7):
            if comparador_2((1, 4, 7), jogador, tab):
                return indice_1
        if indice_1 in (2, 5, 8):
            if comparador_2((2, 5, 8), jogador, tab):
                return indice_1
        if indice_1 in (3, 6, 9):
            if comparador_2((3, 6, 9), jogador, tab):
                return indice_1
        # diagonal
        if indice_1 in (1, 5, 9):
            if comparador_2((1, 5, 9), jogador, tab):
                return indice_1
        if indice_1 in (3, 5, 7):
            if comparador_2((3, 5, 7), jogador, tab):
                return indice_1


# Devolve as posicoes ocupadas por um determinado jogador
def obter_posicoes_ocupadas(tab, jogador):  # obter_posicoes_ocupadas: tabuleiro x jogador -> tuplo
    posicoes_ocupadas = []
    tab_dict = transforma_tuplo_em_dicionario(tab)
    for key in tab_dict:
        if tab_dict[key] == jogador:
            posicoes_ocupadas.append(key)
    return tuple(posicoes_ocupadas)


# Verifica as posibilidades de bifurcacao e devolve uma lista com as jogadas possiveis
'''A partir de tres cenarios (centro vazio, centro ocupado por 1 e por -1) 
analisa as possibilidades de bifurcacao'''


def bifurcacao(tab, jogador):  # bifurcacao: tabuleiro x jogador -> lista
    vazios = obter_posicoes_livres(tab)
    if jogador == 1:
        jogador_2 = -1
    else:
        jogador_2 = 1
    posicoes_ocupadas = obter_posicoes_ocupadas(tab, jogador)
    posicoes_ocupadas_2 = obter_posicoes_ocupadas(tab, jogador_2)
    burifadas = [10]
    # centro vazio
    if 5 in vazios:
        if 1 in posicoes_ocupadas and (3 or 7 in posicoes_ocupadas) and ((7 or 9 in vazios) or (3 or 9 in vazios)):
            burifadas += [5]
        if 9 in posicoes_ocupadas and (3 or 7 in posicoes_ocupadas) and ((1 or 3 in vazios) or (1 or 7 in vazios)):
            burifadas += [5]
    # centro ocupado pelo jogador
    if 5 in posicoes_ocupadas:
        if 7 in posicoes_ocupadas:
            if 4 in vazios:
                if (1 and 9) in vazios:
                    burifadas += [1, 9]
                if 8 in vazios:
                    burifadas += [8]
                if (8 and 9) in vazios:
                    burifadas += [8, 9]
            else:
                if 9 in vazios:
                    burifadas += [9]
                if 8 in vazios:
                    burifadas += [8]
        if 3 in posicoes_ocupadas:
            if 6 in vazios:
                if (1 and 9) in vazios:
                    burifadas += [1, 9]
                if 8 in vazios:
                    burifadas += [8]
                if (8 and 9) in vazios:
                    burifadas += [8, 9]
            else:
                if 9 in vazios:
                    burifadas += [9]
                elif 8 in vazios:
                    burifadas += [8]
        if 9 in posicoes_ocupadas:
            if 6 in vazios:
                if (3 and 7) in vazios:
                    burifadas += [3, 7]
                if 8 in vazios:
                    burifadas += [8]
                if (7 and 8) in vazios:
                    burifadas += [8, 7]
            else:
                if 7 in vazios:
                    burifadas += [7]
                if 8 in vazios:
                    burifadas += [8]
        if 1 in posicoes_ocupadas:
            if 4 in vazios:
                if (3 and 7) in vazios:
                    burifadas += [3, 7]
                if 8 in vazios:
                    burifadas += [8]
                if (7 and 8) in vazios:
                    burifadas += [8, 7]
            else:
                if 7 in vazios:
                    burifadas += [7]
                if 8 in vazios:
                    burifadas += [8]
    # centro ocupado pelo jogador_2
    if 5 in posicoes_ocupadas_2:
        if (1 and 9) in posicoes_ocupadas:
            if 3 in vazios:
                burifadas += [3]
            if 7 in vazios:
                burifadas += [7]
        if (3 and 7) in posicoes_ocupadas:
            if 1 in vazios:
                burifadas += [1]
            if 9 in vazios:
                burifadas += [9]
    burifadas.sort()
    return burifadas


# Verifica as posibilidades de bloquiar bifurcacao
def bloqueio_de_bifurcacao(tab, jogador_2):  # bloqueio_de_bifurcacao: tabuleiro x jogador -> posicao
    vazios = obter_posicoes_livres(tab)
    bifur = bifurcacao(tab, jogador_2)
    # caso o adversario tenha apenas uma bifurcacao
    if len(bifur) == 2:
        return bifur[0]
    # caso o adversario tenha mais do que uma bifurcacao
    if len(bifur) > 2:
        for indice_1 in vazios:
            if indice_1 < 4:
                if comparador_2((1, 2, 3), 0, tab) and indice_1 not in bifur:
                    return indice_1
            if indice_1 in (4, 5, 6):
                if comparador_2((4, 5, 6), 0, tab) and indice_1 not in bifur:
                    return indice_1
            if indice_1 in (7, 8, 9):
                if comparador_2((7, 8, 9), 0, tab) and indice_1 not in bifur:
                    return indice_1
            # coluna
            if indice_1 in (1, 4, 7):
                if comparador_2((1, 4, 7), 0, tab) and indice_1 not in bifur:
                    return indice_1
            if indice_1 in (2, 5, 8):
                if comparador_2((2, 5, 8), 0, tab) and indice_1 not in bifur:
                    return indice_1
            if indice_1 in (3, 6, 9):
                if comparador_2((3, 6, 9), 0, tab) and indice_1 not in bifur:
                    return indice_1
            # diagonal
            if indice_1 in (1, 5, 9):
                if comparador_2((1, 5, 9), 0, tab) and indice_1 not in bifur:
                    return indice_1
            if indice_1 in (3, 5, 7):
                if comparador_2((3, 5, 7), 0, tab) and indice_1 not in bifur:
                    return indice_1
    return 0


# Joga no canto diagonalmente oposto ao do adversario, se estiver livre
def canto_oposto(tab, jogador):  # canto_oposto: tabuleiro x jogador -> posicao
    vazios = obter_posicoes_livres(tab)
    tab_dict = transforma_tuplo_em_dicionario(tab)
    if jogador == 1:
        jogador_2 = -1
    else:
        jogador_2 = 1
    for indice_1 in vazios:
        # verifica a diagonal 1
        if indice_1 in (1, 9):
            for indice_2 in (1, 9):
                if indice_2 != indice_1 and tab_dict[indice_2] == jogador_2:
                    return indice_1
        # verifica a diagonal 2
        if indice_1 in (3, 7):
            for indice_2 in (3, 7):
                if indice_2 != indice_1 and tab_dict[indice_2] == jogador_2:
                    return indice_1
    return 0


# Seleciona as jogadas para o nivel basico
def jogo_basico(tab):  # jogo_basico: tabuleiro -> posicao
    tab_dict = transforma_tuplo_em_dicionario(tab)
    posicao_a_jogar = -1
    for key in (9, 7, 3, 1, 5):
        # analiza as opcoes de posicoes com vazias e seleciona a jogada de acordo com a estrategia
        if tab_dict[key] == 0:
            posicao_a_jogar = key
    if posicao_a_jogar != -1:
        return posicao_a_jogar
    # seleciona a primeira posicao livre possivel
    else:
        return obter_posicoes_livres(tab)[0]


# Seleciona as jogadas para o nivel normal
def jogo_normal(tab, jogador):  # jogo_normal: tabuleiro x jogador -> posicao
    vazios = obter_posicoes_livres(tab)
    if jogador == 1:
        jogador_2 = -1
    else:
        jogador_2 = 1
    # vitoria
    if vitoria_bloqueio(tab, jogador) in vazios:
        return vitoria_bloqueio(tab, jogador)
    # bloqueio
    if vitoria_bloqueio(tab, jogador_2) in vazios:
        return vitoria_bloqueio(tab, jogador_2)
    # centro
    if 5 in vazios:
        return 5
    # canto oposto
    if canto_oposto(tab, jogador):
        return canto_oposto(tab, jogador)
    # canto vazio -> lateral vazio
    else:
        return jogo_basico(tab)


# Seleciona as jogadas para o nivel perfeito
def jogo_perfeito(tab, jogador):  # jogo_perfeito: tabuleiro x jogador -> posicao
    vazios = obter_posicoes_livres(tab)
    if jogador == 1:
        jogador_2 = -1
    else:
        jogador_2 = 1
    posicoes_ocupadas_2 = obter_posicoes_ocupadas(tab, jogador_2)
    if len(vazios) == 9:
        return 2
    if len(vazios) == 8:
        if 5 in vazios:
            for indice_1 in posicoes_ocupadas_2:
                if indice_1 in (1, 3, 7, 9):
                    return 5
                if indice_1 in (2, 4, 6, 8):
                    if indice_1 == (2 or 4):
                        return 1
                    if indice_1 == 6:
                        return 3
                    if indice_1 == 8:
                        return 7
        else:
            return 1
    if len(vazios) == 7:
        if tab[0][1] == jogador:
            if tab[1][1] == 0:
                if 1 in posicoes_ocupadas_2:
                    return 7
                if 3 in posicoes_ocupadas_2 or 8 in posicoes_ocupadas_2:
                    return 9
                if 7 in posicoes_ocupadas_2 or 4 in posicoes_ocupadas_2:
                    return 1
                if 9 in posicoes_ocupadas_2 or 6 in posicoes_ocupadas_2:
                    return 3
            if tab[1][1] == jogador_2:
                return 4
    # vitoria
    if vitoria_bloqueio(tab, jogador) in vazios:
        return vitoria_bloqueio(tab, jogador)
    # bloqueio
    if vitoria_bloqueio(tab, jogador_2) in vazios:
        return vitoria_bloqueio(tab, jogador_2)
    # bifurcacao
    bifur = min(bifurcacao(tab, jogador))
    if bifur in vazios:
        return bifur
    # bloqueio de bifurcacao
    if bloqueio_de_bifurcacao(tab, jogador_2) in vazios:
        return bloqueio_de_bifurcacao(tab, jogador_2)
    # centro
    if 5 in vazios:
        return 5
    # canto oposto
    if canto_oposto(tab, jogador):
        return canto_oposto(tab, jogador)
    # canto vazio -> lateral vazio
    else:
        return jogo_basico(tab)


# Devolve a posicao escolhida automaticamente de acordo com a estrategia seleccionada
def escolher_posicao_auto(tab, jogador,
                          estrategia):  # escolher posicao auto: tabuleiro x inteiro x cad. carateres -> posicao
    if eh_tabuleiro(tab) and estrategia in ("basico", "normal", "perfeito") \
            and (jogador == -1 or jogador == 1) and not isinstance(jogador, bool):
        if estrategia == "basico":
            return jogo_basico(tab)
        if estrategia == "normal":
            return jogo_normal(tab, jogador)
        if estrategia == "perfeito":
            return jogo_perfeito(tab, jogador)
    else:
        raise ValueError("escolher_posicao_auto: algum dos argumentos e invalido")


# Aciona as jogas do computador
def computador(tab, jogador, estrategia):  # computador: tabuleiro x jogador x estrategia -> cad. carateres
    tab = marcar_posicao(tab, jogador, escolher_posicao_auto(tab, jogador, estrategia))
    print("Turno do computador (" + estrategia + "):\n" + tabuleiro_str(tab))
    # verifica se ha ganhador
    if jogador_ganhador(tab) != 0:
        if jogador_ganhador(tab) == 1:
            return "X"
        else:
            return "O"
    elif len(obter_posicoes_livres(tab)) == 0:
        return "EMPATE"
    # se nao houver ganhador manda o jogador jogar
    else:
        return humano(tab, human, estrategia)


# Aciona as jogas do jogador
def humano(tab, jogador, estrategia):  # humano: tabuleiro x jogador x estrategia -> cad. carateres
    posicao = escolher_posicao_manual(tab)
    tab = marcar_posicao(tab, jogador, posicao)
    print(tabuleiro_str(tab))
    # verifica se ha ganhador
    if jogador_ganhador(tab) != 0:
        if jogador_ganhador(tab) == 1:
            return "X"
        else:
            return "O"
    elif len(obter_posicoes_livres(tab)) == 0:
        return "EMPATE"
    # se nao houver ganhador manda o jogador jogar
    else:
        return computador(tab, cpu, estrategia)


# Permite jogar um jogo completo de Jogo do Galo de um jogador contra o computador
def jogo_do_galo(simbolo, estrategia):  # jogo do galo: cad. carateres Öcad. carateres -> cad. carateres
    tab = ((0, 0, 0), (0, 0, 0), (0, 0, 0))
    if simbolo in ('X', 'O') and estrategia in ("basico", "normal", "perfeito"):
        global human
        global cpu
        if simbolo == 'X':
            human = 1
            cpu = -1
        else:
            human = -1
            cpu = 1
        # iniciacao do jogo caso jogador escolher 'X'
        if simbolo == 'X':
            print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'X'.")
            posicao = escolher_posicao_manual(tab)
            tab = marcar_posicao(tab, 1, posicao)
            print(tabuleiro_str(tab))
            return computador(tab, cpu, estrategia)
        # iniciacao do jogo caso jogador escolher 'O'
        else:
            print("Bem-vindo ao JOGO DO GALO.\nO jogador joga com 'O'.")
            return computador(tab, cpu, estrategia)
    else:
        raise ValueError("jogo_do_galo: algum dos argumentos e invalido")

tab = ((0,0,0),(0,-1,1),(0,1,0))
print(escolher_posicao_auto(tab, -1, 'perfeito'))