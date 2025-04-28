from fastapi import FastAPI, Request

app = FastAPI()

valid_users = {
    12345678: "hwid_example_123",
    87654321: "hwid_example_456"
}

@app.post("/getscript")
async def get_script(request: Request):
    data = await request.json()
    uid = data.get("uid")
    hwid = data.get("hwid")
    
    if uid in valid_users and valid_users[uid] == hwid:
        return '''
print("Hello")
-- future code
'''
    else:
        return {"error": "Unauthorized"}, 403
