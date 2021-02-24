from collections import namedtuple

import data

from models import Machine, Pod


def get_machines(product_type: str = None, water_line_compatible: bool = None):
    machines = [Machine(sku=machine["sku"], product_type=machine["product_type"], water_line_compatible=machine["water_line_compatible"]) for machine in data.products["machines"] if (product_type is None or machine["product_type"] == product_type) and (
        water_line_compatible is None or machine["water_line_compatible"] == water_line_compatible)]
    return machines


def get_pods(product_type: str = None, coffee_flavor: str = None, pack_size: str = None):
    pods = [Pod(sku=pod["sku"], product_type=pod["product_type"], coffee_flavor=pod["coffee_flavor"], pack_size=pod["pack_size"]) for pod in data.products["pods"] if (product_type is None or pod["product_type"] == product_type) and (
        coffee_flavor is None or pod["coffee_flavor"] == coffee_flavor) and (pack_size is None or pod["pack_size"] == pack_size)]
    return pods


if __name__ == "__main__":
    print([m for m in get_pods(coffee_flavor="COFFEE_FLAVOR_CARAMEL",pack_size='7 dozen (84)')])
