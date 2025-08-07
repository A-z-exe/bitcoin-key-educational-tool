import requests
import time
import json
import logging
from bitcoinlib.keys import Key
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def print_banner():
    """
    Prints a banner at the start of the program.
    """
    banner = f"""
    ██████╗ ████████╗ ██████╗    ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗ 
    ██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ██████╔╝   ██║   ██║         █████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
    ██╔══██╗   ██║   ██║         ██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
    ██████╔╝   ██║   ╚██████╗    ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
    ╚═════╝    ╚═╝    ╚═════╝    ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
                                                                            
    
    {Fore.YELLOW}For Educational Purposes Only{Style.RESET_ALL}
                    ╔═════════════════╗   ╔══════════════════════════════╗
                    ║AmirHosseinZarei ║   ║  Bitcoin Private Key Finder  ║ {Fore.GREEN}v1.1{Fore.CYAN}
                    ╚═════════════════╝   ╚══════════════════════════════╝
                                
                🌐 Github:  github.com/A_Z_exe
                📱 Telegram: t.me/A_Z_exe
                📷 Instagram: instagram.com/A_Z_exe
    """
    print(banner)
    print(Style.RESET_ALL)  # Reset color after banner

class BitcoinPrivateKeyFinder:
    """
    Class for finding Bitcoin private keys using real libraries.
    """
    def __init__(self):
        """
        Constructor for BitcoinPrivateKeyFinder class
        Sets up API address for retrieving Bitcoin balance.
        """
        # We'll use multiple APIs to avoid rate limits
        self.apis = [
            "https://api.blockcypher.com/v1/btc/main/addrs/",
            "https://blockchain.info/balance?active="
        ]
        self.current_api = 0  # Start with the first API
        self.error_count = 0  # Track consecutive errors for exponential backoff
        self.max_error_count = 5  # Reset after 5 successful calls
        
        # Setup logger
        logging.basicConfig(
            level=logging.INFO,
            format=f'{Fore.CYAN}%(asctime)s - %(levelname)s - %(message)s{Style.RESET_ALL}',
            handlers=[
                logging.FileHandler("bitcoin_finder.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger("BitcoinFinder")
        
    def _switch_api(self):
        """
        Switch to the next API in the list with exponential backoff for error handling.
        
        Returns:
        - str: The URL of the new API
        """
        self.current_api = (self.current_api + 1) % len(self.apis)
        
        # Apply exponential backoff based on error count
        backoff_time = min(2 * (2 ** self.error_count), 30)  # Maximum 30 seconds delay
        
        self.logger.info(f"Switching to API: {self.apis[self.current_api]} (backoff: {backoff_time}s)")
        time.sleep(backoff_time)
        return self.apis[self.current_api]
        
    def generate_private_key_and_address(self):
        """
        Generate a real Bitcoin private key and address using bitcoinlib.
        
        Returns:
        - tuple: (private key, Bitcoin address)
        """
        try:
            # Generate new key
            key = Key()
            private_key = key.private_hex
            address = key.address()
            return private_key, address
        except Exception as e:
            self.logger.error(f"{Fore.RED}Error generating key: {e}{Style.RESET_ALL}")
            # Wait before retrying
            time.sleep(1)
            return None, None
    
    def get_balance(self, address):
        """
        Get Bitcoin balance for an address using API with improved error handling.
        
        Parameters:
        - address: str
            Bitcoin address to check balance.
            
        Returns:
        - float: Bitcoin balance for the specified address.
        """
        max_retries = 3
        retry_count = 0
        
        while retry_count < max_retries:
            try:
                # Add delay to prevent API request limits
                time.sleep(1)
                
                current_api = self.apis[self.current_api]
                
                if "blockcypher" in current_api:
                    self.logger.debug(f"Requesting balance from Blockcypher API for {address}")
                    response = requests.get(f"{current_api}{address}/balance", timeout=10)
                    
                    # Check HTTP status first
                    if response.status_code != 200:
                        self.logger.warning(f"{Fore.YELLOW}API returned status code {response.status_code}{Style.RESET_ALL}")
                        self.error_count += 1
                        self._switch_api()
                        retry_count += 1
                        continue
                        
                    response.raise_for_status()
                    data = response.json()
                    
                    # Convert satoshi to Bitcoin
                    balance_satoshi = data.get("final_balance", 0)
                    balance_btc = balance_satoshi / 100000000  # 1 BTC = 100,000,000 satoshi
                    
                elif "blockchain.info" in current_api:
                    self.logger.debug(f"Requesting balance from Blockchain.info API for {address}")
                    response = requests.get(f"{current_api}{address}", timeout=10)
                    
                    # Check HTTP status first
                    if response.status_code != 200:
                        self.logger.warning(f"{Fore.YELLOW}API returned status code {response.status_code}{Style.RESET_ALL}")
                        self.error_count += 1
                        self._switch_api()
                        retry_count += 1
                        continue
                        
                    response.raise_for_status()
                    data = response.json()
                    
                    # blockchain.info API returns data in a different format
                    balance_satoshi = data.get(address, {}).get("final_balance", 0)
                    balance_btc = balance_satoshi / 100000000
                
                # Reset error count after successful call
                self.error_count = max(0, self.error_count - 1)
                return balance_btc
                
            except requests.exceptions.RequestException as e:
                retry_count += 1
                self.error_count += 1
                
                if retry_count < max_retries:
                    self.logger.warning(f"{Fore.YELLOW}API error (attempt {retry_count}/{max_retries}): {e}. Retrying...{Style.RESET_ALL}")
                    self._switch_api()  # Try a different API
                else:
                    self.logger.error(f"{Fore.RED}Failed to retrieve balance after {max_retries} attempts: {e}{Style.RESET_ALL}")
                    return 0
            except Exception as e:
                self.logger.error(f"{Fore.RED}Unexpected error retrieving balance: {e}{Style.RESET_ALL}")
                self.error_count += 1
                return 0
    
    def save_result(self, private_key, address, balance):
        """
        Save found keys in both JSON (structured) and text formats.
        
        Parameters:
        - private_key: str
            Bitcoin private key found
        - address: str
            Bitcoin address with balance
        - balance: float
            Balance in BTC
        """
        result = {
            "address": address,
            "private_key": private_key,
            "balance": balance,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        
        try:
            # Try to read existing JSON file
            with open("found_bitcoin_keys.json", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = {"keys": []}
        except FileNotFoundError:
            data = {"keys": []}
        
        # Add new result
        data["keys"].append(result)
        
        # Save JSON results
        with open("found_bitcoin_keys.json", "w") as f:
            json.dump(data, f, indent=2)
            
        # Also save in text format for easy reading
        with open("found_bitcoin_keys.txt", "a") as f:
            f.write(f"Address: {address}\n")
            f.write(f"Private Key: {private_key}\n")
            f.write(f"Balance: {balance} BTC\n")
            f.write(f"Timestamp: {result['timestamp']}\n")
            f.write("-" * 50 + "\n")
    
    def find_private_keys_with_balance(self, max_attempts=1000, timeout_minutes=10):
        """
        Search for private keys with positive balance.
        
        Parameters:
        - max_attempts: int
            Maximum number of attempts.
        - timeout_minutes: int
            Time limit in minutes.
            
        Returns:
        - list: List of tuples (private_key, address, balance) with positive balance.
        """
        found_keys = []
        attempts = 0
        errors = 0
        start_time = time.time()
        timeout_seconds = timeout_minutes * 60
        
        self.logger.info(f"{Fore.GREEN}Starting search for keys with balance. Time limit: {timeout_minutes} minutes{Style.RESET_ALL}")
        
        try:
            while attempts < max_attempts:
                # Check time limit
                if time.time() - start_time > timeout_seconds:
                    self.logger.info(f"{Fore.YELLOW}Time limit ({timeout_minutes} minutes) reached.{Style.RESET_ALL}")
                    break
                    
                attempts += 1
                private_key, address = self.generate_private_key_and_address()
                
                if not address:
                    errors += 1
                    if errors > 5:  # If too many errors, take a break
                        self.logger.warning(f"{Fore.YELLOW}Too many errors. Taking a 10-second break...{Style.RESET_ALL}")
                        time.sleep(10)
                        errors = 0
                    continue
                    
                self.logger.info(f"Attempt {attempts}/{max_attempts}: Checking address {Fore.CYAN}{address}{Style.RESET_ALL}")
                
                balance = self.get_balance(address)
                
                if balance > 0:
                    self.logger.info(f"{Fore.GREEN}Key with balance found! Address: {address}, Balance: {balance} BTC{Style.RESET_ALL}")
                    found_keys.append((private_key, address, balance))
                    
                    # Save to file immediately
                    self.save_result(private_key, address, balance)
                
                # Show progress every 10 attempts
                if attempts % 10 == 0:
                    elapsed_minutes = (time.time() - start_time) / 60
                    remaining_minutes = timeout_minutes - elapsed_minutes if elapsed_minutes < timeout_minutes else 0
                    
                    print(f"{Fore.CYAN}Progress: {attempts}/{max_attempts} ({attempts/max_attempts*100:.1f}%) - " 
                          f"Time elapsed: {elapsed_minutes:.2f} min - " 
                          f"Remaining: {remaining_minutes:.2f} min{Style.RESET_ALL}")
                    
                    # Take a short break every 50 attempts to avoid overwhelming APIs
                    if attempts % 50 == 0:
                        self.logger.info("Taking a short break to avoid API rate limits...")
                        time.sleep(5)
            
        except KeyboardInterrupt:
            self.logger.info(f"{Fore.YELLOW}Search stopped by user.{Style.RESET_ALL}")
        except Exception as e:
            self.logger.error(f"{Fore.RED}An error occurred during search: {e}{Style.RESET_ALL}")
        
        self.logger.info(f"{Fore.GREEN}Search completed. {len(found_keys)} keys with balance found out of {attempts} attempts.{Style.RESET_ALL}")
        return found_keys

def main():
    """
    Main program function.
    """
    try:
        print_banner()
        
        print(f"{Fore.YELLOW}⚠️ WARNING: This program is for educational purposes only.{Style.RESET_ALL}")
        print("The probability of finding a key with balance is extremely low (almost zero).")
        print("Randomly finding someone else's Bitcoin private key is unethical and illegal.")
        print("-" * 70)
        
        # Check if required libraries are installed
        try:
            import bitcoinlib
            import colorama
            import json
        except ImportError as e:
            print(f"{Fore.RED}Error: Missing required library: {e}{Style.RESET_ALL}")
            print("Please install required libraries with:")
            print(f"{Fore.GREEN}pip install bitcoinlib requests colorama{Style.RESET_ALL}")
            return
        
        # Get user input with validation
        try:
            max_attempts_input = input(f"{Fore.CYAN}Enter maximum number of attempts [default=100]: {Style.RESET_ALL}")
            max_attempts = int(max_attempts_input) if max_attempts_input.strip() else 100
            
            timeout_input = input(f"{Fore.CYAN}Enter time limit in minutes [default=5]: {Style.RESET_ALL}")
            timeout_minutes = int(timeout_input) if timeout_input.strip() else 5
            
            # Set reasonable limits
            max_attempts = min(max_attempts, 1000)  # Limit to 1000 attempts
            timeout_minutes = min(timeout_minutes, 30)  # Limit to 30 minutes
            
        except ValueError:
            print(f"{Fore.YELLOW}Invalid input. Using default values.{Style.RESET_ALL}")
            max_attempts = 100
            timeout_minutes = 5
        
        finder = BitcoinPrivateKeyFinder()
        
        # Start search
        found_keys = finder.find_private_keys_with_balance(max_attempts, timeout_minutes)
        
        # Display results
        if found_keys:
            print(f"\n{Fore.GREEN}Keys found with positive balance:{Style.RESET_ALL}")
            for private_key, address, balance in found_keys:
                print(f"{Fore.CYAN}Address: {address}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Private Key: {private_key}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Balance: {balance} BTC{Style.RESET_ALL}")
                print("-" * 50)
        else:
            print(f"\n{Fore.YELLOW}No keys with positive balance found.{Style.RESET_ALL}")
            print("This result is completely normal due to the vast space of possible private keys.")
            print(f"{Fore.CYAN}Did you know? The odds of finding a private key with balance are roughly")
            print(f"1 in 2^160, which is vastly smaller than the number of atoms in the universe!{Style.RESET_ALL}")
    
    except Exception as e:
        print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
        print("Please check that you have all required libraries installed.")
        print(f"{Fore.GREEN}pip install bitcoinlib requests colorama{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
