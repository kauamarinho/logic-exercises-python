orders = ["A123", "B456", "C789"]

def encrypt_cme(order_list, status="Pending"):
    for order in order_list:
        message = f"Order {order}: Status - {status}"
        encrypted_message = ""

        for index, character in enumerate(message):
            if character == " ":
                encrypted_message += character
            elif index % 2 == 0:
                encrypted_message += chr(ord(character) + 2)
            else:
                encrypted_message += chr(ord(character) - 1)

        print(encrypted_message)

encrypt_cme(orders)
encrypt_cme(orders, status="Sent")