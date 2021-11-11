# ⌨️ Python Keylogger
This is a keylogger made with python that log the data to your discord server with webhook integration. Once this script is running, it collects all the key press data and logs it to discord at specific interval! It is fully configurable!

- [Setup](#%EF%B8%8F-warning)
- [Configuration](#%EF%B8%8F-configuration)
- [Live Example](#⚒️-Example)

## ⚠️ Warning
This project is only for demonstration/educational purpose and I am not responsible for anything. Use at your own risk!

# ⚙️ Setup

### 📃 Prerequisite

- [Python 3 ](https://www.python.org/downloads/)
- A discord server with webhook integration
- [Install requirements.txt](requirements.txt)

### 🪚 requirements
For setup, you have to install the requirements, for that go to the root directory and run the following command

```
 pip install -r requirements.txt
```

After installing the requirements, run the script:
```
python app.py
```

# ✒️ Configuration
In the [app.py](app.py) file you can configur the keylogger. Change the following variables accordingly

| Variable        | Value                                       | Type     |
|-----------------|---------------------------------------------|----------|
| webhook         | Your discord Webhook URL                    | `string` |
| smuggleInterval | Interval in which, Script will log the data | `int`    |

# ⚒️ Example
After Setting up this, you can try using the keylogger with the default webhook url in the script. Join this [server](https://discord.gg/mteKzphDGT) to try it! This is a record of me trying to sing in to github! <br><br>
![Example](https://i.imgur.com/TxvzeGA.png)

# 💪 Support
Please support this repo by starring it ⭐<br><br>
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/J3J16V6AZ)
