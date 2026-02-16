"""
Responsive and Accessible User Interface
User Story: As a user, I want the LMS to be easy to use and accessible on desktop and mobile so that I can access it conveniently.
Acceptance Criteria:
- Interface is responsive and accessible across devices and browsers.
"""

# Placeholder for UI logic. In a real Python web app, you would use Flask/FastAPI + frontend (React/Angular/Vue).
# Here, we provide a stub for API endpoint and device detection.

def get_device_type(user_agent: str) -> str:
    if "Mobile" in user_agent:
        return "mobile"
    elif "Tablet" in user_agent:
        return "tablet"
    else:
        return "desktop"

# Example usage:
if __name__ == "__main__":
    print(get_device_type("Mozilla/5.0 (iPhone; Mobile)") )  # mobile
    print(get_device_type("Mozilla/5.0 (Windows NT; desktop)") )  # desktop
