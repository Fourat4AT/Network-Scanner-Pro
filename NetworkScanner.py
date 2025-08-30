import os
import threading
import sys
import time
import socket
from datetime import datetime

class ProfessionalNetworkScanner:
    def __init__(self):
        self.active_devices = []
        self.scan_start_time = None
        self.scan_complete = False
        self.lock = threading.Lock()
        self.total_ips_scanned = 0
    
    def print_logo(self):
        logo = r"""
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
        """
        print("\033[1;36m" + logo + "\033[0m")
        print("\033[1;35m" + " " * 20 + "NETWORK DISCOVERY SUITE" + "\033[0m")
        print("\033[1;33m" + " " * 18 + "Enterprise-Grade Scanning Technology" + "\033[0m")
        print("\033[1;34m" + " " * 23 + "Developed by: Fourat Beji" + "\033[0m")
        print("\033[1;90m" + "─" * 70 + "\033[0m")
    
    def get_hostname(self, ip):
        """Attempt to resolve IP to hostname for more informative results"""
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except (socket.herror, socket.gaierror):
            return "Unknown"
        except:
            return "Unresolved"
    
    def ping(self, ip):
        try:
            if os.name == "posix":
                response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
            else:
                response = os.system(f"ping -n 1 -w 1000 {ip} > nul 2>&1")
            
            if response == 0:
                hostname = self.get_hostname(ip)
                with self.lock:
                    self.active_devices.append((ip, hostname))
                return True
        except:
            pass
        return False
    
    def progress_bar(self, completed, total, length=40):
        """Display a professional progress bar"""
        percent = completed / total
        filled_length = int(length * percent)
        bar = "█" * filled_length + "░" * (length - filled_length)
        return f"[{bar}] {percent:.1%}"
    
    def spinning_cursor(self):
        """Professional status display with progress bar"""
        total_ips = 254
        while not self.scan_complete:
            for cursor in '⣾⣽⣻⢿⡿⣟⣯⣷':
                with self.lock:
                    completed = self.total_ips_scanned
                progress = self.progress_bar(completed, total_ips)
                sys.stdout.write(f'\r\033[1;34m{cursor} Scanning: {progress} | Devices: {len(self.active_devices)}\033[0m')
                sys.stdout.flush()
                time.sleep(0.1)
                if self.scan_complete:
                    break
    
    def display_results_table(self):
        """Display results in a professional table format"""
        print("\n\033[1;35m" + "═" * 70 + "\033[0m")
        print("\033[1;32mSCAN RESULTS SUMMARY\033[0m")
        print("\033[1;35m" + "═" * 70 + "\033[0m")
        
        print(f"\033[1;36mScan Date:\033[0m {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\033[1;36mScan Duration:\033[0m {time.time() - self.scan_start_time:.2f} seconds")
        print(f"\033[1;36mIPs Scanned:\033[0m 254")
        print(f"\033[1;36mActive Devices Found:\033[0m {len(self.active_devices)}")
        print("\033[1;35m" + "─" * 70 + "\033[0m")
        
        if self.active_devices:
            print("\n\033[1;33mACTIVE DEVICES:\033[0m")
            print("\033[1;34mIP Address\033[0m".ljust(20) + "\033[1;34mHostname\033[0m".ljust(35) + "\033[1;34mStatus\033[0m")
            print("\033[1;90m" + "─" * 70 + "\033[0m")
            
            for ip, hostname in sorted(self.active_devices):
                status = "\033[1;32mOnline\033[0m"
                print(f"\033[1;37m{ip.ljust(20)}{hostname.ljust(35)}{status}\033[0m")
        else:
            print("\n\033[1;31mNo active devices detected on the network.\033[0m")
        
        print("\033[1;35m" + "═" * 70 + "\033[0m")
        print("\033[1;90mScan completed by Fourat Beji Network Scanner Pro\033[0m")
        print("\033[1;35m" + "═" * 70 + "\033[0m")
    
    def network_discover(self):
        self.print_logo()
        print("\033[1;32m[+] Initializing network discovery protocol...\033[0m\n")
        
        try:
            base_ip = sys.argv[1].strip()
            if base_ip.endswith('.'):
                base_ip = base_ip[:-1]
        except IndexError:
            base_ip = "192.168.1"
        
        print(f"\033[1;36mTarget Network:\033[0m {base_ip}.0/24")
        print(f"\033[1;36mScan Started:\033[0m {datetime.now().strftime('%H:%M:%S')}")
        print("\033[1;90m" + "─" * 70 + "\033[0m")
        
        self.scan_start_time = time.time()
        
        # Start status thread
        spinner_thread = threading.Thread(target=self.spinning_cursor)
        spinner_thread.daemon = True
        spinner_thread.start()
        
        # Scan IPs with thread pooling
        threads = []
        max_threads = 50  # More conservative for stability
        semaphore = threading.Semaphore(max_threads)
        
        def scan_ip(ip):
            with semaphore:
                self.ping(ip)
                with self.lock:
                    self.total_ips_scanned += 1
        
        print("\033[1;33m[+] Deploying scanning threads...\033[0m")
        for i in range(1, 255):
            ip = f"{base_ip}.{i}"
            thread = threading.Thread(target=scan_ip, args=(ip,))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
        
        # Mark scan as complete
        self.scan_complete = True
        time.sleep(0.3)  # Allow status display to finish
        
        # Display professional results
        self.display_results_table()

if __name__ == "__main__":
    scanner = ProfessionalNetworkScanner()
    try:
        scanner.network_discover()
    except KeyboardInterrupt:
        print("\n\033[1;31mScan interrupted by user. Exiting gracefully...\033[0m")
        sys.exit(1)
    except Exception as e:
        print(f"\n\033[1;31mUnexpected error: {e}\033[0m")
        sys.exit(1)