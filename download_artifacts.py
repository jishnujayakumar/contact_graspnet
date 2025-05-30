# Script to download Google Drive folders to specified directories
# Downloads:
# - https://drive.google.com/drive/folders/1tBHKf60K8DLM5arm-Chyf7jxkzOr5zGl to checkpoints/
# - https://drive.google.com/drive/folders/1TqpM2wHAAo0j3i1neu3Xeru3_WnsYQnx to test_data/

import os
import gdown

# Define target directories
CHECKPOINTS_DIR = "checkpoints"
TEST_DATA_DIR = "test_data"

# Google Drive folder IDs extracted from URLs
CHECKPOINTS_FOLDER_ID = "1tBHKf60K8DLM5arm-Chyf7jxkzOr5zGl"
TEST_DATA_FOLDER_ID = "1TqpM2wHAAo0j3i1neu3Xeru3_WnsYQnx"

# Create directories if they don't exist
os.makedirs(CHECKPOINTS_DIR, exist_ok=True)
os.makedirs(TEST_DATA_DIR, exist_ok=True)

# Function to download a Google Drive folder
def download_gdrive_folder(folder_id, output_dir):
    print(f"Downloading folder {folder_id} to {output_dir}...")
    try:
        gdown.download_folder(
            id=folder_id,
            output=output_dir,
            quiet=False,
            use_cookies=False
        )
        print(f"Successfully downloaded to {output_dir}")
    except Exception as e:
        print(f"Error downloading folder {folder_id}: {str(e)}")

# Download checkpoints folder
download_gdrive_folder(CHECKPOINTS_FOLDER_ID, CHECKPOINTS_DIR)

# Download test_data folder
download_gdrive_folder(TEST_DATA_FOLDER_ID, TEST_DATA_DIR)