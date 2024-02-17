#!/bin/env python3
import sys
def sanitize(words, banned):
    sanitized_list = []

    for word in words:
        if any(banned_word in word for banned_word in banned):
            sanitized_list.append("BANNED")
        else:
            sanitized_list.append("SAFE")

    return sanitized_list

# Apri il file di input in modalità lettura
with open("2024-sanitization_sanitization-1_1707834532.txt", "r") as fin:
    N, M = map(int, fin.readline().strip().split())

    if not (1 <= N <= 1000 and 1 <= M <= 100):
        print("Errore: le dimensioni non sono nel range consentito.")
        sys.exit(1)

    words = []
    banned = []

    for _ in range(M):
        banned.append(fin.readline().strip())

    for _ in range(N):
        words.append(fin.readline().strip())

# Chiama la funzione sanitize
ans = sanitize(words, banned)

# Apri il file di output in modalità scrittura
with open("output.txt", "w") as fout:
    for a in ans:
        fout.write(a + "\n")
