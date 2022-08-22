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
        "--model_name", "-m", type=str, required=True,
        help="The URL of the resource to be downloaded."
    )
    parser.add_argument(
        "--save_path", "-s", required=True,
        help=("Destination local file path. If not set, the resource "
              "will be downloaded to the current working directory, with filename "
              "same as the basename of the URL")
    )

    parser.add_argument(
        "--proxy", "-p",
        help="The  proxy endpoints,eg http://127.0.0.1:7890"
    )
    parser.add_argument(
        "--cache_dir", "-c",default='.cached',
        help="Path to a directory in which a downloaded pretrained model configuration should be cached if the standard cache should not be used."
    )
    args = parser.parse_args()
    # file_size = download(model_name=args.model_name, save_path=args.save_path)
    file_size = download(args)
    print("Download successful! (size: {} B)".format(file_size))


if __name__ == "__main__":
    main()
