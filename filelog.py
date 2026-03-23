class Logger:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(self.file_path, "a")  # append mode
        print("Log file opened successfully")

    def log(self, message):
        if self.file:
            self.file.write(message + "\n")

    def __del__(self):
        if self.file:
            self.file.close()
            print("Log file closed automatically")


# Usage
logger = Logger("log.txt")

logger.log("Program started")
logger.log("Performing some operations...")
logger.log("Program ended")