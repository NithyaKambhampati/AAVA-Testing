def get_user_profile(user_id):
    user = fetch_user(user_id)

    if not user:
        return {"error": "User not found"}, 404

    profile = user.profile or {}
    return {"profile": profile}, 2000
