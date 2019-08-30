from subprocess import Popen, PIPE
import json
from shutil import which

class AzureError(Exception):
    pass

def azure_proxy(command, *args, **kwargs):
    if "replace_underscore" in kwargs.keys():
        replace_underscore = kwargs["replace_underscore"]
        del kwargs["replace_underscore"]
    else:
        replace_underscore = True
    flags = [
        "--{key}=\"{value}\"".format(
            key=(key.replace("_", "-") if replace_underscore else key),
            value=val) for key, val in kwargs.items()
        ]
    f = Popen(" ".join([
        "az",
        command,
        *["\"{}\"".format(arg) for arg in args],
        *flags
    ]),
    stdout=PIPE,
    stderr=PIPE,
    shell=True
    )
    if f.wait() == 0:
        return json.loads(f.stdout.read().decode("utf-8"))
    else:
        raise AzureError(f.stderr.read().decode("utf-8"))

class Azure:
    def __init__(self):
        pass
    def __getattribute__(self, attr):
        attributes = attr.split("_")
        if attributes[-1] == "":
            attributes.pop(-1)
        def run_azure(*args, **kwargs):
            return azure_proxy(*attributes, *args, **kwargs)
        return run_azure

if which("az") == None:
    raise FileNotFoundError("\'az\' command was not found in your environment. Ensure it is installed and set up properly.")

if __name__ == '__main__':
    az = Azure()
    print(az.account_show())

__all__ = [Azure, AzureError]
