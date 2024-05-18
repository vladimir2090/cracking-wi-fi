import subprocess

try:
    data = subprocess.check_output("netsh wlan show profiles").decode('cp866').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All user profiles" in i]
    pass_wifi = ''

    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('cp866').split('\n')

        for j in results:
            if "Key Contents" in j:
                pass_wifi += f"{i} -- {j.split(':')[1][1:-1]}\n"

    print(f"Pass: {pass_wifi}")
except Exception as ex:
    print(f'Error: {ex}')