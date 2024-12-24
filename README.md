# IPv4 Info Retriever

A Python wrapper that retrieves detailed information about an IPv4 address using the [ipinfo.io](https://ipinfo.io/) API. 

Provides information such as the IP's location, timezone, organization, city, and more.

## Features

- Fetch hostname, city, region, country, postal code, timezone, and organization details for an IP address.
- Detect if an IP is a bogon address.
- Retrieve latitude and longitude coordinates.
- Supports error handling for invalid IPs or API request issues.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ChocolaMilk92/GetDetailIPv4Info.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

```python
from src.ip_info import IPv4InfoRetriever

# Example: Fetch details for an IP address
ip_info = IPv4InfoRetriever("8.8.8.8")

print(f"IP Address: {ip_info.ip}")
print(f"City: {ip_info.city}")
print(f"Country: {ip_info.country}")
print(f"Latitude and Longitude: {ip_info.location}")
print(f"Timezone: {ip_info.timezone}")
print(f"Bogon Address: {ip_info.bogon}")
```

## Requirements

- Python 3.8 or higher
- `pytz`
- `urllib3`

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

