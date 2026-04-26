# data-vault-2.0 documentation!

## Description

This is a data vault 2.0 implementation

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `az storage blob upload-batch -d` to recursively sync files in `data/` up to `dv_container/data/`.
* `make sync_data_down` will use `az storage blob upload-batch -d` to recursively sync files from `dv_container/data/` to `data/`.


