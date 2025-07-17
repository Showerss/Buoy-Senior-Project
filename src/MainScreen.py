import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class BuoyUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Water Quality Buoy Control")
        self.geometry("800x600")
        self.resizable(True, True)
        
        # Initialize UI components
        self._setup_ui()
        
        # Initialize state variables
        self.is_running = False
        
    def _setup_ui(self):
        # Create main frame
        main_frame = ttk.Frame(self, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create control panel
        control_panel = ttk.Frame(main_frame)
        control_panel.pack(side=tk.TOP, fill=tk.X, pady=(0, 10))
        
        # Add buttons
        self._add_buttons(control_panel)
        
        # Create canvas for visualization
        self.canvas = tk.Canvas(main_frame, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind resize event
        self.bind("<Configure>", self._on_resize)
        
    def _add_buttons(self, parent):
        # Create button frame
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X)
        
        # Run button
        self.run_button = ttk.Button(button_frame, text="Run", command=self._on_run)
        self.run_button.pack(side=tk.LEFT, padx=5)
        
        # Settings button
        self.settings_button = ttk.Button(button_frame, text="Settings", command=self._on_settings)
        self.settings_button.pack(side=tk.LEFT, padx=5)
        
        # Data button
        self.data_button = ttk.Button(button_frame, text="Data", command=self._on_data)
        self.data_button.pack(side=tk.LEFT, padx=5)
        
    def _on_run(self):
        """Handle Run button click"""
        if not self.is_running:
            self.run_button.configure(text="Stop")
            self.is_running = True
            # Add your run logic here
            self._update_canvas()
        else:
            self.run_button.configure(text="Run")
            self.is_running = False
            # Add your stop logic here
            
    def _on_settings(self):
        """Handle Settings button click"""
        # Create settings dialog
        settings_window = tk.Toplevel(self)
        settings_window.title("Settings")
        settings_window.geometry("400x300")
        
        # Create main frame for better organization
        main_frame = ttk.Frame(settings_window)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Add depth slider
        ttk.Label(main_frame, text="Depth (meters)").pack(anchor="w", pady=(0, 5))
        self.depth_slider = ttk.Scale(
            main_frame,
            from_=0,
            to=100,
            orient="horizontal",
            length=200
        )
        self.depth_slider.pack(fill="x", pady=(0, 15))
        
        # Add sensor status indicators
        status_frame = ttk.LabelFrame(main_frame, text="Sensor Status")
        status_frame.pack(fill="x", pady=(0, 15))
        
        # Create sensor status labels with color indicators
        self.sensor_labels = {}
        sensor_types = ["Temperature", "pH", "Turbidity", "Dissolved Oxygen"]
        
        for sensor in sensor_types:
            frame = ttk.Frame(status_frame)
            frame.pack(fill="x", pady=2)
            
            # Color indicator
            indicator = ttk.Label(frame, text="•", font=("TkDefaultFont", 12))
            indicator.pack(side="left", padx=(0, 5))
            
            # Sensor name
            ttk.Label(frame, text=sensor).pack(side="left")
            
            # Store reference to indicator for later updates
            self.sensor_labels[sensor] = indicator
        
        # Add button to update sensor status
        ttk.Button(
            main_frame,
            text="Refresh Status",
            command=self._update_sensor_status
        ).pack(pady=(0, 10))
        
    def _update_sensor_status(self):
        """Update the sensor status indicators with color coding"""
        # Simulated sensor status data (replace with actual sensor readings)
        sensor_status = {
            "Temperature": True,  # Green
            "pH": False,         # Red
            "Turbidity": True,   # Green
            "Dissolved Oxygen": True  # Green
        }
        
        # Update each sensor indicator
        for sensor, status in sensor_status.items():
            if sensor in self.sensor_labels:
                if status:
                    # Green for good status
                    self.sensor_labels[sensor].configure(foreground="green")
                else:
                    # Red for bad status
                    self.sensor_labels[sensor].configure(foreground="red")

    def _on_data(self):
        """Handle Data button click"""
        # Create data viewer window
        data_window = tk.Toplevel(self)
        data_window.title("Data Viewer")
        data_window.geometry("600x400")
        
        # Add data viewer UI components here
        ttk.Label(data_window, text="Data Viewer Window").pack(pady=20)
        
    def _on_resize(self, event):
        """Handle window resize"""
        if hasattr(self, 'canvas'):
            self.canvas.config(width=event.width-20, height=event.height-20)
            
    def _update_canvas(self):
        """Update canvas visualization"""
        if self.is_running:
            # Add your visualization logic here
            self.canvas.create_rectangle(10, 10, 50, 50, fill="blue")
            
            # Schedule next update
            self.after(1000, self._update_canvas)

if __name__ == '__main__':
    app = BuoyUI()
    app.mainloop()
