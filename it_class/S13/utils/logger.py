def error(msg):
    print(f"[ERROR]{msg}")
    

def warning(msg):
    print(f"[WARNING] {msg}")

def info(msg):
    print(f"[INFO] {msg}")      

def debug(msg):
    print(f"[DEBUG] {msg}")      

if __name__ == "__main__": #module guard
    print("From module code!")

