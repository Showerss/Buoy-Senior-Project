"""
Main entry point for the Buoy Water Quality Monitoring System.

This module initializes the application and starts the main user interface.
"""
import sys
import os
import logging
from MainScreen import BuoyUI

def setup_logging():
    """Configure application logging."""
    log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, 'buoy_app.log')
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    """Main entry point for the application."""
    try:
        # Set up logging
        setup_logging()
        logger = logging.getLogger(__name__)
        logger.info("Starting Buoy Water Quality Monitoring System")
        
        # Initialize and start the main application
        app = BuoyUI()
        app.mainloop()
        
        logger.info("Application shutdown complete")
        
    except Exception as e:
        logging.critical("Fatal error in main application", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
