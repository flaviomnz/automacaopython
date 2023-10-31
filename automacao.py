import os
import shutil

# ps: "\\" = windows
# se for outro sistema operacional vai ser diferente. 


# diretorio:
diretorio_origem = 'C:\\Users\\mnzfl\\OneDrive\\Ambiente de Trabalho\\Teste'

# fazer o mapeamento, onde 'XXX' são os 3 primeiro digitos das pastas criadas.
mapeamento = {
    'VIX': 'C:\\Users\\mnzfl\\OneDrive\\Ambiente de Trabalho\\Teste\\movido\\VIX',
    'KRM': 'C:\\Users\\mnzfl\\OneDrive\\Ambiente de Trabalho\\Teste\\movido\\KRM',
    'VAB': 'C:\\Users\\mnzfl\\OneDrive\\Ambiente de Trabalho\\Teste\\movido\\VAB',
}

# Loop pelos arquivos na pasta de origem
for arquivo in os.listdir(diretorio_origem):
    caminho_arquivo_origem = os.path.join(diretorio_origem, arquivo)
    
    # verifica se o arquivo é um arquivo (não um diretorio)
    if os.path.isfile(caminho_arquivo_origem):
        
        # para obter os 3 primeiros caracteres
        tres_primeiros_digitos = arquivo[:3]

        # verifica se tem um mapeamento criado para os três primeiros digitos do arquivo
        if tres_primeiros_digitos in mapeamento:
            # obter o diretório de destino com base no mapeamento
            diretorio_destino = mapeamento[tres_primeiros_digitos]

            # contruir o caminho de destino completo
            caminho_arquivo_destino = os.path.join(diretorio_destino, arquivo)

            # verifica se o diretorio de destino exist
            os.makedirs(diretorio_destino, exist_ok=True)

            # caso tudo dê certo, move o arquivo selecionado no mapeamento. 
            shutil.move(caminho_arquivo_origem, caminho_arquivo_destino)

print("Arquivos movidos com sucesso.")
