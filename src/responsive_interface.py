"""
Responsive and Accessible Interface
As a user, I want the system to be intuitive and responsive on desktop and mobile devices, so that I can access leave management anytime.
"""
def render_interface(device_type):
    if device_type == 'desktop':
        return 'Rendering desktop interface: dashboard, menu, leave forms.'
    elif device_type == 'mobile':
        return 'Rendering mobile interface: compact dashboard, touch-friendly forms.'
    else:
        return 'Device not supported.'

# Example usage
if __name__ == '__main__':
    print(render_interface('desktop'))
    print(render_interface('mobile'))
    print(render_interface('tablet'))
