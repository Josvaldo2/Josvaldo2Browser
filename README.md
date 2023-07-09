# Josvaldo2Browser
<img alt="Página inicial" src="https://github.com/Josvaldo2/Josvaldo2Browser/assets/59576112/e07993f2-4c30-4543-b25a-04cb88dc44e2" height=220>
<img alt="Pesquisa no Google" src="https://github.com/Josvaldo2/Josvaldo2Browser/assets/59576112/bd7f5ce3-c6e0-43bc-b8e0-72b9200bf99a" height=220>
<img alt="Página inicial da Wikipédia" src="https://github.com/Josvaldo2/Josvaldo2Browser/assets/59576112/cc493de4-5d14-4860-bb28-7f9606c44bd0" height=220>

Um navegador simples feito em python com o PyQt5 e PyQtWebEngine.  
Inicialmente ele foi feito em 2021 como um aplicativo simples para testar o PyQt5, mas fiz algumas modificações recentemente para deixá-lo mais interessante.
A versão antiga está na pasta `old`.

Para executar o navegador, você precisa primeiro [instalar o Python no seu computador](https://www.python.org/downloads), após isso você deve instalar os módulos
PyQt5 e PyQtWebEngine:

```bash
pip install PyQt5 PyQtWebEngine
```

Após isso, você pode abrir o navegador pelo arquivo `main.py`:

```bash
python main.py
```

Note que os arquivos `JosvaldoSearch.html`, `JosvaldoSearch.css` e `EpicFace.png` devem estar no mesmo diretório que `main.py` para carregar a página inicial
e o ícone do aplicativo corretamente.