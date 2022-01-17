class Client:
    name = 'default'
    phone = '(123)456-7890'
    email = 'abc@gmail.com'
    purchases = 0


def main():
    firstClient = Client()
    firstClient.name = "James Tam"
    firstClient.email = 'tam@ucalgary.com'
    print(firstClient.name)
    print(firstClient.phone)
    print(firstClient.email)
    print(firstClient.purchases)


main()