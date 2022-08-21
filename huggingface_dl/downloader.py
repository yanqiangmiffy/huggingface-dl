import os
from transformers import AutoTokenizer, AutoModel


def download(model_name, save_path):
    """
    huggingface-dl -m bert-base-uncased -s bert-base-uncased
    :param model_name:
    :param save_path:
    :return:
    """
    if os.path.exists(save_path):
        os.makedirs(save_path)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    tokenizer.save_pretrained(save_path)
    model.save_pretrained(save_path)
