def recall_password(cipher_grille, ciphered_password):
    grille = sorted((x, y) for x in range(4) for y in range(4) if cipher_grille[x][y] == 'X')
    ans = []
    for i in range(4):
        ans.extend(ciphered_password[g[0]][g[1]] for g in grille)
        grille = sorted((y, 3 - x) for (x, y) in grille)
    return ''.join(ans)
