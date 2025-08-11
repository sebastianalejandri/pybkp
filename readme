***Como o Código Funciona

    from datetime import datetime: Importa a classe datetime para obter a data e a hora atuais.

    datetime.now().strftime("%Y-%m-%d"): Esta linha obtém a data atual e a formata como uma string no padrão "Ano-Mês-Dia" (ex: "2025-08-11"). Isso garante que o nome da pasta de backup seja sempre consistente e ordenado.

    os.path.exists(caminho): Verifica se um determinado caminho (pasta ou arquivo) existe. É uma etapa importante para garantir que o script não tente copiar de uma pasta que não existe.

    os.makedirs(pasta_destino_base): Cria o diretório de destino base se ele ainda não existir.

    shutil.rmtree(pasta_destino_completo): Remove a árvore de diretórios inteira, caso o backup do dia já tenha sido executado. Isso garante que a pasta de backup seja recriada com o estado mais atual dos arquivos.

    shutil.copytree(pasta_origem, pasta_destino_completo): Esta é a parte principal do script. Ela copia recursivamente todos os arquivos e subdiretórios da pasta_origem para a pasta_destino_completo.

**Como Usar o Script

    Salve o arquivo: Salve o código em um arquivo .py.

    Ajuste os caminhos: No final do script (if __name__ == "__main__":), edite as variáveis pasta_origem e pasta_destino com os caminhos corretos da sua máquina. Lembre-se de usar barras duplas (\\) no Windows ou barras simples (/) no Linux/macOS.

    Execute: Abra o terminal, navegue até a pasta onde salvou o arquivo e execute-o com o comando:


Bash    
-------------------------------------  
python backup_automatizado.py
--------------------------------------
                                            
Você pode configurando-lo para rodar automaticamente em um agendador de tarefas (como o Crontab no Linux ou o Agendador de Tarefas do Windows).
