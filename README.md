# Here's a complete README.md file you can copy and paste:

```markdown
# Network Scanner Pro 🔍

A professional, multi-threaded network discovery tool developed by **Fourat Beji** that efficiently scans local networks to identify active devices with detailed information.

![Network Scanner](https://img.shields.io/badge/Network-Scanner-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6%2B-green?style=for-the-badge)
![Multi-Platform](https://img.shields.io/badge/Windows-Linux%20%7C%20macOS-lightgrey?style=for-the-badge)

## ✨ Features

- **Fast Multi-threaded Scanning** - Concurrent pinging for rapid results
- **Hostname Resolution** - Identifies device names alongside IP addresses
- **Real-time Progress Display** - Visual progress bar and spinner
- **Professional UI** - Color-coded console output with elegant formatting
- **Cross-Platform** - Works on Windows, macOS, and Linux
- **Detailed Reporting** - Comprehensive scan statistics and results
- **Easy to Use** - Simple command-line interface

## 🚀 Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Fourat4AT/Network-Scanner-Pro.git
cd Network-Scanner-Pro
```

2. **Ensure you have Python 3.6+ installed**:
```bash
python --version
```

## 💻 Usage

### Basic Scan (Default Network):
```bash
python scanner.py
```

### Scan Specific Network:
```bash
python scanner.py 192.168.0
python scanner.py 10.0.0
```

### Command Line Arguments:
- `[network_prefix]` - Optional network prefix (e.g., "192.168.1", "10.0.0")
- If omitted, defaults to 192.168.1.0/24 network

## 📊 Output Example

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗    ║
║    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗   ║
║    ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝   ║
║    ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗   ║
║    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║   ║
║    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝   ║
║                                                              ║
║                   S C A N N E R  P R O                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝

                    NETWORK DISCOVERY SUITE
          Enterprise-Grade Scanning Technology
                 Developed by: Fourat Beji
──────────────────────────────────────────────────────
[+] Initializing network discovery protocol...

Target Network: 192.168.1.0/24
Scan Started: 14:32:45
──────────────────────────────────────────────────────
[+] Deploying scanning threads...
⣾ Scanning: [████████████████████░░░░░░░░░░] 65.4% | Devices: 8

[+] Scanning Completed!
══════════════════════════════════════════════════════════════
SCAN RESULTS SUMMARY
══════════════════════════════════════════════════════════════
Scan Date: 2023-10-15 14:33:12
Scan Duration: 27.45 seconds
IPs Scanned: 254
Active Devices Found: 8
──────────────────────────────────────────────────────

ACTIVE DEVICES:
IP Address           Hostname                           Status
──────────────────────────────────────────────────────
192.168.1.1          router.home                        Online
192.168.1.15         DESKTOP-PC                         Online
192.168.1.23         Unknown                            Online
192.168.1.42         android-device                     Online
192.168.1.67         printer-office                     Online
192.168.1.104        iPhone                             Online
192.168.1.128        nas-server                         Online
192.168.1.200        smart-tv                           Online
══════════════════════════════════════════════════════════════
Scan completed by Fourat Beji Network Scanner Pro
══════════════════════════════════════════════════════════════
```

## 🛠️ How It Works

1. **Network Discovery**: The scanner pings all IP addresses in the specified range (x.x.x.1 to x.x.x.254)
2. **Multi-threading**: Uses concurrent threads for fast scanning (50 threads simultaneously)
3. **Hostname Resolution**: Attempts to resolve IP addresses to friendly device names
4. **Real-time Feedback**: Displays progress and found devices during scanning
5. **Professional Reporting**: Presents results in an organized, easy-to-read format

## 📋 Prerequisites

- Python 3.6 or higher
- Network connectivity
- Appropriate permissions to run ping commands

## 🐛 Troubleshooting

### Permission Issues:
```bash
# On Linux/Mac, you might need to run with sudo
sudo python scanner.py
```

### No Devices Found:
- Check your network connection
- Verify the network prefix matches your actual network
- Ensure devices are powered on and connected

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Fourat Beji** - Network Security Enthusiast & Python Developer

- GitHub: [@Fourat4AT](https://github.com/Fourat4AT)
- Project: [Network Scanner Pro](https://github.com/Fourat4AT/Network-Scanner-Pro)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/Fourat4AT/Network-Scanner-Pro/issues).

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

---

**Disclaimer**: Use this tool responsibly and only on networks you own or have permission to scan. Unauthorized network scanning may violate laws or policies.
```
