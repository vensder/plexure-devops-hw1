import unittest
from aws_ip_ranges import URL, all_valid_regions, get_data, region_ip_ranges, total_ip_address_count

ip_range_regex = r'^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$'
data = get_data(URL)
region = 'us-west-1'


class TestDataType(unittest.TestCase):
    def test_data_type(self):
        self.assertIsInstance(data, dict)


class TestIfPrefixInData(unittest.TestCase):
    def test_if_prefixes_in_data(self):
        self.assertIn('prefixes', data)


class TestPrefixesType(unittest.TestCase):
    def test_prefixes_type(self):
        self.assertIsInstance(data['prefixes'], list)


class TestAllValidRegionsType(unittest.TestCase):
    def test_all_valid_regions_type(self):
        self.assertIsInstance(all_valid_regions(
            data['prefixes']), set)


class TestSpecificRegionInData(unittest.TestCase):
    def test_if_region_in_data(self):
        self.assertIn(region, all_valid_regions(
            data['prefixes']))


class TestIpRangesTypeForRegion(unittest.TestCase):
    def test_ip_ranges_type(self):
        self.assertIsInstance(region_ip_ranges(
            region, data['prefixes']), set)


class TestIpRangesRegexIPv4(unittest.TestCase):
    def test_ip_ranges_regex_ipv4(self):
        self.assertRegex(region_ip_ranges(region, data[
                         'prefixes']).pop(), ip_range_regex)

class TestTotalIpCountInIpRanges(unittest.TestCase):
    def test_total_ip_address_count(self):
        self.assertEqual(total_ip_address_count({'10.0.0.0/24',}), 256)
