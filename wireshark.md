# Wireshark Assignment

**Name**: Palmy Klangsathorn

After examining the list of network frames shown in the main Wireshark display, I identified a total of 8 frames, including the following:

| Frame | Source       | Destination  | Protocol | Packet     |
| ----- | ------------ | ------------ | -------- | ---------- |
| 1     | 192.168.64.2 | 129.6.15.28  | TCP      | [SYN]      |
| 2     | 129.6.15.28  | 192.168.64.2 | TCP      | [SYN, ACK] |
| 3     | 192.168.64.2 | 129.6.15.28  | TCP      | [ACK]      |
| 4     | 129.6.15.28  | 192.168.64.2 | DAYTIME  | Response   |
| 5     | 129.6.15.28  | 192.168.64.2 | TCP      | [FIN, ACK] |
| 6     | 192.168.64.2 | 129.6.15.28  | TCP      | [ACK]      |
| 7     | 192.168.64.2 | 129.6.15.28  | TCP      | [FIN, ACK] |
| 8     | 129.6.15.28  | 192.168.64.2 | TCP      | [ACK]      |

===== DAYTIME =====

**1. Identify the parts of the TCP 3-way handshake by listing the frame summaries of the relevant frames:**

1 192.168.64.2 129.6.15.28 TCP [SYN]  
2 129.6.15.28 192.168.64.2 TCP [SYN, ACK]  
3 192.168.64.2 129.6.15.28 TCP [ACK]

**2. What port number does the client (i.e. nc on your Kali computer) use for this interaction?**

In this case, we used port 13.

**3. Why does the client need a port?**

The client needs a port to establish a unique communication endpoint. This port allows the client to receive responses from the server and maintain a separate channel for each communication session.

**4. What frame contains the actual date and time? (Show the frame summary as in question 1 above.)**

4 129.6.15.28 192.168.64.2 DAYTIME Response

**5. What do [SYN] and [ACK] mean?**

- **[SYN]**: Synchronize. This flag is used to initiate the TCP connection. It indicates that a client wants to start a communication session with the server.
- **[ACK]**: Acknowledge. This flag is used to confirm the receipt of a previous packet.

**6. Which entity (the nc client or the daytime server) initiated the closing of the TCP connection? How can you tell?**

The **daytime server** initiated the closing of the TCP connection. This is evident from Frame 5:
5 129.6.15.28 192.168.64.2 TCP [FIN, ACK]

The server sends a `FIN` (finish) flag to indicate that it wants to close the connection.
