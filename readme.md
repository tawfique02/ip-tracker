<p align="center">

```
   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
  ██║  ███╗███████║██║   ██║███████╗   ██║   
  ██║   ██║██╔══██║██║   ██║╚════██║   ██║   
  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝  
  ████████╗██████╗  █████╗  ██████╗██╗  ██╗
  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
     ██║   ██████╔╝███████║██║     █████╔╝ 
     ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ 
     ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
```

# GHOST-TRACK v3.1

**Advanced IP Intelligence & Network Recon Tool**

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux%20%7C%20Windows-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)
![Version](https://img.shields.io/badge/Version-3.1-cyan?style=flat-square)

</p>

---

## 👤 Developer

| Field | Info |
|---|---|
| **Developer** | r00td3athsh3ll01 |
| **GitHub** | [github.com/tawfique02](https://github.com/tawfique02) |
| **Telegram** | [t.me/r00td3athsh3ll01](https://t.me/r00td3athsh3ll01) |
| **Built** | 2026 |
| **Language** | Python 3 + Rich |

---

## 📌 About

GHOST-TRACK is a Python-based IP Intelligence Tool that retrieves detailed information about any IP address or domain. It runs on Linux, Termux (Android), and Windows.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔍 IP / Domain Lookup | Full geo, ISP, and security info for any IP or domain |
| 🌐 My Public IP | Full report on your own public IP |
| 📋 Bulk Scan | Scan multiple IPs or domains at once |
| 🔌 Port Scanner | Check 15 common ports (SSH, HTTP, FTP, RDP...) |
| 📡 Ping | Test latency to any target |
| 🛤️ Traceroute | Hop-by-hop network path analysis |
| 🗺️ Google Maps | Open target location directly on Google Maps |
| 💾 Save Report | Export full result to a JSON file |
| 🔗 Domain Resolve | Automatically converts URLs and domains to IP |
| 🛡️ Proxy / VPN Detection | Detects VPN, proxy, and hosting/datacenter IPs |

---

## 📋 Requirements

- Python **3.7+**
- `requests >= 2.28.0`
- `rich >= 13.0.0`

---

## ⚙️ Installation & Usage

### 🐧 Linux (Debian / Ubuntu / Kali)

```bash
# Clone the repository
git clone https://github.com/tawfique02/ip-tracker
cd ip-tracker

# Install dependencies
pip install -r requirements.txt

# Run the tool
python3 ghost.py
```

### 📱 Termux (Android)

```bash
# Install Python and Git
pkg update && pkg install python git -y

# Clone the repository
git clone https://github.com/tawfique02/ip-tracker
cd ip-tracker

# Install dependencies
pip install -r requirements.txt

# Run the tool
python ghost.py
```

> **Termux Note:** To use Traceroute, install it separately:
> ```bash
> pkg install traceroute
> ```

### 🪟 Windows

```cmd
git clone https://github.com/tawfique02/ip-tracker
cd ip-tracker
pip install -r requirements.txt
python ghost.py
```

---

## 🖥️ Menu Overview

**Main Menu:**

```
┃ [1]  IP / Domain Lookup     Track any target  ┃
┃ [2]  My Public IP           Your IP info      ┃
┃ [3]  Bulk Scan              Multiple IPs      ┃
┃ [4]  About & Help           Dev + features    ┃
┃ [0]  Exit                                     ┃
```

**After a Lookup — Action Sub-Menu:**

```
┃ [1]  Open Google Maps    View on map    ┃
┃ [2]  Ping                Check latency  ┃
┃ [3]  Traceroute          Network path   ┃
┃ [4]  Port Scan           Common ports   ┃
┃ [5]  Save JSON Report    Export to file ┃
┃ [0]  Back to Main Menu                  ┃
```

---

## 📡 APIs Used

| API | Purpose |
|---|---|
| [ip-api.com](http://ip-api.com) | Geo location, ISP, proxy/VPN detection |
| [ipwho.is](https://ipwho.is) | Currency, language, calling code, borders |
| [ipify.org](https://api.ipify.org) | Detect your own public IP address |

---

## 🖼️ Example Output

```
╔══════════════════════════════════════════════════════════════╗
║       ◉ IP INTELLIGENCE REPORT   2026-01-01 12:00:00         ║
╠══════════════════╦═══════════════════════════════════════════╣
║   IDENTITY       ║                                           ║
║   TARGET IP      ║  8.8.8.8                                  ║
║   IP TYPE        ║  IPv4                                     ║
║   IS PROXY/VPN   ║  false                                    ║
║   LOCATION       ║                                           ║
║   COUNTRY        ║  United States                            ║
║   CITY           ║  Mountain View                            ║
║   LATITUDE       ║  37.386                                   ║
║   LONGITUDE      ║  -122.0838                                ║
║   NETWORK        ║                                           ║
║   ISP            ║  Google LLC                               ║
║   ASN            ║  15169                                    ║
╚══════════════════╩═══════════════════════════════════════════╝
```

---

## 📁 File Structure

```
ghost-track/
│
├── ip_tracker.py       # Main tool
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes** and **personal network research only**. The developer is not responsible for any illegal or unauthorized use of this tool.

---

## 📞 Contact

- **Telegram:** [t.me/r00td3athsh3ll01](https://t.me/r00td3athsh3ll01)
- **GitHub:** [github.com/tawfique02](https://github.com/tawfique02)

---

<p align="center">
Made with ❤️ by <b>r00td3athsh3ll01</b>
</p>
