import csv


def marias_functions(data):
    orders_by_maria = dict()
    for order in data:
        if order["cliente"] == "maria":
            if order["pedido"] not in orders_by_maria:
                orders_by_maria[order["pedido"]] = 1
            else:
                orders_by_maria[order["pedido"]] += 1

    return max(orders_by_maria, key=orders_by_maria.get)


def arnaldo_functions(data):
    orders_by_arnaldo = dict()
    for order in data:
        if order["cliente"] == "arnaldo":
            if order["pedido"] not in orders_by_arnaldo:
                orders_by_arnaldo[order["pedido"]] = 1
            else:
                orders_by_arnaldo[order["pedido"]] += 1

    return orders_by_arnaldo["hamburguer"]


def verify_orders(data):
    orders = set()
    for order in data:
        if order["pedido"] not in orders:
            orders.add(order["pedido"])
    return orders


def verify_days(data):
    days = set()
    for order in data:
        if order["dia"] not in days:
            days.add(order["dia"])
    return days


def joao_function_orders(data):
    orders = verify_orders(data)
    orders_by_joao = set()
    for order in data:
        if order["cliente"] == "joao":
            if order["pedido"] not in orders_by_joao:
                orders_by_joao.add(order["pedido"])

    return orders.difference(orders_by_joao)


def joao_function_days(data):
    days = verify_days(data)
    joao_days = set()
    for order in data:
        if order["cliente"] == "joao":
            if order["dia"] not in joao_days:
                joao_days.add(order["dia"])

    return days.difference(joao_days)


def analyze_log(path_to_file):
    if ".csv" not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        data = []
        with open(path_to_file, encoding="utf-8") as file:
            orders = csv.reader(file, delimiter=",", quotechar='"')
            for order in orders:
                orderByClient = dict()
                orderByClient["cliente"] = order[0]
                orderByClient["pedido"] = order[1]
                orderByClient["dia"] = order[2]
                data.append(orderByClient)

        most_order_maria = marias_functions(data)

        how_many_times_arnaldo = arnaldo_functions(data)

        joao_never_order = joao_function_orders(data)

        joao_never_went = joao_function_days(data)

        with open("data/mkt_campaign.txt", "w") as txt:
            txt.write(f"""{most_order_maria}
{how_many_times_arnaldo}
{joao_never_order}
{joao_never_went}""")
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
