import os
import sys
import time
import json
import socket
import requests
import webbrowser
import subprocess
from datetime import datetime

# ─── Auto-install dependencies ───────────────────────────────────────────────
# Works on Linux, Termux, Windows
_IS_TERMUX = os.path.exists("/data/data/com.termux")
_PIP_FLAGS  = "" if _IS_TERMUX else "--break-system-packages -q"

for pkg in ["rich", "requests"]:
    try:
        __import__(pkg)
    except ImportError:
        print(f"\n[!] Installing {pkg}...")
        os.system(f"pip install {pkg} {_PIP_FLAGS}")

from rich import print, pretty
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich.prompt import Prompt
from rich.rule import Rule
from rich import box

pretty.install()
console = Console()

# ─── Developer Info ───────────────────────────────────────────────────────────
DEV = {
    "name":    "r00td3athsh3ll01",
    "version": "3.1",
    "tool":    "GHOST-TRACK",
    "github":  "github.com/tawfique02",
    "contact": "t.me/r00td3athsh3ll01",
    "built":   "2026",
}

sys.stdout.write(f'\x1b]2;{DEV["tool"]} v{DEV["version"]} | by {DEV["name"]}\x07')

# ─── Banner ───────────────────────────────────────────────────────────────────
BANNER = r"""[bold cyan]
   ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗
  ██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝
  ██║  ███╗███████║██║   ██║███████╗   ██║   
  ██║   ██║██╔══██║██║   ██║╚════██║   ██║   
  ╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   
   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝  [/bold cyan][bold red]
  ████████╗██████╗  █████╗  ██████╗██╗  ██╗
  ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
     ██║   ██████╔╝███████║██║     █████╔╝ 
     ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ 
     ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝[/bold red]
"""

def header():
    print(BANNER)
    credits = (
        f"  [dim]Tool[/dim] [bold white]{DEV['tool']} v{DEV['version']}[/bold white]  "
        f"[dim]|[/dim]  [dim]Dev[/dim] [bold yellow]{DEV['name']}[/bold yellow]  "
        f"[dim]|[/dim]  [dim]TG[/dim] [bold cyan]{DEV['contact']}[/bold cyan]  "
        f"[dim]|[/dim]  [dim]GH[/dim] [bold green]{DEV['github']}[/bold green]"
    )
    console.print(credits)
    console.print(Rule(style="dim red"))
    print()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def spin(msg="Loading", secs=1.0):
    with Progress(
        SpinnerColumn(spinner_name="dots2", style="bold red"),
        TextColumn(f"[bold cyan]{msg}[/bold cyan]"),
        BarColumn(bar_width=28, style="red", complete_style="cyan"),
        transient=True,
    ) as p:
        t = p.add_task("", total=40)
        for _ in range(40):
            time.sleep(secs / 40)
            p.advance(t)

def safe_get(data, *keys, fallback="N/A"):
    try:
        for k in keys:
            data = data[k]
        return data if data is not None else fallback
    except (KeyError, TypeError):
        return fallback

# ─── Network ──────────────────────────────────────────────────────────────────
def get_my_ip():
    try:
        r = requests.get("https://api.ipify.org?format=json", timeout=8)
        return r.json().get("ip", "Unknown")
    except Exception:
        return "Unknown"

def resolve_hostname(target):
    target = target.strip().lower()
    for pfx in ("https://", "http://"):
        if target.startswith(pfx):
            target = target[len(pfx):]
    target = target.split("/")[0]
    try:
        ip = socket.gethostbyname(target)
        if ip != target:
            console.print(f"  [dim]Resolved[/dim] [cyan]{target}[/cyan] [dim]→[/dim] [green]{ip}[/green]")
        return ip
    except socket.gaierror:
        return target

