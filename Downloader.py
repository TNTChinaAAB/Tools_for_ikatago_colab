import WebUtils
import Handler
import FileUtils
import Values
from ShellUtils import *

def download_libnvinfer_deb(version: str, path: str):
    repo = "https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64"
    url_ = f"{repo}/libnvinfer8_{version}_amd64.deb"
    isDownloadedFailed = Handler.isProcessFailed(3)
    isEqual = WebUtils.getUrlFileSize(url_) == FileUtils.getFileSize(path)
    if isDownloadedFailed and (not isEqual):
        status = callShell(f"wget {url_} -O {path}")
        FileUtils.chmod_file(path)
        Handler.handle_process(status, "downloaded lib1.deb", "downloading lib1.deb", 3)


def downloadKataGo():
    KATAGO_DRIVE_ID = "1b503WPLetCqZ7obkeAHoTmaz-ajJEmUX"
    size1 = FileUtils.getFileSize("./data/bins/katago")
    size2 = WebUtils.getGoogleFileSize(f"{KATAGO_DRIVE_ID}&confirm=t")
    if size1 != size2:
        callShell(f"gdown '{KATAGO_DRIVE_ID}&confirm=t' -O ./data/bins/katago")


def downloadWeights(fileId):
    _status = callShell(f"gdown '{fileId}' -O /content/work/data/weights/40b.bin.gz")
    if _status == 0:
        print("Downloaded " + Values.WEIGHT_FILE + " successfully.")
    else:
        print("There was an error while downloading " + Values.WEIGHT_FILE + ".")

