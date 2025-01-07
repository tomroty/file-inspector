import os
import subprocess
import argparse
import logging

if not os.path.exists('logs'):
    os.makedirs('logs')


logging.basicConfig(
    filename='logs/suspicious_files.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

def get_current_file_extension(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]

    
def get_detected_file_extension(file_path):
    command = f"file {file_path} --extension"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    output = output.decode()[len(file_path) + 2:].strip()
    if output == "???":
        return None
    return output

def is_suspicious(file_path):
    extension = get_current_file_extension(file_path)
    detected_extension = get_detected_file_extension(file_path)
    print(f"Actual file extension: {extension}")
    logging.info(f"Actual file extension: {extension}")
    print(f"Detected file extension: {detected_extension}")
    logging.info(f"Detected file extension: {detected_extension}")
    if detected_extension is None:
        print(f"Could not detect file extension for {file_path}.")
        command = f"file {file_path}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        output = output.decode()[len(file_path) + 2:].strip()
        print(f"File extension of {file_path} could not be guessed confidently from the file data by the `file` command.\nPlease check manually if file type `{output}` matches the file extension `{extension}`.")
        logging.info(f"File extension of {file_path} could not be guessed confidently from the file data by the `file` command.")
        logging.info(f"Please check manually if file type `{output}` matches the file extension `{extension}`.")
        return -1

    if extension != detected_extension:
        return True
    return False


def main():
    
    if os.name != 'posix':
        print("This script is intended to run on Unix-like systems only.")
        return

    parser = argparse.ArgumentParser(description="Analyze a file to check if its type matches its extension.")
    parser.add_argument("file", help="Path to the file to be analyzed.")
    args = parser.parse_args()

    file_path = args.file
    
    if not os.path.exists(file_path):
        print("Error: The specified file does not exist.")
        logging.info(f"Error: The specified file {file_path} does not exist.")
        return

    suspicious = is_suspicious(file_path)
    if suspicious == True:
        print(f"⚠️ The file {file_path} is suspicious.")
        logging.info(f"The file {file_path} is suspicious.")
    elif suspicious == False:
        print(f"✅ The file {file_path} seems not suspicious.")
        logging.info(f"The file {file_path} seems not suspicious.")
    else:
        print(f"❓ The file {file_path} needs manual inspection.")
        logging.info(f"Manual inspection required for file: {file_path}")
    
if __name__ == "__main__":
    main()
