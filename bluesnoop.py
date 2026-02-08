import asyncio
import time
import json
import csv
from datetime import datetime
from bleak import BleakScanner
from rich.console import Console
from rich.table import Table
from rich.live import Live

# Import from your menu module
from menu import display_banner, show_about_screen, print_menu_options, get_snoop_time, show_history_menu

console = Console()

FOUND_DEVICES = {}

def detect_call(device, ad_data):

    uid = device.address
    name = ad_data.local_name or device.name or "Unknown"
    rssi = ad_data.rssi
    current_ts = datetime.now().strftime("%H:%M:%S")

    if uid not in FOUND_DEVICES:
        FOUND_DEVICES[uid] = {
            "name": name,
            "first_seen": current_ts,
            "last_seen": current_ts,
            "rssi": rssi,
            "sighting_count": 1
        }
    else:
        FOUND_DEVICES[uid]["last_seen"] = current_ts
        FOUND_DEVICES[uid]["sighting_count"] += 1
        FOUND_DEVICES[uid]["rssi"] = rssi
        
        if FOUND_DEVICES[uid]['name'] == "Unknown" and name != "Unknown":
            FOUND_DEVICES[uid]['name'] = name

def export_data(session_data):
    """Handles exporting the tracked devices including GPS data."""
    if not session_data:
        console.print("[yellow]No data to export.[/yellow]")
        return

    console.print("\n[bold cyan]Export Results[/bold cyan]")
    console.print("1. JSON | 2. CSV | 3. Skip")
    choice = console.input("Select format: ").strip()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if choice == "1":
        filename = f"snoop_report_{timestamp}.json"
        with open(filename, "w") as f:
            json.dump(session_data, f, indent=4)
        console.print(f"[green]Saved to {filename}[/green]")
    elif choice == "2":
        filename = f"snoop_report_{timestamp}.csv"
        keys = ["uuid", "name", "first_seen", "last_seen", "rssi", "sighting_count"]
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            for uuid, data in session_data.items():
                row = {"uuid": uuid, **data}
                writer.writerow(row)
        console.print(f"[green]Saved to {filename}[/green]")
    else:
        console.print("[yellow]Export skipped.[/yellow]")

async def run_scanner(duration=None):
    start_time = time.time()
    scanner = BleakScanner(detect_call)
 
    title = "\n🦉 BLUESNOOP | LIMITLESS (Ctrl+C to stop)"

    try:
        with Live(refresh_per_second=1, screen=True) as live:
            await scanner.start()
            while True:
                if duration:
                    elapsed = time.time() - start_time
                    title = f"\n🦉 BLUESNOOP | TIMED: {int(duration - elapsed)}s left"
                    if elapsed >= duration:
                        break
    
                table = Table(title=title, border_style="bright_black")
                table.add_column("Identifier", style="magenta")
                table.add_column("Name", style="green")
                table.add_column("RSSI", style="magenta")
                table.add_column("Sightings", justify="center")
                table.add_column("First Seen", style="cyan")
                table.add_column("Last Seen", style="cyan")

                for uid, info in FOUND_DEVICES.items():
                    table.add_row(
                        uid,
                        info['name'],
                        str(info['rssi']),
                        str(info["sighting_count"]),
                        info['first_seen'],
                        info['last_seen']
                    )
                live.update(table)
                await asyncio.sleep(0.5)

    except (asyncio.CancelledError, KeyboardInterrupt):
        await scanner.stop()
        console.print("\n[bold yellow]![/bold yellow] Interrupted. Closing scanner and saving intelligence...")

    console.print(f"\n[bold green]✔[/bold green] Intelligence retained. {len(FOUND_DEVICES)} targets in memory.")
    # Trigger export automatically or wait for menu return
    export_data(FOUND_DEVICES)
    time.sleep(1)

async def main():
    while True:
        console.clear()
        display_banner()
        print_menu_options()
        try:
            choice = console.input("\n[bold cyan]Select Option > [/bold cyan]")

            if choice == "1":
                t = get_snoop_time()
                await run_scanner(duration=t)
            elif choice == "2":
                await run_scanner(duration=None)
            elif choice == "3":
                show_history_menu(FOUND_DEVICES)
            elif choice == "4":
                show_about_screen()
            elif choice == "5":
                break
        
        except (EOFError):
            break



if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("[bold yellow]! Interrupted[/bold yellow]")
