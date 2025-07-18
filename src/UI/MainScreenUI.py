import tkinter as tk
from tkinter import ttk, messagebox
from Sensors.SensorManager import SensorManager

class MainScreenUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Water Quality Buoy Control")
        self.geometry("800x600")
        self.resizable(True, True)
        
        # Initialize sensor manager
        self.sensor_manager = SensorManager()
        
        # Initialize state variables
        self.is_running = False
        
        # Initialize UI components
        self._setup_ui()
        

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

        # About button
        self.about_button = ttk.Button(button_frame, text="About", command=self._on_about)
        self.about_button.pack(side=tk.LEFT, padx=5)
        
    def _on_about(self):
        """Handle About button click"""
        messagebox.showinfo("About", """Water Quality Buoy Control
                            Version 1.0
                            Created by Phillip Banky and Jennaya Horne

                            This is a test version of the water quality buoy control system.""")
        
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
        
        # Create sensor status labels with larger, more prominent indicators
        self.sensor_labels = {}
        sensor_types = self.sensor_manager.get_sensor_types()
        
        for sensor in sensor_types:
            frame = ttk.Frame(status_frame)
            frame.pack(fill="x", pady=5)
            
            # Create a larger indicator box
            indicator_frame = ttk.Frame(frame, relief="raised", borderwidth=2)
            indicator_frame.pack(side="left", padx=(0, 10))
            
            # Color indicator (larger and more prominent)
            indicator = tk.Label(
                indicator_frame, 
                text="●", 
                font=("TkDefaultFont", 10, "bold"),
                width=2,
                relief="sunken",
                borderwidth=1
            )
            indicator.pack(padx=5, pady=5)
            
            # Sensor name with larger font
            name_label = ttk.Label(frame, text=sensor, font=("TkDefaultFont", 11, "bold"))
            name_label.pack(side="left")
            
            # Store reference to indicator for later updates
            self.sensor_labels[sensor] = indicator
        
        # Add button to update sensor status
        ttk.Button(
            main_frame,
            text="Refresh Status",
            command=self._update_sensor_status
        ).pack(pady=(0, 10))
        
    def _update_sensor_status(self):
        """Update the sensor status indicators with comprehensive status checking"""
        # Get sensor status from the sensor manager
        sensor_status = self.sensor_manager.check_sensor_functionality()
        
        # Update each sensor indicator with enhanced colors
        for sensor, status in sensor_status.items():
            if sensor in self.sensor_labels:
                if status == "functional":
                    # Bright green for functional sensors
                    self.sensor_labels[sensor].configure(
                        foreground="darkgreen",
                        background="lightgreen",
                        relief="raised"
                    )
                elif status == "disabled":
                    # Gray for disabled sensors
                    self.sensor_labels[sensor].configure(
                        foreground="gray",
                        background="lightgray",
                        relief="flat"
                    )
                elif status == "error":
                    # Bright red for error sensors
                    self.sensor_labels[sensor].configure(
                        foreground="darkred", 
                        background="lightcoral",
                        relief="sunken"
                    )
                elif status == "needs_calibration":
                    # Yellow for sensors needing calibration
                    self.sensor_labels[sensor].configure(
                        foreground="darkorange",
                        background="lightyellow",
                        relief="sunken"
                    )
    
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
    app = MainScreenUI()
    app.mainloop()