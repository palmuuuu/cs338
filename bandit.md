# Solutions for Solving Bandit Challenges

## Level 0

- **SSH Command**: `ssh -p 2220 bandit0@bandit.labs.overthewire.org`
- **Password**: `bandit0`

---

## Level 0 -> Level 1

1. Run `ls` to check the files/folders in the directory.
2. Use `cat readme` to view the password inside the `readme` file.

- **Password**: `ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If`

---

## After this, the SSH number will change based on the level, and the password will be the one from the previous level.

## Level 1 -> Level 2

1. Run `ls` to list the contents of the directory.
2. Use `cat ./-` to view the contents of the file named `-`. Since the `-` is a special character, so we need to add `./` to identify `-`.

- **Password**: `263JGJPfgU6LtdEvgfWU1XP5yac29mFx`

---

## Level 2 -> Level 3

1. Run `ls` to list the contents of the directory.
2. Notice the file `spaces in this filename`.
3. Use `cat spaces` and press `Tab` to autocomplete the file name, or use the command `cat spaces\ in\ this\ filename` (the `\` is used to escape spaces).

- **Password**: `MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx`

---

## Level 3 -> Level 4

1. Run `ls` to list the contents of the directory.
2. Notice the directory named `inhere`.
3. Use `cd inhere/` to navigate into the `inhere` directory.
4. Run `ls` again, and notice that there are no visible files because the file is hidden.
5. Run `ls -a` to show the hidden file. Now, `...Hiding-From-You` shows.
6. Use `cat ...Hiding-From-You` to view the text inside that hidden file.

- **Password**: `2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ`

---

## Level 4 -> Level 5

1. Run `ls` to list the contents of the directory.
2. Notice the directory named `inhere`.
3. Use `cd inhere/` to navigate into the `inhere` directory.
4. Run `ls` to list the contents of the `inhere` directory.
5. The password for the next level is stored in the only human-readable file in the inhere directory. So, I `cat` every file here. Since, the file starts with `-`. So, I need to type `./-` before every file here.
6. I did `cat` for every file until I got the human-readable one, then I got the password when I did `cat ./-file07`

- **Password**: `4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw`

---

## Level 5 -> Level 6

1. Run `ls` to list the contents of the directory.
2. Notice the directory named `inhere`.
3. Use `cd inhere/` to navigate into the `inhere` directory.
4. Run `ls` to list the contents of the `inhere` directory.
5. Now I see 20 contents inside, but I don't know which one. The clue told me that the password has all of the following properties: human-readable, 1033 bytes in size, and not executable. So, I use `find` to find the file with 1033 bytes in size,
   run `find . -type f -size 1033c`.
6. I got `./maybehere07/.file2`, then run `cat ./maybehere07/.file2`.

- **Password**: `HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`

---

## Level 6 -> Level 7

1. Run `ls` to list the contents of the directory. And there is no content inside this directory.
2. The clue told me that the password has all of the following properties: owned by user bandit7, owned by group bandit6, and 33 bytes in size.
3. Run `cd /` to go to the root directory.
4. Run `find . -size 33c -user bandit7 -group bandit6 | grep bandit7`. Then, it gives you a chunk of lines that owned by user bandit7, owned by group bandit6, and 33 bytes in size. Now you need to look for the bandit7.password. And I found `./var/lib/dpkg/info/bandit7.password`.
5. Run `cat ./var/lib/dpkg/info/bandit7.password`.

- **Password**: `morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`

---

## Level 7 -> Level 8

1. Run `ls` to list the contents of the directory. And now we see the file `data.txt`. The password for the next level is stored in the file data.txt next to the word millionth.
2. Run `cat data.txt | grep millionth`. grep is the commind-line serching for specific pattern, here it looks for the word millionth.

- **Password**: `dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc`

---

## Level 8 -> Level 9

1. Run `ls` to list the contents of the directory. And now we see the file `data.txt`. The password for the next level is stored in the file data.txt and is the only line of text that occurs only once.
2. Run `sort data.txt | uniq -u`. Because `uniq` is the commind-line that indicate the uniqeness or the only line of text that occurs only once.

- **Password**: `4CKMh1JI91bUIZZPXDqGanal4xvAg0JM`

---

## Level 9 -> Level 10

1. Run `ls` to list the contents of the directory. And now we see the file `data.txt`. The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.
2. Run `strings data.txt | grep '==='`. Here, I just typed 3 equals, but you can add more.

- **Password**: `FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey`

---

## Level 10 -> Level 11

1. Run `ls` to list the contents of the directory. And now we see the file `data.txt`. The password for the next level is stored in the file data.txt, which contains base64 encoded data.
2. Run `base64 -d data.txt`

- **Password**: `dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr`

---

## Level 11 -> Level 12

1. Run `ls` to list the contents of the directory. And now we see the file `data.txt`. The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions.
2. Run `tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt`, because the `tr` is the command-line that used to substitute the character. Here, It's substituting the character with the one 13 positions after for all character. So, A substituted by N, etc.

- **Password**: `7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4`
