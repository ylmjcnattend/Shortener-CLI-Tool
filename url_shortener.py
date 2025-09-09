import argparse
import requests
import sys

def shorten_url(url: str) -> str:
    api_url = f"https://tinyurl.com/api-create.php?url={url}"
    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error shortening URL: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description="URL Shortener using TinyURL API"
    )
    parser.add_argument(
        "url",
        type=str,
        help="The long URL to shorten"
    )
    args = parser.parse_args()
    short_url = shorten_url(args.url)
    print(f"Shortened URL: {short_url}")

if __name__ == "__main__":
    main()
