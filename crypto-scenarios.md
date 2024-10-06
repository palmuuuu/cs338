# Cryptographic Scenarios

**Author Name**  
Palmy Klangsathorn

---

## Simple Communication Scenarios

1. **Alice wants to send Bob a long message, and she doesn't want Eve to be able to read it. Assume AITM is impossible.**

   **Plan:**

   - Alice and Bob agree on a shared secret key \( K \) using the Diffie-Hellman key exchange.
   - Alice encrypts the long message \( M \) using AES: \( C = \text{AES}(K, M) \).
   - Alice sends \( C \) to Bob.

   **Explanation:**

   - Since \( C \) is encrypted with a symmetric key \( K \) that only Alice and Bob know, Eve cannot read the message without knowing \( K \).

---

2. **Alice wants to send Bob a long message. She doesn't want Mal to be able to modify the message without Bob detecting the change.**

   **Plan:**

   - Alice encrypts the long message \( M \) with AES using a shared key \( K \): \( C = \text{AES}(K, M) \).
   - Alice generates a hash of the message: \( H(M) \).
   - Alice signs the hash with her private key: \( \text{Sig} = E(S_A, H(M)) \).
   - Alice sends both \( C \) and \( \text{Sig} \) to Bob.

   **Explanation:**

   - Bob can decrypt \( C \) using \( K \) to retrieve \( M \) and compute \( H(M) \) to compare it with the signature \( \text{Sig} \). If they match, he knows that the message hasn't been altered.

---

3. **Alice wants to send Bob a long signed contract (C) that she doesn't want Eve to be able to read, and she wants Bob to have confidence that it was Alice who sent the message. Assume AITM is impossible.**

   **Plan:**

   - Alice and Bob agree on a shared secret key \( K \) using Diffie-Hellman.
   - Alice generates the hash of the contract \( H(C) \) and signs it: \( \text{Sig} = E(S_A, H(C)) \).
   - Alice encrypts the contract along with the signature: \( C' = \text{AES}(K, C || \text{Sig}) \).
   - Alice sends \( C' \) to Bob.

   **Explanation:**

   - Bob decrypts \( C' \) using \( K \) to retrieve \( C \) and \( \text{Sig} \). He verifies the signature against \( H(C) \) to confirm Alice's identity and ensure confidentiality against Eve.

---

## Questions About Breaking Security

1. **Alice claims, "C is not the contract I sent to Bob." What could she claim happened?**

   - **Claim 1:** **Bob modified the contract after receiving it.**

     - **Plausibility:** As a judge, I would find this plausible since Bob could theoretically alter the document before presenting it in court.

   - **Claim 2:** **Eve intercepted the contract and sent a modified version to Bob.**

     - **Plausibility:** This would be less plausible if AITM is assumed impossible, but still conceivable if we consider earlier communication vulnerabilities.

   - **Claim 3:** **There was a flaw in the digital signature or hashing process.**
     - **Plausibility:** Highly implausible if the cryptographic methods used were sound, but worth investigating if Alice can provide evidence of a vulnerability.

---

2. **For Bob’s certificate (Cert_B), what does Sig_CA consist of?**

   **Formula for Sig_CA:**
   \[
   \text{Sig*CA} = E(S*{CA}, H("bob.com" || P_B))
   \]

   **Explanation:**

   - The certificate authority (CA) signs the hash of the domain and Bob's public key, ensuring integrity and authenticity of Bob's public key.

---

3. **Is Cert_B enough for Alice to believe she's talking to Bob? What could Alice and Bob do?**

   **No, Cert_B alone is not enough.** Alice needs to verify that Bob has the corresponding secret key \( S_B \).

   **Plan:**

   - Alice can challenge Bob by sending a nonce \( N \) (a random number).
   - Bob responds by signing the nonce: \( \text{Sig}\_B = E(S_B, N) \).
   - Alice verifies \( \text{Sig}\_B \) using \( P_B \). If valid, she knows Bob owns \( S_B \).

---

4. **Ways the certificate-based trust system could be subverted.**

   - **Subversion 1:** **Mal replaces Bob's public key with his own key during the initial exchange.**

     - This allows Mal to impersonate Bob using his own private key while Alice believes she is communicating with Bob.

   - **Subversion 2:** **Mal creates a fake CA and issues certificates for public keys that he controls.**
     - Alice could be misled into trusting Mal's key as Bob's if he provides a valid-looking certificate.

---
