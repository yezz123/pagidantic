#!/usr/bin/env bash

set -e
set -x

echo "ENV=${ENV}"

export PYTHONPATH=.
pytest --cov=pagidantic --cov=tests --cov-report=html
