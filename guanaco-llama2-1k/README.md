---
dataset_info:
  features:
  - name: text
    dtype: string
  splits:
  - name: train
    num_bytes: 1654448
    num_examples: 1000
  download_size: 966693
  dataset_size: 1654448
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# Guanaco-1k: Lazy Llama 2 Formatting

This is a subset (1000 samples) of the excellent [`timdettmers/openassistant-guanaco`](https://huggingface.co/datasets/timdettmers/openassistant-guanaco) dataset, processed to match Llama 2's prompt format as described [in this article](https://huggingface.co/blog/llama2#how-to-prompt-llama-2). It was created using the following [colab notebook](https://colab.research.google.com/drive/1Ad7a9zMmkxuXTOh1Z7-rNSICA4dybpM2?usp=sharing).

Useful if you don't want to reformat it by yourself (e.g., using a script). It was designed for [this article](https://mlabonne.github.io/blog/posts/Fine_Tune_Your_Own_Llama_2_Model_in_a_Colab_Notebook.html) about fine-tuning a Llama 2 (chat) model in a Google Colab.
