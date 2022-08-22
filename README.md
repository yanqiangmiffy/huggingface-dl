# huggingface-dl

Command-line program to download models from huggingface.co

## Install

```text
pip install git+https://github.com/yanqiangmiffy/huggingface-dl.git
```

## Usage example

```text
huggingface_dl
    --model_name:required,huggingface model name,eg:bert-base-uncased
    --save_path:required,the local path to save model
    --proxy:option,proxy endpoints,eg:http://127.0.0.1:7890
```


* `huggingface_dl --model_name bert-base-uncased --save_path bert-base-uncased`



* `huggingface_dl --model_name=bert-base-uncased --save_path=bert-base-uncased --proxy=http://127.0.0.1:7890`

