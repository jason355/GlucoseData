import dropbox
import gzip
import os
import datetime
import shutil
from dotenv import load_dotenv

script_dir = os.path.dirname(os.path.abspath(__file__))


def download_file_from_dropbox(TOKEN,dropbox_path, local_path):
    dbx = dropbox.Dropbox(TOKEN)

    try:
        metadata, res = dbx.files_download(dropbox_path)
        with open(local_path, 'wb') as f:
            f.write(res.content)
        print(f'File downloaded successfully to {local_path}')
    except dropbox.exceptions.ApiError as err:
        print(f'Error downloading file from Dropbox: {err}')


def extract_gz(gz_path, extract_to_path):
    try:
        with gzip.open(gz_path, 'rb') as f_in:
            with open(extract_to_path, "wb") as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"File extracted successfully to {extract_to_path}")
    except Exception as e:
        print(f"Error extraction file: {e}")


load_dotenv()



APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")


# auth_flow = dropbox.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET)
# authorize_url = auth_flow.start()
# print("1. Go to:", authorize_url)
# print("2. Click 'Allow' (you might have to log in first).")
# print("3. Copy the authorization code.")
# auth_code = input("Enter the authorization code here: ").strip()


# oauth_result = auth_flow.finish(auth_code)
# access_token = oauth_result.access_token

# dbx = dropbox.Dropbox(access_token)
# # Example: List files in the root directory
# for entry in dbx.files_list_folder('').entries:
#     print(entry.name)

dropbox_path = '/應用程式/Glimp/GlicemiaMisurazioni.csv.gz'
local_path = '/data/meta/GlicemiaMisurazioni.csv.gz'
# extract_path = f'./data/{datetime.datetime.today().strftime("%Y%m%d")}'
# print("Downloading Glucose file..")
# download_file_from_dropbox(access_token, dropbox_path, local_path)
# extract_gz(local_path, extract_path)


