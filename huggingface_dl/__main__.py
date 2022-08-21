"""
The command-line interface for the downloader
"""
import argparse

from .downloader import download


def main():
    parser = argparse.ArgumentParser(
        description="An over-simplified downloader to demonstrate python packaging."
    )
    parser.add_argument(
        "--model_name", "-m", type=str,required=True,
        help="The URL of the resource to be downloaded."
    )
    parser.add_argument(
        "--save_path", "-s",required=True,
        help=("Destination local file path. If not set, the resource "
              "will be downloaded to the current working directory, with filename "
              "same as the basename of the URL")
    )
    args = parser.parse_args()
    file_size = download(model_name=args.model_name, save_path=args.save_path)
    print("Download successful! (size: {} B)".format(file_size))


if __name__ == "__main__":
    main()
