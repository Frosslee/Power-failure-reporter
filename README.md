

## 📝 Report Power Failure Automation

This Python script automates submitting power failure reports to the **Tshwane Power Failure** website using Selenium with **Microsoft Edge WebDriver**.

It:
Loads queries (account numbers + house numbers) from a `queries.json` file.
Submits the form on the website for each query.
Saves the responses into a `results.json` file.
Saves the responses into a `responses.txt` file.



### 📂 Project Structure

```
.
├── main.py
├── queries.json
├── results.json   # (output)
├── responses.txt   # (output)
├── requirements.txt
└── README.md
```


## 🔧 Requirements

Python 3.7+
Microsoft Edge installed
Microsoft Edge WebDriver compatible with your browser version

Install Python dependencies:

```bash
pip install -r requirements.txt
```


## queries.json format

Create a `queries.json` in the same folder with your account numbers and house numbers:

```json
[
  { "house_number": "num", "account_number": "num" },
  { "house_number": "num", "account_number": "num" },
  { "house_number": "num", "account_number": "num" }
]
```

Each object maps a **house number** to an **account number or prepaid meter serial number**.


## How to run

1. Download the **Edge WebDriver** matching your Edge browser version:
   [https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

2. Place the `msedgedriver.exe` somewhere on your system.

3. In `main.py`, update this line with your WebDriver path:

```python
service = Service(executable_path=r"C:/path/to/msedgedriver.exe")
```

4. Run the script:

```bash
python main.py
```


## Output

After running:

1. **`results.json`** → contains structured responses keyed by house number.
2. **`responses.txt`** → contains readable text lines like:

```
House Number: num - Response: Your call Ref num of date for a power failure at address will be attended to soon.
```

## Notes

- The script uses **headless mode** (runs without UI).
  Remove `options.add_argument("--headless")` in `main.py` if you want to see the browser.

- Adjust `time.sleep(3)` if the website takes longer/shorter to return a response.

- Ensure no CAPTCHA or additional login/authentication is required.
