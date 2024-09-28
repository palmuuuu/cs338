# Being Eve

**Name:** Palmy Klangsathorn

## Diffie-Hellman

### Given:

- **g** = 7
- **p** = 97
- Alice sent Bob: 53
- Bob sent Alice: 82

### Task: Compute the Shared Secret (K)

In the Diffie-Hellman key exchange, both Alice and Bob each choose a secret number that they do not share with one another. They use these secret numbers along with the public values \( g \) and \( p \) to compute and exchange numbers. In this case, Alice sent Bob the number 53, and Bob sent Alice the number 82.

Let Alice's secret number be \( x \), and Bob's secret number be \( y \). The numbers exchanged between Alice and Bob are computed as follows:

#### Alice's Secret Number:

Alice sends Bob a value computed as:

$$
\text{Alice sent Bob} = g^x \mod p
$$

Substitute the values:

$$
53 = 7^x \mod 97
$$

To solve for \( x \):

```python
for x in range(1, 97):
    if (7**x) % 97 == 53:
        print(x)
```

Thus, the secret number \( x \) that Alice used in this Diffie-Hellman exchange is 63.

#### Bob's Secret Number:

Similarly, Bob sends Alice a value calculated as:

$$
\text{Bob sent Alice} = g^y \mod p
$$

Substituting the values:

$$
82 = 7^y \mod 97
$$

To solve for \( y \):

```python
for y in range(1, 97):
    if (7**y) % 97 == 82:
        print(y)
```

Thus, the secret number \( x \) that Bob used in this Diffie-Hellman exchange is 81.

The shared secret \( K \) is computed by both Alice and Bob using the following formulas:

$$
K*{\text{Alice}} = (\text{Bob's value})^x \mod p = 82^{63} \mod 97 = 30
$$

$$
K*{\text{Bob}} = (\text{Alice's value})^y \mod p = 53^{81} \mod 97 = 30
$$

Both computations should give the same result for the shared secret \( K = 30 \).

#### Why This Wouldn't Work with Large Integers:

In real-world applications, the numbers used in Diffie-Hellman (like g, p, and the exchanged values) are much larger (often hundreds of digits). Computing modular exponentiations for such large values requires specialized algorithms (e.g., **modular exponentiation algorithms**) and significant computational power. Without these optimizations, handling large numbers would result in overflow or extremely slow calculations, making the process impractical for everyday use.

## RSA

### Given:

Bob's Public Key

Given:

- Public key: $( e_{\text{Bob}}, n_{\text{Bob}}) = (13 , 162991)$

The encrypted message sent from Alice to Bob is represented as the following ciphertext:

```plaintext
[17645, 100861, 96754, 160977, 120780, 90338, 130962, 74096,
128123, 25052, 119569, 39404, 6697, 82550, 126667, 151824,
80067, 75272, 72641, 43884, 5579, 29857, 33449, 46274,
59283, 109287, 22623, 84902, 6161, 109039, 75094, 56614,
13649, 120780, 133707, 66992, 128221]
```

### Step 1: Factor \( n\_{\text{Bob}} \)

In order to decrypt the message, we first need to factor \( n\_{\text{Bob}} = 162991 \) into its prime factors \( p \) and \( q \):

- \( p = 379 \)
- \( q = 430 \)

Using these factors, we can compute Euler's Totient function \( \phi(n) \):

\[
\phi(n) = (p - 1) \times (q - 1) = (379 - 1) \times (430 - 1) = 378 \times 429 = 162162
\]
