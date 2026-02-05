MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50MB

def upload_file(file):
    if file.size > MAX_UPLOAD_SIZE:
        return {"error": "File too large"}, 413

    save_file(file)
    return {"message": "Upload successful"}, 200
