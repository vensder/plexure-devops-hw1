#!/usr/bin/env python3

import urllib.request
import json
from sys import argv


arguments = argv[1:]  # remove the script name from the arguments list


URL = 'https://ip-ranges.amazonaws.com/ip-ranges.json'


def get_data(url):
    """
    The function returns decoded dictionary from the remote json
    """
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data


def all_valid_regions(prefixes):
    """
    The function return the set of all valid regions
    """
    return set(item['region'] for item in prefixes)


def print_sorted_data(data):
    """
    The function prints iterable data line by line in sorted order
    """
    for item in sorted(data):
        print(item)


def region_ip_ranges(region, prefixes):
    """
    The function returns the set of IP ranges for the region
    """
    return set(item['ip_prefix'] for item in prefixes if item['region'] == region)


def total_ip_address_count(ip_ranges):
    """
    The function returns the IP addresses count for all ranges in the region
    """
    return sum([2 ** (32 - int(ip_range.split('/')[-1])) for ip_range in ip_ranges])


if __name__ == "__main__":

    prefixes = get_data(URL)['prefixes']
    regions = all_valid_regions(prefixes)

    # If arguments not passed, run script in interactive mode
    if not arguments:
        print('\nThe AWS region names:\n')
        print_sorted_data(regions)

        region = input(
            '\nPlease pass the region name as an argument, or enter the region from the list above: ')
        while not region in regions:
            print('Sorry, your region name is not from the list above. Try again.')
            region = input('Please enter the region from the list above: ')

    # If not valid region name passed as argument, print the valid names and raise an error
    elif arguments[0] not in regions:
        print_sorted_data(regions)
        raise ValueError(
            'The AWS region name is not valid: see the list above please')

    else:
        region = arguments[0]

    ip_ranges = region_ip_ranges(region, prefixes)
    print_sorted_data(ip_ranges)
    print(
        f'The number of IP addresses in the region {region}: {total_ip_address_count(ip_ranges)}')

# TODO: move it to the separate repo to enable CI pipeline with GitHub actions
