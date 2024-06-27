import json
import logging

class JSONProcessor:
    def __init__(self, filepath):
        self.data = self.load_json_file(filepath)

    def load_json_file(self, filepath):
        try:
            with open(filepath) as f:
                data = json.load(f)
                return data
        except FileNotFoundError as e:
            raise Exception(f"File not found: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"Error decoding JSON: {e}")

    def get_vm_private_ips(self):
        return self.data.get("vm_private_ips", {}).get("value", {})

    def get_network_vms(self):
        return {vm['attributes']['name']: vm['attributes']['access_ip_v4'] for vm in self.data.get("network", {}).get("vms", [])}