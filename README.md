# Stealth - Automatizador de Teclas

Aplicativo em Python que automatiza o pressionamento da tecla LSHIFT a cada 5 segundos.

## Funcionalidades

- **Botão Ativar**: Inicia a automação da tecla LSHIFT (pressionada a cada 5 segundos)
- **Botão Desativar**: Para a automação
- Interface gráfica simples e intuitiva
- Status em tempo real da automação

## Instalação

1. Certifique-se de ter o Python 3.6+ instalado
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

1. Execute o aplicativo:
```bash
python stealth_app.py
```

2. Clique em "Ativar" para iniciar a automação
3. Clique em "Desativar" para parar a automação
4. Feche a janela para encerrar o aplicativo

## Dependências

- `pynput`: Para automatização do teclado
- `tkinter`: Para interface gráfica (já incluído no Python)

## Observações

- O aplicativo executa a automação em uma thread separada para não travar a interface
- A tecla LSHIFT é pressionada por 100ms a cada 5 segundos quando ativo
- É possível fechar o aplicativo com segurança a qualquer momento

