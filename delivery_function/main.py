from function import Delivery
if __name__ == '__main__':
    # Some examples of function action
    calculator = Delivery()
    print(calculator.calculate_delivery_cost(40, False, 'base', 'large'))
    print(calculator.calculate_delivery_cost(40, False, 'increased', 'large'))
    print(calculator.calculate_delivery_cost(40, False, 'high', 'large'))
    print(calculator.calculate_delivery_cost(40, False, 'extreme', 'large'))
    print(calculator.calculate_delivery_cost(40, False, 'base', 'small'))
    print(calculator.calculate_delivery_cost(40, False, 'increased', 'small'))
    print(calculator.calculate_delivery_cost(40, False, 'high', 'small'))
    print(calculator.calculate_delivery_cost(40, False, 'extreme', 'small'))