def fetch_ip_data(ip):
    z, ip_data = {}, {}
    try:
        r1 = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719", timeout=10)
        r1.raise_for_status()
        z = r1.json()
    except requests.RequestException as e:
        console.print(f"  [bold red]✗ ip-api.com:[/bold red] {e}")
    try:
        r2 = requests.get(f"http://ipwho.is/{ip}", timeout=10)
        r2.raise_for_status()
        ip_data = r2.json()
    except requests.RequestException as e:
        console.print(f"  [bold red]✗ ipwho.is:[/bold red] {e}")
    return z, ip_data

# ─── Display ──────────────────────────────────────────────────────────────────
def result_table(ip, z, ip_data):
    is_proxy   = str(safe_get(z, "proxy"))
    is_hosting = str(safe_get(z, "hosting"))
    is_mobile  = str(safe_get(z, "mobile"))

    def flag(val):
        return f"[bold red]⚠  {val}[/bold red]" if val.lower() == "true" else f"[dim green]{val}[/dim green]"

    t = Table(
        title=f"[bold white]◉ IP INTELLIGENCE REPORT[/bold white]  [dim]{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}[/dim]",
        box=box.DOUBLE_EDGE, border_style="bold cyan",
        header_style="bold yellow on grey19",
        show_lines=True, min_width=62,
    )
    t.add_column("  FIELD", style="bold cyan", width=22, no_wrap=True)
    t.add_column("VALUE",   style="bold white")

    sections = [
        ("── IDENTITY ──",      None),
        ("TARGET IP",           f"[bold yellow]{ip}[/bold yellow]"),
        ("IP TYPE",             safe_get(ip_data, "type")),
        ("IS PROXY / VPN",      flag(is_proxy)),
        ("IS HOSTING / DC",     flag(is_hosting)),
        ("IS MOBILE",           is_mobile),
        ("── LOCATION ──",      None),
        ("COUNTRY",             z.get("country", "N/A")),
        ("COUNTRY CODE",        z.get("countryCode", "N/A")),
        ("REGION",              z.get("regionName", "N/A")),
        ("CITY",                z.get("city", "N/A")),
        ("ZIP / POSTAL",        f"{z.get('zip','N/A')} / {safe_get(ip_data,'postal')}"),
        ("LATITUDE",            str(z.get("lat", "N/A"))),
        ("LONGITUDE",           str(z.get("lon", "N/A"))),
        ("CAPITAL",             safe_get(ip_data, "capital")),
        ("BORDERS",             safe_get(ip_data, "borders")),
        ("── TIME & LOCALE ──", None),
        ("TIMEZONE",            z.get("timezone", "N/A")),
        ("UTC OFFSET",          str(safe_get(ip_data, "timezone", "utc"))),
        ("CALLING CODE",        str(safe_get(ip_data, "calling_code"))),
        ("CURRENCY",            f"{safe_get(ip_data,'currency','name')} ({safe_get(ip_data,'currency','code')})"),
        ("LANGUAGES",           safe_get(ip_data, "languages")),
        ("── NETWORK ──",       None),
        ("ISP",                 z.get("isp", "N/A")),
        ("ORG",                 z.get("org", "N/A")),
        ("AS",                  z.get("as",  "N/A")),
        ("ASN",                 str(safe_get(ip_data, "connection", "asn"))),
        ("DOMAIN",              safe_get(ip_data, "connection", "domain")),
    ]

    for field, val in sections:
        if val is None:
            t.add_row(f"[bold magenta]{field}[/bold magenta]", "")
        else:
            t.add_row(f"  {field}", str(val))

    console.print(t)

