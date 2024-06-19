try:
    import requests, fake_useragent, os
    from requests import Timeout, RequestException
    from fake_useragent import UserAgent
    import time
    from multiprocessing import Pool
    from concurrent.futures import ThreadPoolExecutor
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
                print("\033[1;32m{}{} - {}".format(url, admin, response.status_code))
            else:
                print("\033[1;91m{}{} - {}".format(url, admin, response.status_code))
        except Timeout:
            print("\033[1;91m Timeout!")
            time.sleep(20)
            continue
        except RequestException:
            print("\033[1;91m An Error Occured!")
            continue
if __name__ == '__main__':
    clear()
    print(logo)
    url = input("[+] Insert Url : ")
    file_path = input("[+] Insert Path Admin [.txt] : ")
    try:
        with Pool(20) as mp:
            mp.map(start_scanning, url, file_path)
    except TypeError:
        with ThreadPoolExecutor(max_workers=40) as executor:
            futures = [executor.submit(start_scanning, url, file_path)]
    except:
        start_scanning(url, file_path)
