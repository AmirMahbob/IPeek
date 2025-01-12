# IPeek - A Tool for IP and Domain Information 🌐

IPeek is a Python-based GUI application designed to fetch and display information about IP addresses and domains. It uses CustomTkinter for its interface and integrates APIs and Python libraries to provide a seamless experience.

---

## ✨ Features

- 🔍 **IP Address Lookup:** Fetch detailed information about any public IP address.
- 🌐 **Domain Resolution:** Convert domain names to IP addresses and retrieve information.
- 🛡️ **Private IP Detection:** Detect private IPs and notify the user that they don't have public information.
- 📡 **Internet Connection Check:** Ensure connectivity before making API requests.
- 🎨 **User-Friendly Interface:** Clean and responsive GUI built with CustomTkinter.
- ⚙️ **Error Handling:** Handles invalid inputs and displays meaningful error messages.

---

## ⚙️ Requirements

Before running the application, ensure the following dependencies are installed:

- Python 3.7+
- Required libraries:
  - `customtkinter`
  - `tkinter`
  - `requests`
  - `Pillow`

Install dependencies using the following command:

```bash
pip install customtkinter
pip install tkinter
pip install requests
pip install pillow
```

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ipeek.git
   cd ipeek
   ```

2. Ensure you have the required dependencies installed.

3. Run the application:
   ```bash
   python app.py
   ```

---

## 🛠️ Usage

1. Launch the application.
2. Enter an IP address or domain name in the input field.
3. Press the **Submit** button or hit `Enter`.
4. If the input is valid, the application fetches information and displays it in a user-friendly format.

---

## 🌟 Example

- **Input:** `8.8.8.8`
- **Output:**
  ```
  IP: 8.8.8.8
  Country: United States
  Region: California
  City: Mountain View
  Lat: 37.4056
  Lon: -122.0775
  ISP: Google LLC
  Timezone: America/Los_Angeles
  Org: Google Public DNS
  ```

---

## 📂 Project Structure

```
.
├── app.py                  # Main GUI application
├── find_ip.py              # Backend logic for IP and domain lookup
├── find_ip_picture.png     # Background image for the GUI
└── README.md               # Project documentation
```

---

## ⚠️ Known Issues

- Ensure a stable internet connection for proper functionality.
- Only works with public IPs and valid domain names.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 💡 Acknowledgments

- [ip-api.com](https://ip-api.com) for providing the IP lookup API.
- The Python community for their amazing libraries and support.

---
