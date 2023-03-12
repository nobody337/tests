import time
import secrets
import hashlib
import base58
import requests
import os
from rich.console import Console
from rich.table import Table
from rich import box
from pyfiglet import Figlet

console = Console()

def clear():
    """Clear the console."""
    os.system('clear')

def print_header():
    """Print the header."""
    f = Figlet(font='slant')
    console.print(f.renderText('Bitcoin Miner'), style='bold magenta')
    console.print("\nMade by ctx#6239", style='cyan')

def print_loading():
    """Print the loading screen."""
    console.print("\n[bold yellow]Connecting, please wait...[/bold yellow]\n")

def print_connected():
    """Print the connected screen."""
    console.print("[bold blue]\nCONNECTED SUCCESSFULLY![/bold blue]\n")

def print_connecting():
    """Print the connecting screen."""
    console.print("[bold yellow]\nTrying to connect to LocalHost...[/bold yellow]\n")

def print_mining():
    """Print the mining screen."""
    console.print("[bold blue]Starting Mining Process please be patient![/bold blue]\n")

def generate_private_key():
    """Generate a new private key."""
    while True:
        private_key = hex(secrets.randbits(256))[2:]
        if len(private_key) == 64:
            return private_key

def private_key_to_public_key(private_key):
    """Convert a private key to a public key."""
    private_key_bytes = bytes.fromhex(private_key)
    public_key_bytes = hashlib.sha256(private_key_bytes).digest()
    return public_key_bytes.hex()

def public_key_to_wallet_address(public_key):
    """Convert a public key to a wallet address."""
    public_key_bytes = bytes.fromhex(public_key)
    hash_bytes = hashlib.new('ripemd160', public_key_bytes).digest()
    return base58.b58encode_check(b'\x00' + hash_bytes).decode()

def get_wallet_balance(wallet_address):
    """Get the balance of a wallet address."""
    try:
        response = requests.get(f"https://blockchain.info/q/addressbalance/{wallet_address}")
        if response.status_code == 200:
            balance = int(response.text)
            return balance
        else:
            return None
    except:
        return None

def mine_wallet():
    """Mine a new wallet."""
    while True:
        private_key = generate_private_key()
        public_key = private_key_to_public_key(private_key)
        wallet_address = public_key_to_wallet_address(public_key)
        balance = get_wallet_balance(wallet_address)

        if balance is not None:
            console.print(f"[bold green]Balance:[/bold green] {balance} | [bold green][✅] FOUND![/bold green] {wallet_address} | [bold green]Priv:[/bold green] {private_key}")
            break
        else:
            console.print(f"[bold red]Balance:[/bold red] None | [bold red][X] Trying![/bold red] {wallet_address} | [bold red]Priv:[/bold red] {private_key}")

def main():
    """Main function."""
    print_header()
    time.sleep(1)
    clear()
    print_loading()
    time.sleep(3)
    clear()
    print_connected()
    time.sleep(1)
    clear()
    print_connecting()
    time.sleep(4)
    clear()
    print_mining()
    while True:
        mine_wallet()

while True:
  if __name__ == "__main__":
    main()
