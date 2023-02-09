# Docker

## Setup

- [Download](https://github.com/aistairc/virtualhome_unity_aist/releases/download/Build_2023_0111/Build_2023_0111_linux.zip) the VirtualHome exectable for Linux.
- unity ディレクトリ直下に Build_2023_0111_linux.zip を配置します

## Usage

```
docker compose up --build
```

### Generate Video via API

```
curl -X POST http://127.0.0.1/generate_video -d '{"script": ["<char0> [Walk] <tv> (1)"], "characters": [{"resource": "Chars/Female1"}]}' -H "Content-Type: application/json"
```
