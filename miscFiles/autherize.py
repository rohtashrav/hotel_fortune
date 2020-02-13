def authentication(auth, role_id, user_role):
    if auth is True:
        if role_id == user_role:
            return True
        else:
            return False, "invalid_user"
    else:
        return False, "not_login"
