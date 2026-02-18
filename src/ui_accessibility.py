# ui_accessibility.py

class ResponsiveUI:
    def __init__(self):
        self.device = None
        self.accessibility_features = []

    def set_device(self, device: str):
        self.device = device
        return f"UI set for {device}"

    def enable_accessibility(self, feature: str):
        self.accessibility_features.append(feature)
        return f"Enabled accessibility feature: {feature}"

    def get_ui_state(self):
        return {
            "device": self.device,
            "accessibility_features": self.accessibility_features
        }

# Example usage
if __name__ == "__main__":
    ui = ResponsiveUI()
    print(ui.set_device('mobile'))
    print(ui.enable_accessibility('high_contrast'))
    print(ui.enable_accessibility('screen_reader'))
    print(ui.get_ui_state())
