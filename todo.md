- [x] lsp
- [x] formatter
- [x] parse stdin
- [x] parse lsp initialize
  - [x] pydantic vs dataclass-wizard

- [x] configure neovim to load goose for sql files
  - [ ] neovim command to open LSP error buffer
  - [ ] neovim command to clear LSP Error log
  - [x] nushell command to grep lsp error log
- [x] connect neovim to running goose server
  - [x] ftplugin for sql to connect to running goose
  - [x] goose lsp needs to support stdio & sockets
    - [x] python read and write to socket

- [x] goose needs to unlink existing sock file
- [x] goose parses content headers and lsp dataclass
- [ ] goose needs to report lsp capabilities
  


Links:
- [jsonrpc](https://www.jsonrpc.org/specification)
- [lsp](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/#initialize)
- [basedpyright](https://docs.basedpyright.com/latest/)
- [dataclass-wizard](https://pypi.org/project/dataclass-wizard/)

## Development
```sh
uv tool install --python 3.14 --editable --force .
```
  
