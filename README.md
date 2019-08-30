# gcloud-pyproxy

This Python package provides a proxy class for calling gcloud commands directly from Python.

## Requirements

- [gcloud](https://cloud.google.com/sdk/gcloud/)
- Python 3.x

## Installation

## Via PIP

```console
pip3 install gcloudpyproxy
```

or

```console
python3 -m pip install gcloudpyproxy
```

## Building from source

```console
wget https://github.com/tomasvotava/gcloud-pyproxy/archive/master.zip
unzip master.zip
cd gcloud-pyproxy-master
python setup.py build
python setup.py install
```

## Usage

```python
from gcloud_pyproxy import GCloud
gcloud = GCloud()

# comamnd: gcloud compute instances list
gcloud.compute_instances_list()

# command: gcloud compute instances start virtual
gcloud.compute_instances_start("virtual")

# additional flags and parameters
# next method call expands like this:
# gcloud compute instances list --project="gcp-project-id"
gcloud.compute_instances_list(project="gcp-project-id")

# positional arguments are simply concatenated after the command call
gcloud.compute_instances_start("virtual", project="gcp-project-id")
# expands as:
# gcloud compute instances start virtual --project="gcp-project-id"

# by default, underscores in flag names are replaced with dashes
gcloud.kms_encrypt(plaintext_file="file.txt")
# gcloud kms encrypt --plaintext-file="file.txt"

# however, this can be overriden by specifying replace_underscore=False
gcloud.kms_encrypt(plaintext_file="file.txt", replace_underscore=False)
# gcloud kms encrypt --plaintext_file="file.txt"
```
