import os
import shutil
import time
import argparse

def synchronize_folders(source_path, replica_path, log_path, interval):
    while True:
        source_files = set(os.listdir(source_path))
        replica_files = set(os.listdir(replica_path))

        files_to_copy = source_files - replica_files
        files_to_delete = replica_files - source_files

        for file in files_to_copy:
            src_file = os.path.join(source_path, file)
            dst_file = os.path.join(replica_path, file)
            shutil.copy2(src_file, dst_file)
            log(log_path, f"copied {src_file} to {dst_file}")

        for file in files_to_delete:
            file_path = os.path.join(replica_path, file)
            os.remove(file_path)
            log(log_path, f"deleted {file_path}")

        time.sleep(interval)

def log(log_path, message):
    with open(log_path, "a") as log_file:
        log_file.write(f"{message}\n")
    print(message)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument("source_path", type=str, help="path to source folder")
    parser.add_argument("replica_path", type=str, help="path to replica folder")
    parser.add_argument("interval", type=int, help="sync interval in seconds")
    parser.add_argument("log_path", type=str, help="path to log file")
    args = parser.parse_args()

    synchronize_folders(args.source_path, args.replica_path, args.log_path, args.interval)