SESSION_TIMEOUT = 30 * 60  # 30 minutes

def is_session_valid(session):
    return (current_time() - session.last_active) < SESSION_TIMEOUT
