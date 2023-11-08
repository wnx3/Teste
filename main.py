import requests
import hashlib
import PySimpleGUI as sg
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
            sg.popup('Bot atualizado com sucesso. Reiniciando...')
            raise Exception('Abra novamente.')

def main():
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text("Bot em execução.", font=('Open Sans', 10))]
    ]
    window = sg.Window("Bot", layout)

    while True:
        check_and_update_code()  # Verifica e atualiza no início de cada iteração

        event, values = window.read(timeout=1000)  # verifica a cada segundo

        if event == sg.WIN_CLOSED:
            break

    window.close()

if __name__ == "__main__":
    main()
