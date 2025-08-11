import os
import shutil
from datetime import datetime

def fazer_backup(pasta_origem, pasta_destino_base):
    """
    Cria um backup de uma pasta de origem em uma pasta de destino,
    adicionando a data atual ao nome do diretório de backup.
    
    Args:
        pasta_origem (str): O caminho completo da pasta que será copiada.
        pasta_destino_base (str): O caminho completo do diretório onde o backup será salvo.
    """
    
    # 1. Valida os caminhos da pasta de origem
    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta de origem '{pasta_origem}' não existe.")
        return
        
    # 2. Cria a pasta de destino base se ela não existir
    if not os.path.exists(pasta_destino_base):
        try:
            os.makedirs(pasta_destino_base)
            print(f"Pasta de destino '{pasta_destino_base}' criada com sucesso.")
        except OSError as e:
            print(f"Erro ao criar a pasta de destino: {e}")
            return

    # 3. Gera um nome para a pasta de backup com a data atual
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    nome_pasta_backup = f"backup_{data_hoje}"
    
    # 4. Combina o caminho de destino base com o nome da nova pasta de backup
    pasta_destino_completo = os.path.join(pasta_destino_base, nome_pasta_backup)
    
    # 5. Verifica se a pasta de backup já existe e a remove para evitar erros
    # Esta abordagem garante que a cópia mais recente do dia será salva
    if os.path.exists(pasta_destino_completo):
        print(f"Pasta de backup '{pasta_destino_completo}' já existe. Removendo...")
        try:
            shutil.rmtree(pasta_destino_completo)
        except OSError as e:
            print(f"Erro ao remover a pasta de backup antiga: {e}")
            return
    
    # 6. Copia a pasta de origem para o destino
    print(f"Iniciando o backup de '{pasta_origem}' para '{pasta_destino_completo}'...")
    try:
        shutil.copytree(pasta_origem, pasta_destino_completo)
        print("Backup concluído com sucesso!")
    except shutil.Error as e:
        print(f"Erro ao copiar arquivos: {e}")
    except OSError as e:
        print(f"Erro no sistema operacional durante a cópia: {e}")


# --- Exemplo de Uso ---
if __name__ == "__main__":
    # Substitua os caminhos abaixo pelos que você deseja usar
    pasta_origem = "C:\\Users\\Seu_Usuario\\Documents\\Projetos"
    pasta_destino = "C:\\Backups\\Documentos"
    
    # Em sistemas Linux/macOS, os caminhos seriam assim:
    # pasta_origem = "/home/seu_usuario/Documentos/Projetos"
    # pasta_destino = "/home/seu_usuario/Backups"
    
    fazer_backup(pasta_origem, pasta_destino)
