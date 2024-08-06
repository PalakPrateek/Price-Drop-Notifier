# Price Drop Notifier
This project tracks the price of Grand Theft Auto V on Steam and sends an email when the price drops below a specified threshold. This is useful for gamers looking to buy the game at a discounted price.

## Getting Started
### Prerequisites
* Python 3.x
* An email account (Gmail recommended for simplicity)
* Python packages: requests, beautifulsoup4, python-dotenv

### Installation

1. Clone the repository.

```bash
git clone https://github.com/PalakPrateek/Price-Drop-Notifier.git
cd Price-Drop-Notifier
```
2. Install required packages.

```bash
pip install requests
pip install beautifulsoup4
pip install python-dotenv
```
## Usage

1. Edit the TARGET_PRICE variable in main.py to set your desired price threshold for notifications.

2. Set up environment variables.

```
EMAIL_ADDRESS_FROM=your_email@gmail.com
EMAIL_PASSWORD=your_password
EMAIL_ADDRESS_TO=recipient_email@gmail.com
```
3. Run the script.

```bash
python main.py
```
## Screenshots
![image](https://github.com/user-attachments/assets/962d3de4-947a-43da-ba16-dce62d03b42c)


