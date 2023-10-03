import base64
import random
def generate_api_key():
    api_key = base64.b64encode(str(random.randint(1000000, 9999999)).encode()).decode()
    return api_key
sandbox_api_key = generate_api_key()
main_api_key = generate_api_key()
print(sandbox_api_key, main_api_key)