def sub_menu(ip, z, ip_data):
    m = Table(box=box.SIMPLE, show_header=False, border_style="dim", min_width=44, padding=(0,1))
    m.add_column(style="bold red",   width=5)
    m.add_column(style="bold white", width=24)
    m.add_column(style="dim cyan",   width=18)
    m.add_row("[1]", "Open Google Maps",   "View on map")
    m.add_row("[2]", "Ping",               "Check latency")
    m.add_row("[3]", "Traceroute",         "Network path")
    m.add_row("[4]", "Port Scan",          "Common ports")
    m.add_row("[5]", "Save JSON Report",   "Export to file")
    m.add_row("[0]", "Back to Main Menu",  "")
    console.print(Panel(m, title="[bold yellow]⚙  ACTIONS[/bold yellow]", border_style="cyan", padding=(0,1)))

    while True:
        ch = input("\n  [ACTION] → ").strip()
        if   ch == "1": open_map(z)
        elif ch == "2": ping_ip(ip)
        elif ch == "3": traceroute_ip(ip)
        elif ch == "4": port_scan(ip)
        elif ch == "5": save_report(ip, z, ip_data)
        elif ch == "0": break
        else: console.print("  [bold red]✗  Invalid. Enter 0-5.[/bold red]")

# ─── Features ─────────────────────────────────────────────────────────────────
def open_map(z):
    lat, lon = z.get("lat"), z.get("lon")
    if lat and lon:
        url = f"https://maps.google.com/?q={lat},{lon}"
        webbrowser.open(url)
        console.print(f"  [bold green]✓  Opened:[/bold green] [cyan]{url}[/cyan]")
    else:
        console.print("  [bold yellow]⚠  Coordinates unavailable.[/bold yellow]")

def ping_ip(ip):
    console.print(f"\n  [bold cyan]Pinging [yellow]{ip}[/yellow]...[/bold cyan]\n")
    p = "-n" if os.name == "nt" else "-c"
    res = subprocess.run(["ping", p, "4", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    console.print(res.stdout or res.stderr)

def traceroute_ip(ip):
    console.print(f"\n  [bold cyan]Traceroute → [yellow]{ip}[/yellow][/bold cyan]\n")
    cmd = ["tracert", ip] if os.name == "nt" else ["traceroute", "-m", "15", ip]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=40)
        console.print(res.stdout or res.stderr)
    except FileNotFoundError:
        console.print("  [bold red]✗  traceroute not installed.[/bold red]  [dim]sudo apt install traceroute[/dim]")
    except subprocess.TimeoutExpired:
        console.print("  [bold yellow]⚠  Timed out.[/bold yellow]")

def port_scan(ip):
    ports = {
        21:"FTP", 22:"SSH", 23:"Telnet", 25:"SMTP", 53:"DNS",
        80:"HTTP", 110:"POP3", 143:"IMAP", 443:"HTTPS", 445:"SMB",
        3306:"MySQL", 3389:"RDP", 5900:"VNC", 8080:"HTTP-Alt", 27017:"MongoDB"
    }
    t = Table(
        title=f"[bold cyan]PORT SCAN — {ip}[/bold cyan]",
        box=box.SIMPLE_HEAVY, border_style="red", header_style="bold yellow"
    )
    t.add_column("PORT",    style="cyan",  width=8)
    t.add_column("SERVICE", style="white", width=14)
    t.add_column("STATUS",  style="bold",  width=12)

    console.print(f"\n  [bold cyan]Scanning {len(ports)} ports on [yellow]{ip}[/yellow]...[/bold cyan]\n")
    open_count = 0
    for port, svc in ports.items():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.8)
            r = s.connect_ex((ip, port))
            s.close()
            if r == 0:
                status = "[bold green]● OPEN[/bold green]"
                open_count += 1
            else:
                status = "[dim]○ CLOSED[/dim]"
        except Exception:
            status = "[dim red]ERROR[/dim red]"
        t.add_row(str(port), svc, status)

    console.print(t)
    console.print(f"  [bold yellow]Result:[/bold yellow] [green]{open_count} open[/green] / [dim]{len(ports)-open_count} closed[/dim]  out of {len(ports)} ports.\n")

