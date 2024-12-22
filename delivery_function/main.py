from function import Delivery
if __name__ == '__main__':
    # Some examples of function action
    calculator = Delivery()
    print(calculator.calculate_delivery_cost(40, False, 'increased', 'large'))
    print(calculator.calculate_delivery_cost(2, True, 'base', 'small'))
    print(calculator.calculate_delivery_cost(40, True, 'increased', 'large'))

