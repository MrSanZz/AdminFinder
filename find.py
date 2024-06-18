try:
    import requests, fake_useragent, os
    from requests import Timeout, RequestException
    from fake_useragent import UserAgent
except ModuleNotFoundError:
    import os
    os.system('pip3 install requests')
    os.system('pip3 install fake_useragent')

logo = """

┏┓ ┓   •    ┏┓•   ┓    
┣┫┏┫┏┳┓┓┏┓  ┣ ┓┏┓┏┫┏┓┏┓
┛┗┗┻┛┗┗┗┛┗  ┻ ┗┛┗┗┻┗ ┛ 
            v 2.0
"""
def clear():
    os.system('clear' if os.name=='posix' else 'cls')
def start_scanning(url, path):
    admin_path = open(path, 'r').read().split()
    for admin in admin_path:
        try:
            response = requests.get(url + admin, headers={"User-Agent": UserAgent().chrome}, timeout=7)
            if response.status_code == 200:
                print("\n\033[1;32m{}{} - {}".format(url, admin, response.status_code))
            else:
                print("\n\033[1;91m{}{} - {}".format(url, admin, response.status_code))
        except Timeout:
            print("\n\033[1;91m Timeout!")
            break
        except RequestException:
            print("\n\033[1;91m An Error Occured!")
            break
if __name__ == '__main__':
    clear()
    print(logo)
    url = input("[+] Insert Url : ")
    file_path = input("[+] Insert Path Admin [.txt] : ")
    start_scanning(url, file_path)
