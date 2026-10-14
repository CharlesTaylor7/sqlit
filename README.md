## TODO
- []  Fix code gen:
  - [ ] Sort the fields of each class, so we can put optionals after
  - [ ] Don't use mixins, they play poorly with default fields. just merge fields into the dataclass.
- [ ] handlers:

## Links
- [jsonrpc](https://www.jsonrpc.org/specification)
- [lsp](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.18/specification/#initialize)
- [basedpyright](https://docs.basedpyright.com/latest/)
- [dataclass-wizard](https://pypi.org/project/dataclass-wizard/)
- [Typescript Compiler API](https://github.com/microsoft/TypeScript/wiki/Using-the-Compiler-API)

## Development
```sh
uv tool install --python 3.14 --editable --force .
```
