from analyze_log import verify_days, verify_orders


class TrackOrders:
    def __init__(self):
        self._data = []

    # aqui deve expor a quantidade de estoque
    def __len__(self):
        return len(self._data)

    def add_new_order(self, customer, order, day):
        orderByClient = dict()
        orderByClient["cliente"] = customer
        orderByClient["pedido"] = order
        orderByClient["dia"] = day
        self._data.append(orderByClient)

    def get_most_ordered_dish_per_customer(self, customer):
        orders_by_customer = dict()
        for order in self._data:
            if order["cliente"] == customer:
                if order["pedido"] not in orders_by_customer:
                    orders_by_customer[order["pedido"]] = 1
                else:
                    orders_by_customer[order["pedido"]] += 1

        return max(orders_by_customer, key=orders_by_customer.get)

    def get_never_ordered_per_customer(self, customer):
        orders = verify_orders(self._data)
        orders_by_customer = set()
        for order in self._data:
            if order["cliente"] == customer:
                if order["pedido"] not in orders_by_customer:
                    orders_by_customer.add(order["pedido"])

        return orders.difference(orders_by_customer)

    def get_days_never_visited_per_customer(self, customer):
        days = verify_days(self._data)
        customer_days = set()
        for order in self._data:
            if order["cliente"] == customer:
                if order["dia"] not in customer_days:
                    customer_days.add(order["dia"])

        return days.difference(customer_days)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
