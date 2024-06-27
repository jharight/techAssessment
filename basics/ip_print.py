import json
import sys

def print_ip_addresses(filename):
    try:
        with open(filename) as f:
            data = json.load(f)

        vm_private_ips = data.get('vm_private_ips', {}).get('value', {})
        network_vms = {vm['attributes']['name']: vm['attributes']['access_ip_v4'] for vm in data.get('network', {}).get('vms', [])}

        for vm_name, ip in vm_private_ips.items():
            print(ip, end='')
            if vm_name in network_vms:
                print(f" {network_vms[vm_name]}")
            else:
                print()

    except FileNotFoundError:
        print("File not found. Please make sure the file exists.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except KeyError as e:
        print(f"Key not found in JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ip_print.py FILENAME")
        sys.exit(1)

    filename = sys.argv[1]
    print_ip_addresses(filename)