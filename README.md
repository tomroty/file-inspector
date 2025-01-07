# File Inspector

A simple Python utility to detect file type mismatches and identify potentially suspicious files.

## Purpose

File Inspector helps identify files whose actual content doesn't match their extension, which could indicate:
- Maliciously disguised files
- Incorrectly renamed files
- Corrupted files

## Requirements

- Python 3.x
- Unix-like operating system (Linux, macOS)
- `file` command (usually pre-installed on Unix systems)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/file-inspector.git
cd file-inspector
```

2. No additional Python packages are required.

## Usage

```bash
python file_inspector.py <file_path>
```

The script will:
1. Check the file's extension
2. Detect the actual file type
3. Compare them and report if the file is suspicious

### Output Indicators

- ✅ File type matches extension
- ⚠️ File type doesn't match extension (suspicious)
- ❓ Manual inspection needed

### Example

```bash
python file_inspector.py suspicious.jpg
Actual file extension: jpg
Detected file extension: pdf
⚠️ The file suspicious.jpg is suspicious.
```

## Logging

Suspicious file detections are logged in `logs/suspicious_files.log` with timestamps.

## Limitations

- Currently only works on Unix-like systems
- Depends on the `file` command's detection capabilities
