def validate_otp(input_otp, actual_otp):
    if input_otp != actual_otp:
        return {"error": "Invalid OTP"}, 400

    return {"message": "OTP verified"}, 200
