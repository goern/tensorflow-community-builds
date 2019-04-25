# TensorFlow on Fedora

Red Hat's AICoE is publishing [community builds of TensorFlow](https://tensorflow.pypi.thoth-station.ninja/), these are compile with distribution specific optimizations for Fedora, Red Hat Enterprise Linux et al.

This repository demonstrates how to use the distribution specific builds of TensorFlow with Fedora 28+.

## Python Environment

We use [`pipenv`]() to manage the Python dependencies, and to use the Fedora builds of TensorFlow you have to add a source to the `Pipfile`:

```shell
[[source]]
url ="https://tensorflow.pypi.thoth-station.ninja/index/fedora29/1.13/jemalloc/simple"
verify_ssl = true
name = "redhat-aicoe-experiments"
```

This will enable pipenv to install Python modules not only from [upstream Pypi](https://pypi.org/) but also from AICoE's Python Index.

## Verify the source

Using this Python environment does not reveal where the wheel files came from, this could be verified by using [thamos](https://github.com/thoth-station/thamos):

```shell
sudo podman run --rm --tty --interactive \
    --volume `pwd`:/opt/redhat/thoth/thamos/workdir:Z \
    docker://quay.io/thoth-station/thamos:v0.3.1 \
    thamos provenance-check
2019-04-25 13:59:30,523 [1] INFO     thamos.lib: Successfully submitted provenance check analysis 'provenance-checker-db05070030046ff7'
 Digest                              |           Id           |                          Justification                               |     Package name     | Package version |         Type
=====================================+========================+======================================================================+======================+=================+======================
```

The output of thamos will tell us which Python index has been used to download the wheel file installed within the Python environment.

A quick check not verifying the provenance of the wheel but who build it is `pip show tensorflow`, it should show `Author: Red Hat Inc.`

## Test TensorFlow

Within this repository we provide a simple test script that is derived from [Thoth's micro-benchmark](https://github.com/thoth-station/performance) using to evaluate the performance of different builds of machine learning frameworks.

```shell
./app.py
TensorFlow version: 1.13.1, path: [...]
Colocations handled automatically by placer.
512 x 512 matmul took:   	2.7095 ms,	 98.97 GFLOPS
```

## Packaging it into a Container Image

TBD

### Disclaimer

I am using a Fedora 29 host system, so I have not packages it up in a container

## Copyright

Copyright (C) 2019 Red Hat Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.

The GNU General Public License is provided within the file LICENSE.