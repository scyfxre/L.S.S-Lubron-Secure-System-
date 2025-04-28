
from fastapi import FastAPI, Request
import random

app = FastAPI()

valid_users = {
    12345678: "hwid_example_123",
    87654321: "hwid_example_456"
}

def obfuscate_code(code):
    return "".join(chr(ord(c) ^ random.randint(1, 10)) for c in code)

@app.post("/getscript")
async def get_script(request: Request):
    data = await request.json()
    uid = data.get("uid")
    hwid = data.get("hwid")
    
    if uid in valid_users and valid_users[uid] == hwid:
        script = f'''
print("scs Login {uid}!")
-- code
'''
        return script
    else:
        return {"error": "Unauthorized"}, 403