def save_report(ip, z, ip_data):
    fname = f"ghost_report_{ip.replace('.','_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    data = {
        "tool":       DEV["tool"],
        "version":    DEV["version"],
        "developer":  DEV["name"],
        "github":     DEV["github"],
        "contact":    DEV["contact"],
        "generated":  datetime.now().isoformat(),
        "target_ip":  ip,
        "ip_api_data": z,
        "ipwho_data":  ip_data,
    }
    with open(fname, "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    console.print(f"  [bold green]✓  Saved →[/bold green] [cyan]{fname}[/cyan]")

def bulk_scan():
    console.print(Panel(
        "[dim]Enter multiple IPs or domains — comma or space separated.\n"
        "Example: [cyan]8.8.8.8, 1.1.1.1, google.com[/cyan][/dim]",
        title="[bold yellow]BULK SCAN[/bold yellow]", border_style="cyan"
    ))
    raw = input("\n  Targets → ").strip()
    targets = [x.strip() for x in raw.replace(",", " ").split() if x.strip()]
    if not targets:
        console.print("  [bold red]✗  No targets entered.[/bold red]")
        return
    console.print(f"\n  [dim]Scanning [bold]{len(targets)}[/bold] target(s)...[/dim]\n")
    found = fail = 0
    for target in targets:
        console.print(Rule(f"[dim cyan]{target}[/dim cyan]", style="dim"))
        ip = resolve_hostname(target)
        spin(f"Fetching {ip}", secs=0.6)
        z, ip_data = fetch_ip_data(ip)
        if z.get("status") == "success":
            result_table(ip, z, ip_data)
            found += 1
        else:
            console.print(f"  [bold red]✗  {ip} — NOT FOUND or PRIVATE IP[/bold red]")
            fail += 1
        print()
    console.print(Rule(style="dim"))
    console.print(f"  [bold]Done.[/bold]  [green]{found} success[/green]  [red]{fail} failed[/red]  ({len(targets)} total)\n")

# ─── About ────────────────────────────────────────────────────────────────────
def show_about():
    clear(); header()

    dev_t = Table(box=box.ROUNDED, border_style="cyan", show_header=False, min_width=52)
    dev_t.add_column(style="bold yellow", width=16)
    dev_t.add_column(style="bold white")
    dev_t.add_row("Tool",      f"{DEV['tool']} v{DEV['version']}")
    dev_t.add_row("Developer", DEV["name"])
    dev_t.add_row("Telegram",  DEV["contact"])
    dev_t.add_row("GitHub",    DEV["github"])
    dev_t.add_row("Built",     DEV["built"])
    dev_t.add_row("Language",  "Python 3 + Rich")
    dev_t.add_row("APIs",      "ip-api.com  |  ipwho.is  |  ipify.org")
    console.print(Panel(dev_t, title="[bold red]◈ DEVELOPER INFO ◈[/bold red]", border_style="bold red"))

    feat = Table(box=box.SIMPLE_HEAVY, border_style="dim", header_style="bold yellow", min_width=52)
    feat.add_column("FEATURE",     style="bold cyan", width=22)
    feat.add_column("DESCRIPTION", style="white")
    for f, d in [
        ("IP / Domain Lookup",  "Full geo + ISP + security info"),
        ("My Public IP",        "Your own IP full report"),
        ("Bulk Scan",           "Scan many IPs / domains at once"),
        ("Port Scanner",        "Check 15 common open ports"),
        ("Ping",                "Test latency to any target"),
        ("Traceroute",          "Network hop-by-hop path"),
        ("Google Maps",         "Open target location on map"),
        ("Save JSON Report",    "Export full result to file"),
        ("Domain Resolve",      "Works with URLs & domains"),
        ("Proxy / VPN Flag",    "Detect VPN / proxy / hosting IPs"),
    ]:
        feat.add_row(f, d)
    console.print(Panel(feat, title="[bold yellow]◈ FEATURES[/bold yellow]", border_style="yellow"))

    input("  [ENTER] Back to Menu...")

# ─── Screens ──────────────────────────────────────────────────────────────────
def screen_lookup():
    clear(); header()
    console.print(Panel(
        "[dim]Enter an [bold]IP address[/bold] like [cyan]8.8.8.8[/cyan]  "
        "or a [bold]domain[/bold] like [cyan]google.com[/cyan] — it auto-resolves.[/dim]",
        title="[bold yellow]IP / DOMAIN LOOKUP[/bold yellow]", border_style="cyan", padding=(0,2)
    ))
    ip_input = Prompt.ask("\n  [bold cyan]Target IP or Domain[/bold cyan]").strip()
    if not ip_input:
        console.print("  [bold red]✗  Nothing entered.[/bold red]")
        input("  [ENTER]..."); main(); return

    ip = resolve_hostname(ip_input)
    spin("Fetching intelligence", secs=1.2)
    clear(); header()
    z, ip_data = fetch_ip_data(ip)

    if z.get("status") == "success":
        result_table(ip, z, ip_data)
        print()
        sub_menu(ip, z, ip_data)
    else:
        console.print(Panel(
            f"[bold red]✗  No data for:[/bold red] [cyan]{ip}[/cyan]\n\n"
            "[dim]Possible reasons:\n"
            "  • Private/local IP  (e.g. 192.168.x.x, 10.x.x.x)\n"
            "  • Invalid IP or domain\n"
            "  • No internet connection[/dim]",
            title="[bold red]NOT FOUND[/bold red]", border_style="red"
        ))

    input("\n  [ENTER] Back to Menu...")
    main()

def screen_myip():
    clear(); header()
    spin("Detecting your public IP", secs=1.0)
    ip = get_my_ip()
    if ip == "Unknown":
        console.print("  [bold red]✗  Could not detect IP. Check internet.[/bold red]")
        input("  [ENTER]..."); main(); return
    console.print(f"\n  [dim]Your public IP →[/dim] [bold yellow]{ip}[/bold yellow]\n")
    z, ip_data = fetch_ip_data(ip)
    if z.get("status") == "success":
        result_table(ip, z, ip_data)
        print()
        sub_menu(ip, z, ip_data)
    input("\n  [ENTER] Back to Menu...")
    main()

def screen_bulk():
    clear(); header()
    bulk_scan()
    input("  [ENTER] Back to Menu...")
    main()

# ─── Main Menu ────────────────────────────────────────────────────────────────
def main():
    clear(); header()

    m = Table(box=box.SIMPLE_HEAVY, show_header=False, border_style="dim red", min_width=48, padding=(0,1))
    m.add_column(style="bold red",   width=5)
    m.add_column(style="bold white", width=26)
    m.add_column(style="dim cyan",   width=18)
    m.add_row("[1]", "IP / Domain Lookup",   "Track any target")
    m.add_row("[2]", "My Public IP",         "Your IP info")
    m.add_row("[3]", "Bulk Scan",            "Multiple IPs")
    m.add_row("[4]", "About & Help",         "Dev + features")
    m.add_row("[0]", "Exit",                 "")

    console.print(Panel(
        m,
        title=f"[bold yellow]◈ {DEV['tool']} v{DEV['version']} — MAIN MENU ◈[/bold yellow]",
        subtitle=f"[dim]by {DEV['name']}  |  {DEV['contact']}[/dim]",
        border_style="bold red",
        padding=(0,1),
    ))
    print()

    ch = input("  SELECT → ").strip()
    if   ch == "1": screen_lookup()
    elif ch == "2": screen_myip()
    elif ch == "3": screen_bulk()
    elif ch == "4": show_about(); main()
    elif ch == "0":
        console.print(f"\n  [bold red]Exiting {DEV['tool']}...[/bold red]  [dim]— {DEV['name']}[/dim]\n")
        sys.exit(0)
    else:
        console.print("  [bold red]✗  Invalid. Enter 0–4.[/bold red]")
        time.sleep(0.7)
        main()

main()
