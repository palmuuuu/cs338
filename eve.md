# Being Eve

**Name:** Palmy Klangsathorn

## Diffie-Hellman

### Given:

- **g** = 7
- **p** = 97
- Alice picked a secret number, x: 53
- Bob picked a secret number, y: 82

### Task: Compute the Shared Secret (K)

In the Diffie-Hellman key exchange, both Alice and Bob each choose a secret number that they do not share with one another. They use these secret numbers along with the public values \( g \) and \( p \) to compute and exchange numbers. In this case, Alice secret number is 53, and Bob secreat number is 82.

Let Alice's secret number be \( x \), and Bob's secret number be \( y \). The numbers exchanged between Alice and Bob are computed as follows:

#### Alice sent to Bob:

Alice sends Bob a value computed as:

$$
\text{Alice sent Bob} = g^x \mod p
$$

Substitute the values:

$$
\text{Alice sent Bob} = 7^53 \mod 97
$$

To solve for Alice sent Bob:

```python
7**53 % 97
```

Thus, Alice sent Bob a 71.

#### Bob sent to Alice:

Similarly, Bob sends Alice a value calculated as:

$$
\text{Bob sent Alice} = g^y \mod p
$$

Substituting the values:

$$
\text{Bob sent Alice} = 7^82 \mod 97
$$

To solve for \( y \):

```python
7**82 % 97
```

Thus, Bob sent Alice a 31.

The shared secret \( K \) is computed by both Alice and Bob using the following formulas:

$$
K*{\text{Alice}} = (\text{Bob's value})^x \mod p = 31^{53} \mod 97 = 86
$$

$$
K*{\text{Bob}} = (\text{Alice's value})^y \mod p = 71^{82} \mod 97 = 86
$$

Both computations should give the same result for the shared secret \( K = 86 \).

In the Diffie-Hellman key exchange algorithm, the shared secret is the same because the two parties involved combine values to reach the same resulting value, without ever exchanging the secret itself.

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

### Step 1: Defining Variables and Formula

According to the RSA algorithm, we know that the cipher sent by Alice to Bob is encrypted using the following formula:

$$
{\text{Cipher}} = (\text{ASCII})^{e_{\text{Bob}}} \mod n_{\text{Bob}}
$$

Where $e_{\text{Bob}} = 13$
$n_{\text{Bob}} = 162991$

When we know the formula, Cipher numbers, $e_{\text{Bob}}$, and $n_{\text{Bob}}$, now we can solve for ASCII numbers

So here is the python code:

```python
cipher = [17645, 100861, 96754, 160977, 120780, 90338, 130962, 74096,
128123, 25052, 119569, 39404, 6697, 82550, 126667, 151824,
80067, 75272, 72641, 43884, 5579, 29857, 33449, 46274,
59283, 109287, 22623, 84902, 6161, 109039, 75094, 56614,
13649, 120780, 133707, 66992, 128221]

numbers = []
for i in cipher:
  for j in range(1,162991) :
    if (j**13) % 162991 == i:
      numbers.append(j)

print(numbers)
for num in numbers:
  print(chr(num), end='')
```

[17509, 24946, 8258, 28514, 11296, 25448, 25955, 27424, 29800,
26995, 8303, 30068, 11808, 26740, 29808, 29498, 12079, 30583,
30510, 29557, 29302, 25961, 27756, 24942, 25445, 30561, 29795,
26670,26991, 12064, 21349, 25888, 31073, 11296, 16748, 26979, 25902]

䑥慲⁂潢 Ⱐ 捨散欠瑨楳 ⁯ 畴⸠桴瑰猺⼯睷眮獵牶敩汬慮捥睡瑣栮楯⼠卥攠祡 Ⱐ 䅬楣攮
