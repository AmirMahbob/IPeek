import requests as r
import re
import socket
import ipaddress


class Find_ip:
    
    def __init__(self):
        self.info=''
        self.error=None
    
            
    def is_private_ip(self, ip):
        try:
            return ipaddress.ip_address(ip).is_private
        except ValueError:
            return False
        
        
    def get_info_ip(self, ip):
        url = f"http://ip-api.com/json/{ip}"
        responce=r.get(url=url)
        self.info=responce.json()
        self.info_str = f"IP: {ip}\n"
        self.info_str += f"Country: {self.info.get('country', 'N/A')}\n"
        self.info_str += f"Region: {self.info.get('region', 'N/A')}\n"
        self.info_str += f"Region Name: {self.info.get('regionName', 'N/A')}\n"
        self.info_str += f"City: {self.info.get('city', 'N/A')}\n"
        self.info_str += f"Lat: {self.info.get('lat', 'N/A')}\n"
        self.info_str += f"Lon: {self.info.get('lon', 'N/A')}\n"
        self.info_str += f"ISP: {self.info.get('isp', 'N/A')}\n"
        self.info_str += f"Timezone: {self.info.get('timezone', 'N/A')}\n"
        self.info_str += f"Org: {self.info.get('org', 'N/A')}\n"
        self.info_str += f"as: {self.info.get('as', 'N/A')}\n"
        self.info_str += f"query: {self.info.get('query', 'N/A')}\n"
        
        
        self.info = self.info_str 
        
    def convert_domin_to_ip(self, domin):
        try:
            cleaned_domin = re.sub(r'^(https?://)', '', domin)
            self.ip = socket.gethostbyname(cleaned_domin)
            self.get_info_ip(ip=self.ip)
            
        except socket.gaierror:
            self.error = 'Invalid domain name or unable to resolve IP.'
        except Exception as e:
            self.error = f'An error occurred: {str(e)}'

    @staticmethod
    def is_valid_ip(ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False
        return True

    def check_internet_connection(self):
        try:
            response = r.get('http://www.google.com', timeout=5)
            if response.status_code == 200:
                return True
            else:
                return False
        except r.ConnectionError:
            return False


    def cheak(self, entry):
        base_pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
        domin_pattern=r'^(https?://)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,10}(/[^\s]*)?$'
        if self.check_internet_connection():   
            if re.match(base_pattern, entry):
                if self.is_valid_ip(entry):  
                    self.get_info_ip(entry)  
                else:
                    self.error = 'Invalid IP format: each part must be between 0 and 255.'
                
            elif re.match(domin_pattern, entry):
                self.convert_domin_to_ip(entry) 
                
            else:
                self.error = 'Entry not valid!'  
                
        else:
            self.error = 'not internet connection!'