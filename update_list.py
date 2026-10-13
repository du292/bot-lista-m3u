from pathlib import Path
from urllib.request import Request, urlopen

URL = "https://gist.githubusercontent.com/ryan337/29e76ed198731cd3965d3bda0db10781/raw/6339eb3452e965a36460a9ec9add3726a7e1b31c/Canais.m3u"
DESTINO = Path("lista.m3u")

def main():
    pedido = Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urlopen(pedido, timeout=60) as resposta:
        conteudo = resposta.read()

    if not conteudo.lstrip().startswith(b"#EXTM3U"):
        raise ValueError("A resposta recebida nao e uma lista M3U valida.")

    DESTINO.write_bytes(conteudo)
    print(f"Lista salva: {DESTINO} ({len(conteudo)} bytes)")

if __name__ == "__main__":
    main()
