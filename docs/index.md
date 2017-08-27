# Weights & Biases's documentation

This package provides an interactive CLI and python client for [wandb.ai](https://app.wandb.ai).

## Quickstart

If you want to work with private buckets or push data to the cloud you must first [signup](https://app.wandb.ai/login)

```console
$ pip install wandb
$ cd my_training_dir
$ wandb init
$ ./my_training.py arg1 | wandb my_bucket model.json weights.h5
```

To manually push files to the cloud run:

```console
$ wandb push my-new-bucket somefile.proto
```

To pull down a model or sync your local directory with the cloud you can run:

```console
$ wandb pull project/inception_v4
```

You can access configuration and push or pull via the API directly in your python scripts:

```python
import wandb
conf = wandb.Config()
wandb.sync(files=["*.h5"])
wandb.pull("transfer/learning")
```

## Documentation

```eval_rst
.. toctree::
   :maxdepth: 4

   installation
   usage
   wandb
```
   
## Reference

```eval_rst
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```