# Pure Storage Unified Python SDK

## Overview

The `py-pure-client` Python package provides clients that use the Pure1 1.x REST API
and the FlashArray REST 2.x API.

For the current FlashBlade REST 1.x Python SDK, [see here](https://github.com/purestorage/purity_fb_python_client).
For the current FlashArray REST 1.x Python SDK, [see here](https://pypi.org/projects/purestorage).

## Requirements

The library requires Python 2.7 and higher or Python 3.3 and higher. Third-party
libraries are also required.

## Installation
The Pure Storage Unified SDK supports two installation methods:

#### Pure1 API Encrypted Private Key Support
Use this installation method if support is required for encrypted private keys
(i.e. via passphrase). This method uses the [`Paramiko`][1] Python Module to
decrypt passphrase-protected private keys.

***Please note:*** The Paramiko module has dependencies that are not pure python,
so the installation will be platform-specific (ie. not easily portable).

```
pip install py-pure-client[paramiko]
```

#### Pure Python
Use this method if a pure Python implementation is desired, and there is no need
to support private keys with passphrases.

***Please note:*** If a password is supplied when creating a new  to supply a
password when creating a new `pypureclient.pure1.Client`, it will be ignored.

```
pip install py-pure-client
```

## Documentation

For full documentation, including a quick start guide and examples, see https://py-pure-client.readthedocs.io/en/latest/.

[1]: https://github.com/paramiko/paramiko
