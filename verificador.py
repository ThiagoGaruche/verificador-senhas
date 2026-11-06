import getpass
import hashlib
import math
import string

import requests

API_URL = "https://api.pwnedpasswords.com/range/"


def calcular_entropia(senha: str) -> float:
    """Estima a entropia em bits com base no tamanho e nos tipos de caracteres."""
    pool = 0
    if any(c in string.ascii_lowercase for c in senha):
        pool += 26
    if any(c in string.ascii_uppercase for c in senha):
        pool += 26
    if any(c in string.digits for c in senha):
        pool += 10
    if any(c in string.punctuation for c in senha):
        pool += len(string.punctuation)
    return len(senha) * math.log2(pool) if pool else 0.0


def classificar(entropia: float) -> str:
    if entropia < 40:
        return "Fraca"
    if entropia < 60:
        return "Razoável"
    if entropia < 80:
        return "Forte"
    return "Muito forte"


def verificar_vazamento(senha: str) -> int:
    """Retorna quantas vezes a senha apareceu em vazamentos (0 = não encontrada)."""
    sha1 = hashlib.sha1(senha.encode("utf-8")).hexdigest().upper()
    prefixo, sufixo = sha1[:5], sha1[5:]

    resposta = requests.get(API_URL + prefixo, timeout=10)
    resposta.raise_for_status()

    for linha in resposta.text.splitlines():
        hash_sufixo, contagem = linha.split(":")
        if hash_sufixo == sufixo:
            return int(contagem)
    return 0


def main():
    senha = getpass.getpass("Digite a senha a ser verificada: ")

    entropia = calcular_entropia(senha)
    print(f"\nTamanho: {len(senha)} caracteres")
    print(f"Entropia estimada: {entropia:.1f} bits ({classificar(entropia)})")

    try:
        vezes = verificar_vazamento(senha)
        if vezes:
            print(f"ATENÇÃO: esta senha apareceu {vezes:,} vezes em vazamentos. Não use!")
        else:
            print("Não encontrada em vazamentos conhecidos.")
    except requests.RequestException as erro:
        print(f"Não foi possível consultar a API: {erro}")


if __name__ == "__main__":
    main()
