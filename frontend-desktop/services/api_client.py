import requests
import json
from pathlib import Path

class APIClient:
    """API client for communicating with Django backend"""
    
    def __init__(self, base_url='http://localhost:8000/api'):
        self.base_url = base_url
        self.token = None
        self.user = None
        self.load_token()
    
    def load_token(self):
        """Load token from file if exists"""
        token_file = Path('token.json')
        if token_file.exists():
            with open(token_file, 'r') as f:
                data = json.load(f)
                self.token = data.get('token')
                self.user = data.get('user')
    
    def save_token(self, token, user):
        """Save token to file"""
        with open('token.json', 'w') as f:
            json.dump({'token': token, 'user': user}, f)
        self.token = token
        self.user = user
    
    def get_headers(self):
        """Get request headers with authorization"""
        headers = {'Content-Type': 'application/json'}
        if self.token:
            headers['Authorization'] = f'Token {self.token}'
        return headers
    
    def login(self, username, password):
        """Login user"""
        try:
            response = requests.post(
                f'{self.base_url}/auth/login/',
                json={'username': username, 'password': password}
            )
            response.raise_for_status()
            data = response.json()
            self.save_token(data['token'], data['user'])
            return True, data['user']
        except requests.exceptions.RequestException as e:
            return False, str(e)
    
    def register(self, username, password, email):
        """Register new user"""
        try:
            response = requests.post(
                f'{self.base_url}/auth/register/',
                json={'username': username, 'password': password, 'email': email}
            )
            response.raise_for_status()
            data = response.json()
            self.save_token(data['token'], data['user'])
            return True, data['user']
        except requests.exceptions.RequestException as e:
            return False, str(e)
    
    def logout(self):
        """Logout user"""
        try:
            requests.post(
                f'{self.base_url}/auth/logout/',
                headers=self.get_headers()
            )
        except:
            pass
        self.token = None
        self.user = None
        Path('token.json').unlink(missing_ok=True)
    
    def upload_csv(self, file_path):
        """Upload CSV file"""
        try:
            with open(file_path, 'rb') as f:
                files = {'file': f}
                response = requests.post(
                    f'{self.base_url}/upload/',
                    files=files,
                    headers={'Authorization': f'Token {self.token}'}
                )
            response.raise_for_status()
            return True, response.json()
        except Exception as e:
            return False, str(e)
    
    def get_summary(self):
        """Get summary statistics"""
        try:
            response = requests.get(
                f'{self.base_url}/summary/',
                headers=self.get_headers()
            )
            response.raise_for_status()
            return True, response.json()
        except Exception as e:
            return False, str(e)
    
    def get_data(self):
        """Get equipment data"""
        try:
            response = requests.get(
                f'{self.base_url}/data/',
                headers=self.get_headers()
            )
            response.raise_for_status()
            return True, response.json()
        except Exception as e:
            return False, str(e)
    
    def get_history(self):
        """Get upload history"""
        try:
            response = requests.get(
                f'{self.base_url}/history/',
                headers=self.get_headers()
            )
            response.raise_for_status()
            return True, response.json()
        except Exception as e:
            return False, str(e)
    
    def download_report(self, save_path):
        """Download PDF report"""
        try:
            response = requests.get(
                f'{self.base_url}/download-report/',
                headers={'Authorization': f'Token {self.token}'}
            )
            response.raise_for_status()
            with open(save_path, 'wb') as f:
                f.write(response.content)
            return True, 'Report downloaded successfully'
        except Exception as e:
            return False, str(e)
