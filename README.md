# URL Shortener CLI Tool

A simple command-line Python tool to shorten URLs using the [TinyURL](https://tinyurl.com) API.

## Features

- Shortens any valid URL using TinyURL.
- Lightweight, fast, and easy-to-use.
- Command-line interface.

## Requirements

- Python 3.6+
- [`requests`](https://pypi.org/project/requests/) library

Install dependencies:
```sh
pip install requests
```

## Usage

```sh
python url_shortener.py "https://example.com/very/long/url"
```

**Output:**
```
Shortened URL: https://tinyurl.com/abc123
```

## Arguments

- `url` (required): The long URL to shorten.

## Example

```sh
python url_shortener.py "https://github.com/ylmjcnattend/ylmjcnattend"
```

## Error Handling

If the URL cannot be shortened or there is a network error, an error message will be displayed.

## License

MIT
