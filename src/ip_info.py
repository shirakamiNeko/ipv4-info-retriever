"""
The MIT License (MIT)

Copyright (c) 2024 ChocolaMilk92

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import json
import pytz
import urllib3
from datetime import datetime

class GetDetailIPv4Info:
    """
    Get detailed information about an IPv4 address.

    This class retrieves information about an IPv4 address using the ipinfo.io API. 
    Returns details such as the IP's hostname, city, region, country, location, timezone, organization, and more.

    Parameters
    ----------
    ip_address : str
        The IPv4 address to retrieve information for. Defaults to "json", which fetches details for the client IP.

    Attributes
    ----------
    all : dict
        A dictionary containing all relevant information about the IP address.

    hostname : str
        The hostname associated with the IP address.

    ip : str
        The IP address itself.

    city : str
        The city associated with the IP address.

    region : str
        The region/state associated with the IP address.

    country : str
        The country associated with the IP address.

    location : tuple
        A tuple containing the latitude and longitude of the IP address.

    organization : str
        The organization associated with the IP address.

    postal : str
        The postal code associated with the IP address.

    time : datetime.datetime
        The current UTC time in the IP address's timezone.

    timezone : str
        The timezone associated with the IP address.

    bogon : bool
        A boolean indicating whether the IP address is a bogon address.

    Returns
    -------
    dict
        A dictionary containing all available details about the IPv4 address.

    Raises
    ------
    ValueError
        If the API returns an error, such as an invalid IP address or rate-limit exceeded.

    Exception
        For any other unexpected errors during the API call.

    Examples
    --------
    Retrieve information about a public IP address:

    >>> from getdetailipv4info import GetDetailIPv4Info
    >>> ip_info = GetDetailIPv4Info("8.8.8.8")
    >>> ip_info.city
    'Mountain View'
    >>> ip_info.country
    'US'
    >>> ip_info.location
    ('37.3860', '-122.0838')

    Handle invalid IP addresses:

    >>> try:
    >>>     ip_info = GetDetailIPv4Info("invalid_ip")
    >>> except ValueError as e:
    >>>     print(f"Error: {e}")
    
    """
    def __init__(self, ip_address: str = "json") -> None:
        self.ip_address = ip_address
        https = urllib3.PoolManager()
        url = f'https://ipinfo.io/{self.ip_address}'
        try:
            response = https.request('GET', url)
            self.all_data = json.loads(response.data)
            # Handling error
            if "status" in self.all_data:
                error = self.all_data["error"]
                raise ValueError(f"{self.all_data["status"]} {error["title"]}: {error["message"]}")
        except Exception as e:
            raise e
        
    def __repr__(self):
        return str(self.all_data)
        
    @property
    def all(self) -> dict:
        "Returns all information as a dictionary"
        return self.all_data
    
    @property
    def hostname(self) -> str:
        "Returns the hostname associated with the IP"
        return self.all_data["hostname"] if "hostname" in self.all_data else None

    @property
    def ip(self) -> str:
        "Returns the IP address"
        return self.all_data["ip"] if "ip" in self.all_data else None
    
    @property
    def city(self) -> str:
        "Returns the city of the IP belongs to"
        return self.all_data["city"] if "city" in self.all_data else None
    
    @property
    def region(self) -> str:
        "Returns the region of the IP belongs to"
        return self.all_data["region"] if "region" in self.all_data else None
    
    @property
    def country(self) -> str:
        "Returns the country of the IP belongs to"
        return self.all_data["country"] if "country" in self.all_data else None
    
    @property
    def location(self) -> tuple:
        "Returns the latitude and longitude information of the IP"
        return tuple(self.all_data["loc"].split(",")) if "loc" in self.all_data else None
    
    @property
    def organization(self) -> str:
        "Returns the organization of the IP belongs to"
        return self.all_data["org"] if "org" in self.all_data else None
    
    @property
    def postal(self) -> str:
        "Returns the postal code of the IP"
        return self.all_data["postal"] if "postal" in self.all_data else None
    
    @property
    def time(self) -> datetime:
        "Returns the current UTC time of the IP"
        return datetime.now(pytz.timezone(self.all_data["timezone"])) if "timezone" in self.all_data else None

    @property
    def timezone(self) -> pytz.timezone:
        "Returns the timezone of the IP"
        return pytz.timezone(self.all_data["timezone"]) if "timezone" in self.all_data else None
    
    @property
    def bogon(self) -> bool:
        "Checks if the IP is a bogon address"
        return self.all_data["bogon"] if "bogon" in self.all_data else None


