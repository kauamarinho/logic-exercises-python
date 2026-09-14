# Engineering Modular Cipher (CME)

## Context

A development team for embedded systems is implementing a lightweight security component for internal messages exchanged between logistics controllers. To obfuscate information during communication between industrial modules, the Engineering Modular Cipher (CME) was created—a simple, efficient technique with low computational cost.

CME follows specific character-replacement rules based on each character's position in the string.

For every character in the message:

- If the character is a space, keep it unchanged.
- If the index is even (`0`, `2`, `4`, ...), add `2` to the character's ASCII code.
- If the index is odd (`1`, `3`, `5`, ...), subtract `1` from the character's ASCII code.

For example, the message:

```text
Order A123: Status - Pending
```

is transformed character by character as follows:

| Index | Character | Applied rule | Result |
| --- | --- | --- | --- |
| 0 | O | +2 (even) | Q |
| 1 | r | -1 (odd) | q |
| 2 | d | +2 (even) | f |
| 3 | e | -1 (odd) | d |
| ... | ... | ... | ... |

Spaces are preserved. The result is an obfuscated version of the message, suitable for preventing casual reading in systems where strong encryption is not feasible.

The team will use the function directly in a notebook environment, with parameters such as `status="Pending"` as the default value and order lists such as `["A123", "B456", "C789"]`, which can be changed according to the needs of each production line.

## Objective

Build a reusable function that loops through a list of order codes, creates messages with a custom or default status, applies the Engineering Modular Cipher, and prints the encrypted text using default parameters, loops, and string manipulation.

## Task

- Implement the function `encrypt_cme(order_list, status="Pending")` following these steps:
  - For every code in `order_list`, create a message in this format:
    - `Order <CODE>: Status - <STATUS>`
  - Apply the Engineering Modular Cipher (CME) to the message. For every character:
    - If it is a space, keep it unchanged.
    - If its index is even, add `2` to its ASCII value.
    - If its index is odd, subtract `1` from its ASCII value.
    - Build the encrypted string by converting the new values back into characters with `chr()`.
  - Print the encrypted result for each message.
  - Use the following test data:
    - `orders = ["A123", "B456", "C789"]`
  - Run the function as follows:
    - `encrypt_cme(orders)`
    - `encrypt_cme(orders, status="Sent")`
