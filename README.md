# Task 1

Write a script using your preferred scripting language to download the AWS IP Ranges JSON File https://ip-ranges.amazonaws.com/ip-ranges.json and print all the IP ranges for a region name, when passed as a command-line argument, print an error when an invalid region is passed to your script.

For example:

```sh
$sh print_aws_ip_ranges.sh eu-west-1
```

Should output all the IP ranges assigned to the region, passed as the command line argument.

[Bonus points]: Print the total sum of the numbers in the output.

## Implementation

The script has the unit tests, which run by CI system GitHub Actions by push or PR to master.

The tests passed for Python 3.6, 3.7, 3.8 versions.

Script output IP ranges for the region passed as an argument.

Additionally, script output the number of the possible IP addresses in the entire of the region.

```sh
./aws_ip_ranges.py cn-north-1
140.179.0.0/16
15.230.41.0/24
150.222.88.0/24
150.222.89.0/24
52.80.0.0/16
52.80.198.136/29
52.81.0.0/16
52.95.255.144/28
54.222.0.0/19
54.222.128.0/17
54.222.32.0/22
54.222.36.0/22
54.222.48.0/22
54.222.52.0/22
54.222.57.0/24
54.222.58.0/28
54.222.58.32/28
54.222.58.48/28
54.222.59.0/24
54.222.64.0/23
54.222.66.0/23
54.222.70.0/24
54.222.76.0/22
54.223.0.0/16
54.239.0.144/28
The number of IP addresses in the region cn-north-1: 310872
```

Script print the list of all valid regions and raise an error if passed not valid region:

```sh
./aws_ip_ranges.py non-exist-region
GLOBAL
af-south-1
ap-east-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-south-1
ap-southeast-1
ap-southeast-2
ap-southeast-3
ca-central-1
cn-north-1
cn-northwest-1
eu-central-1
eu-north-1
eu-south-1
eu-west-1
eu-west-2
eu-west-3
me-south-1
sa-east-1
us-east-1
us-east-2
us-gov-east-1
us-gov-west-1
us-west-1
us-west-2
Traceback (most recent call last):
  File "./aws_ip_ranges.py", line 63, in <module>
    'The AWS region name is not valid: see the list above please')
ValueError: The AWS region name is not valid: see the list above please
```

If the parameter is not passed, the script runs in an interactive mode:

```sh
./aws_ip_ranges.py

The AWS region names:

GLOBAL
af-south-1
ap-east-1
ap-northeast-1
ap-northeast-2
ap-northeast-3
ap-south-1
ap-southeast-1
ap-southeast-2
ap-southeast-3
ca-central-1
cn-north-1
cn-northwest-1
eu-central-1
eu-north-1
eu-south-1
eu-west-1
eu-west-2
eu-west-3
me-south-1
sa-east-1
us-east-1
us-east-2
us-gov-east-1
us-gov-west-1
us-west-1
us-west-2

Please pass the region name as an argument, or enter the region from the list above: cn-northwest-1
161.189.0.0/16
52.82.0.0/17
52.82.1.0/29
52.82.160.0/22
52.82.164.0/22
52.82.168.0/24
52.82.169.0/28
52.82.169.16/28
52.82.176.0/22
52.82.180.0/22
52.82.184.0/23
52.82.187.0/24
52.82.188.0/22
52.82.192.0/18
52.83.0.0/16
54.239.0.176/28
68.79.0.0/18
The number of IP addresses in the region cn-northwest-1: 202808
```
