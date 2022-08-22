import os
import shutil
from transformers import AutoTokenizer, AutoModel


def download(args):
    """
    huggingface-dl -m bert-base-uncased -s bert-base-uncased
    :param args:
    :return:
    """

    if args.proxy:
        tokenizer = AutoTokenizer.from_pretrained(args.model_name, proxies={"http": args.proxy, "https": args.proxy},
                                                  cache_dir='.cached')
        model = AutoModel.from_pretrained(args.model_name, proxies={"http": args.proxy, "https": args.proxy},
                                          cache_dir='.cached')
    else:
        tokenizer = AutoTokenizer.from_pretrained(args.model_name, cache_dir='.cached')
        model = AutoModel.from_pretrained(args.model_name, cache_dir='.cached')

    if not os.path.exists(args.save_path):
        os.makedirs(args.save_path)
    tokenizer.save_pretrained(args.save_path)
    model.save_pretrained(args.save_path)
    shutil.rmtree('.cached', ignore_errors=True)
