import os
from pystyle import *
import tls_client, requests
import ctypes
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

class Lunarmart:
    def __init__(self):
        try:
            self.tokens = self.load_tokens()
            self.nowtimer = datetime.today().strftime('%H:%M:%S')
            os.system("mode 100, 30")  # Adjust console size
            self.clear()
            self.setTitle("🚀 Lunarmart Password Updater 🌙")
            self.banner()

            self.session = tls_client.Session(client_identifier="chrome_122", random_tls_extension_order=True)
            Write.Print("🔥 No Proxies - Proxyless Mode", Colors.purple_to_blue, interval=0.03 , end="")
            
            self.lunar_main()
        except Exception as e:
            print(f"🚨 An error occurred during initialization: {e}")
    
    def load_tokens(self):
        try:
            with open("input/tokens.txt", "r", encoding="utf-8") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print("❗ input/tokens.txt file not found.")
            return []
        except Exception as e:
            print(f"🚨 An error occurred while loading tokens: {e}")
            return []

    def banner(self):
        try:
            banner = f'''
             .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+. 
            (    ██╗     ██╗   ██╗███╗   ██╗ █████╗ ██████╗ ███╗   ███╗ █████╗ ██████╗ ████████╗      )
             )   ██║     ██║   ██║████╗  ██║██╔══██╗██╔══██╗████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝     ( 
            (    ██║     ██║   ██║██╔██╗ ██║███████║██████╔╝██╔████╔██║███████║██████╔╝   ██║         )
            )    ██║     ██║   ██║██║╚██╗██║██╔══██║██╔══██╗██║╚██╔╝██║██╔══██║██╔══██╗   ██║        ( 
            (    ███████╗╚██████╔╝██║ ╚████║██║  ██║██║  ██║██║ ╚═╝ ██║██║  ██║██║  ██║   ██║         )
             )   ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ( 
            (                                                                                         )
             "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+" 
                      💎 Token Count: {len(self.tokens)} 🚀 Lunarmart Password Changer 🛠️'''


            print(Colorate.Vertical(Colors.purple_to_blue, Center.XCenter(banner)))
        except Exception as e:
            print(f"🚨 An error occurred while displaying the banner: {e}")
    
    def clear(self):
        try:
            os.system("cls")
        except Exception as e:
            print(f"🚨 An error occurred while clearing the console: {e}")
    
    def setTitle(self, _str):
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f"{_str}")
        except Exception as e:
            print(f"🚨 An error occurred while setting the console title: {e}")
    
    @staticmethod
    def get_cookie(): 
        try:
            response = requests.Session().get('https://discord.com/app')
            cookie = str(response.cookies)
            return cookie.split('dcfduid=')[1].split(' ')[0], cookie.split('sdcfduid=')[1].split(' ')[0], cookie.split('cfruid=')[1].split(' ')[0]
        except Exception as e:
            print(f"🚨 Error getting cookies: {e}")
            return None, None, None
    
    @staticmethod
    def get_headers(token):
        try:
            headers = {
                "authority": "discord.com",
                "method": "GET",
                "path": "/api/v9/users/@me",
                "scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.9",
                "Authorization": token,
                "Cache-Control": "no-cache",
                "cookie": "__dcfduid=%s; __sdcfduid=%s; locale=en-US; __cfruid=%s" % Lunarmart.get_cookie(),
                "Dnt": "1",
                "Pragma": "no-cache",
                "Priority": "u=1, i",
                "Referer": "https://discord.com/channels/@me",
                "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                "X-Debug-Options": "bugReporterEnabled",
                "X-Discord-Locale": "en-US",
                "X-Discord-Timezone": "Asia/Calcutta",
                "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjMwNzE3MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ==",
            }

            return headers
        except Exception as e:
            print(f"🚨 Error getting headers: {e}")
            return None
    
    @staticmethod
    def check_status(status_code: int):
        status_messages = {
            200: "✅ Success",
            201: "✅ Success",
            204: "✅ Success",
            400: "❌ Detected Captcha",
            401: "❌ Unauthorized",
            403: "❌ Forbidden",
            404: "❌ Not Found",
            405: "❌ Method not allowed",
            429: "❌ Too many Requests"
        }
        return status_messages.get(status_code, "⚠️ Unknown Status")

    
    def lunar_main(self):
        try:
            self.clear()
            self.banner()

            new_pass = Write.Input(f'{self.nowtimer} 🛡️ New Password: ', Colors.purple_to_blue, interval=0.03, end="")
            threads = float(Write.Input(f'{self.nowtimer} 🧠 Threads: ', Colors.purple_to_blue, interval=0.03, end=""))

            def pwchanger(token, password, email, new_pass):
                url = 'https://discord.com/api/v9/users/@me'
                payload = {'password': password, 'new_password': new_pass}
                headerz = Lunarmart.get_headers(token)
                
                tk = token[:32] + "*" * 3  # Initialize tk before try-except block
                try:
                    r = self.session.patch(url, json=payload, headers=headerz)
                    if r.status_code == 200:
                        new_token = r.json()['token']
                        tk = new_token[:32] + "*" * 3
                        print(Colorate.Vertical(Colors.purple_to_blue, f'{self.nowtimer} ({Lunarmart.check_status(r.status_code)}) → {email} [{new_pass}]'))

                        today_folder = datetime.today().strftime('%d-%m-%Y')
                        output_folder = os.path.join("output", today_folder)
                        os.makedirs(output_folder, exist_ok=True)

                        with open(os.path.join(output_folder, "new_tokens.txt"), "a") as f:
                            f.write(f"{email}:{new_pass}:{new_token}\n")
                    else:
                        print(Colorate.Horizontal(Colors.red_to_yellow, f'{self.nowtimer} ({Lunarmart.check_status(r.status_code)}) → {email}'))
                except Exception as e:
                    print(f"🚨 Error while changing password for {email}: {e}")

            tokens = list(set(self.tokens))

            with ThreadPoolExecutor(max_workers=int(threads)) as executor:
                for account in tokens:
                    email, password, token = account.split(':')[:3]
                    executor.submit(pwchanger, token, password, email, new_pass)

            # After processing, clear the tokens file
            with open("input/tokens.txt", "w", encoding="utf-8") as file:
                file.write("")

            # Append the output folder name to output.txt
            today_folder = datetime.today().strftime('%d-%m-%Y')
            with open("output/output.txt", "a", encoding="utf-8") as output_log:
                output_log.write(f"{today_folder}\n")

        except Exception as e:
            print(f"🚨 An error occurred in the main function: {e}")

Lunarmart()
input("Press Enter to exit.")