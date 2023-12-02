# ponderada 7 - Tradutor de áudio 

## Instruções de Instalação e Execução

1. Clone o repositório:
    ```bash
    git clone https://github.com/jacksonwsaguiar/ponderada8
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd ponderada7
    ```

3. Instale as dependências:
    ```bash
    pip install gtts speech_recognition translate
    ```
    
## Executando o projeto

Para executar o tradutor, use o seguinte comando:
    ```bash
    python3 app.py [caminho do arquivo]
    ```
## Explicação
Este script em Python realiza o reconhecimento de fala em um arquivo de áudio e em seguida traduz o texto resultante para o idioma português. O áudio traduzido é então convertido em um novo arquivo de áudio no formato MP3.

1. A partir do arquivo carregado, reconhece a fala no arquivo de áudio com o speech_recognition.
2. Imprime o texto transcrito.
3. Depois, use a lib translate para traduzir o texto para o português.
4. Imprime a tradução.
5. E por fim, com o tts, converte a tradução em áudio e salva como 'output.mp3'.

## Demonstração em Vídeo

Demonstração completa do funcionamento:
https://drive.google.com/file/d/1n4k3b6_7FSJBuOas8gHUvF4Nvky75wWG/view?usp=sharing

