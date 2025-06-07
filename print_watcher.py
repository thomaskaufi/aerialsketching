# Prints whatever files are dropped in one folder, and moves them to another
# Thomas Kaufmanas, Making Motion 2025

import time
import subprocess
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#----- Config Stuff, create directories if needed ----
DEFAULT_CONFIG = {
    "printer_name": "DYMO_LabelWriter_400",
    "page_size": "w162h90", # Address labels = 36x89mm = "w102h252" | All purpose labels = 57x32mm = "w162h90"
    "incoming_dir": "incoming",
    "processed_dir": "processed",
    "debounce_seconds": 0.5,
    "log_file": "print_watcher.log"
}

BASEDIR = Path(__file__).resolve().parent
CONFIG = DEFAULT_CONFIG.copy()
PRINTER = CONFIG["printer_name"]
PAGE_SIZE = CONFIG["page_size"]
INCOMING = (BASEDIR / CONFIG["incoming_dir"]).expanduser()
PROCESSED = (BASEDIR / CONFIG["processed_dir"]).expanduser()
DEBOUNCE = float(CONFIG.get("debounce_seconds", 0.5))
LOG_FILE = str(BASEDIR / CONFIG.get("log_file", "print_watcher.log"))

INCOMING.mkdir(parents=True, exist_ok=True)
PROCESSED.mkdir(parents=True, exist_ok=True)

class PrintHandler(FileSystemEventHandler):
    """In case something happens in the folder...
    - Skip if the event is another folder
    - Grab the file name, and hold up for a bit too make sure the file is cooked finished!
    - Assemble the CUPS command, which I also used to just print from the terminal
    - Run the print command, and move the file to the second folder! With a few exceptions
    """
    def on_created(self, event):
        if event.is_directory:
            return
        src = Path(event.src_path)
        print(f"\n01     FILE IS DROPPED with the name {src.name}")
        time.sleep(DEBOUNCE)
        cmd = ["lpr", "-P", PRINTER, "-o", f"PageSize={PAGE_SIZE}", str(src)]

        try:
            print("02    Printing....")
            subprocess.run(cmd, check=True)
            subprocess.run(cmd, check=True)
            dest = PROCESSED / src.name
            shutil.move(str(src), str(dest))
            print("03    DONE! Moving the file :)")
            print("... Waiting for something to print")
        except subprocess.CalledProcessError as e:
            print(f"Oh no! ERROR with printing {src.name} because: {e}")
        except Exception as e:
            print("Oh No! Something went completely wrong because: ")

def main():
    print("\n\n\n\n*  *  *  *  *  *  *  *  *  *  *  *  *  *  *  *")
    print("Starting the Print Watching Script!")
    observer = Observer()
    observer.schedule(PrintHandler(), str(INCOMING), recursive=False)
    observer.start()
    print("... Waiting for something to print")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("    Shutting down.... ")
        observer.stop()
    observer.join()
    print("      Quit.")

if __name__ == "__main__":
    main()