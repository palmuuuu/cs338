# Being Eve

**Name:** Palmy Klangsathorn

## Diffie-Hellman

### Given:

- **g** = 7
- **p** = 97
- Alice picked a secret number, x: 53
- Bob picked a secret number, y: 82

### Task: Compute the Shared Secret (K)

In the Diffie-Hellman key exchange, both Alice and Bob each choose a secret number that they do not share with one another. They use these secret numbers along with the public values $g$ and $p$ to compute and exchange numbers. In this case, Alice secret number is 53, and Bob secreat number is 82.

Let Alice's secret number be $x$, and Bob's secret number be $y$. The numbers exchanged between Alice and Bob are computed as follows:

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

To solve for $y$:

```python
7**82 % 97
```

Thus, Bob sent Alice a 31.

The shared secret $K$ is computed by both Alice and Bob using the following formulas:

$$
K*{\text{Alice}} = (\text{Bob's value})^x \mod p = 31^{53} \mod 97 = 86
$$

$$
K*{\text{Bob}} = (\text{Alice's value})^y \mod p = 71^{82} \mod 97 = 86
$$

Both computations should give the same result for the shared secret $K = 86$.

In the Diffie-Hellman key exchange algorithm, the shared secret is the same because the two people combined values to reach the same resulting value, without ever exchanging the secret itself.

#### Why This Wouldn't Work with Large Integers?

This calculation that I have done is slower for larger numbers and can lead to overflow or extremely slow calculations. For example, the expression `7**82 % 97` can be slow because when you use `7**82`, Python computes $7^{82}$ directly. This involves calculating 7 multiplied by itself 82 times, which is computationally expensive as the exponent grows larger. The result can be an extremely large number that requires significant memory and processing power. Moreover, for very large exponents, the intermediate result of $7^{82}$ could become extremely large, leading to overflow issues in computer that do not handle big integers well. While Python does support arbitrary-precision integers, the computations still take longer for larger numbers. In addition, the operation `% 97` is performed only after calculating the full power, which means the full power is computed before any modular reduction is applied. This results in unnecessary calculations with large numbers. We should do modular instantly with powering in some ways, like property of exponentiation in modular arithmetic. So, in real-world applications, the numbers used in Diffie-Hellman (such as g and p) are much larger. Computing modular exponentiations for these large values requires specialized algorithms (like modular exponentiation algorithms, in python code is pow(x, y)) and significant power using for computer.

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

### Task: Figure out the encrypted message sent from Alice to Bob

### Step 1: Defining Variables and Formula

According to the RSA algorithm, we know that the cipher sent by Alice to Bob is encrypted using the following formula:

$$
{\text{Cipher}} = (\text{ASCII})^{e_{\text{Bob}}} \mod n_{\text{Bob}}
$$

Where $e_{\text{Bob}} = 13$,
$n_{\text{Bob}} = 162991$

With this formula, along with the cipher numbers, $e_{\text{Bob}}$, and $n_{\text{Bob}}$, we can solve for the corresponding ASCII numbers.

### Step 2: Python Code to Find the Correct ASCII Numbers

Here is the Python code used to calculate the ASCII numbers:

```python
cipher = [17645, 100861, 96754, 160977, 120780, 90338, 130962, 74096,
128123, 25052, 119569, 39404, 6697, 82550, 126667, 151824,
80067, 75272, 72641, 43884, 5579, 29857, 33449, 46274,
59283, 109287, 22623, 84902, 6161, 109039, 75094, 56614,
13649, 120780, 133707, 66992, 128221]

asciis = []
for i in cipher:
  for j in range(1,162991) :
    if (j**13) % 162991 == i:
      asciis.append(j)

print(asciis)
```

After running this code, we get the following list of ASCII numbers that Alice has encrypted:

```plaintext
asciis = [17509, 24946, 8258, 28514, 11296, 25448, 25955, 27424, 29800,
26995, 8303, 30068, 11808, 26740, 29808, 29498, 12079, 30583,
30510, 29557, 29302, 25961, 27756, 24942, 25445, 30561, 29795,
26670,26991, 12064, 21349, 25888, 31073, 11296, 16748, 26979, 25902]
```

### Step 3: Python Code to Convert ASCII Numbers to Readable Text

Here is the Python code that uses chr(num) to convert each ASCII value to a character:

```python
for num in asciis:
  print(chr(num), end='')
```

Here is the characters that I got:
䑥慲⁂潢 Ⱐ 捨散欠瑨楳 ⁯ 畴⸠桴瑰猺⼯睷眮獵牶敩汬慮捥睡瑣栮楯⼠卥攠祡 Ⱐ 䅬楣攮

Which looks meaningless (I asked my Taiwanese and Chinese friends, and they told me that this Chinese passage is meaningless), so I came back to myself and rethought it again. Now I know that I need to convert the ASCII numbers to hexadecimal numbers first, then convert them to characters.

### Step 4: Python Code to Convert ASCII Numbers to Hexadecimals

Here is the Python code that converts the numbers to hexadecimals:

```python
hex_values = []
for value in asciis:
  hex_values.append(hex(value))

print(hex_values)
```

Here is the list of hexadecimals that I got,

hex_values = ['0x4465', '0x6172', '0x2042', '0x6f62', '0x2c20', '0x6368', '0x6563', '0x6b20', '0x7468',
'0x6973', '0x206f', '0x7574', '0x2e20', '0x6874', '0x7470', '0x733a', '0x2f2f', '0x7777',
'0x772e', '0x7375', '0x7276', '0x6569', '0x6c6c', '0x616e', '0x6365', '0x7761', '0x7463',
'0x682e', '0x696f', '0x2f20', '0x5365', '0x6520', '0x7961', '0x2c20', '0x416c', '0x6963', '0x652e']

Since we cannot convert these hexadecimals one by one directly, we need to concatenate every hexadecimal into one string. Then, we can convert it to characters.

### Step 5: Combine those Hexadecimal Numbers into One String and Convert each Consecutive Pair to a Character.

Here is Python code to concatenate those hexadecimals by removing the '0x' and concatenating them into one string, and then converting those consecutive pairs to characters.

```python
hex_string = ''.join(hex_values).replace('0x', '')

ascii_chars = ''
for i in range(0, len(hex_string), 2):
    ascii_chars += chr(int(hex_string[i:i+2], 16))

print(ascii_chars)
```

This is the message that Alice sent to Bob that I got:

`Dear Bob, check this out. https://www.surveillancewatch.io/ See ya, Alice.`

#### If the integers involved were much larger, the following issues might arise:

- **Computation Time**: Calculating large powers with modular arithmetic would be slow without efficient algorithms like modular exponentiation, as mentioned above. Moreover, the power of a number followed by a modulus can be repeatedly overworked since we can apply the properties of modular exponentiation to solve it (because the modulus yields the same result).

- **Memory**: Handling large numbers can quickly consume significant memory and time, especially in less optimized environments.

#### Why Alice's Message Encoding Is Insecure?

Even if Bob's keys involve larger integers, Alice's message encoding would still be insecure because:

- **The Concepts**: Since everyone knows the concept of RSA and how prime numbers, factoring, and modular arithmetic work, people can run programs (using already established processes) to solve for the prime numbers. While it’s difficult, with a powerful computer and enough time, it might be feasible. Furthermore, since we can easily know somebody's public key, we can attempt to solve for the private key.

- **ASCII**: The message is encoded directly as ASCII without any additional encryption layers.

- **Predictable Content**: If parts of the message are predictable (such as common phrases or headers), someone can deduce parts of the plaintext.
