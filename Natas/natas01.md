# Natas Level 1

### Level Goal
> The goal of this level is to find the password for the next level, but right-clicking has been blocked.

### Discovery & Logic
1. **Analysis**: The website `http://natas1.natas.labs.overthewire.org` blocks right-click, preventing access to "View Page Source" via context menu.
2. **Problem**: Right-click is disabled using a JavaScript event listener, so the usual method is blocked.
3. **Solution**: Bypass the restriction by typing `view-source:` directly in the address bar, or use the keyboard shortcut `Ctrl+U` — JavaScript cannot block these methods.

### Commands Used
```
URL   : http://natas1.natas.labs.overthewire.org
User  : natas1
Pass  : 0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq
```

Access page source via address bar:
```
view-source:http://natas1.natas.labs.overthewire.org
```

In the page source:
```html
<!--The password for natas2 is [password] -->
```

### What I Learned
* **Client-Side Restrictions Are Weak**: Blocking right-click with JavaScript only prevents casual users — it is trivially bypassed with `Ctrl+U` or `view-source:` in the URL bar.
* **Security Through Obscurity**: Hiding data in HTML comments while relying on UI tricks is not a real security measure. If the data is sent to the browser, it can always be accessed.

### Password Found
<details>
  <summary>Click to reveal password</summary>
  <code>TguMNxKo9DSjfuZkj9WT928ZFvYGeRzx</code>
</details>
