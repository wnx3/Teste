import requests
import hashlib
import subprocess
import time

def check_and_update_code():
    base_url = 'https://raw.githubusercontent.com/wnx3/Teste/main/'
    file_list = ['main.py']

    for file_name in file_list:
        local_path = file_name
        url = base_url + file_name
        response = requests.get(url)
        github_version = response.content.decode('utf-8')

        with open(local_path, 'r', encoding='utf-8') as f:
            local_version = f.read()

        local_hash = hashlib.sha256(local_version.encode()).hexdigest()
        github_hash = hashlib.sha256(github_version.encode()).hexdigest()

        if local_hash != github_hash:
            with open(local_path, 'w', encoding='utf-8') as f:
                f.write(github_version)
            print('Bot atualizado com sucesso. Reiniciando...')
            return True

    return False

def main():
    while True:
        if check_and_update_code():
            # Se houve uma atualização, reinicie o bot automaticamente
            subprocess.run(["python", "main.py"])  # Substitua "SEU_ARQUIVO_PRINCIPAL.py" pelo nome do seu arquivo principal
            break  # Este ponto só será alcançado se o subprocess.run for concluído

        # Coloque aqui o restante do seu código principal
        print("Código principal sendo executado...")
        time.sleep(1)  # Adicione algum tipo de operação principal aqui
        print("2")

if __name__ == "__main__":
    main()
