# 🔺 The Bermuda Testnet 🔺

Owshen is an innovative privacy platform developed for EVM-based blockchains. Owshen's very first testnet, The Bermuda Testnet has launched! Excited to check it out? Just follow these steps!)

## Steps

1. Get yourself a GNU/Linux machine. (Ubuntu +22.04 preferred)
2. Install `libfuse2`, `nodejs` and `snarkjs`:
    ```bash
    sudo add-apt-repository universe
    sudo apt install fuse libfuse2 nodejs -y
    sudo npm install -g snarkjs
    ```
3. Download the latest AppImage of the Owshen Wallet:
    ```bash
    wget https://github.com/OwshenNetwork/owshen/releases/download/v0.1.3/Owshen_v0.1.3_x86_64.AppImage
    ```
4. Make it executable:
   ```bash
    chmod +x Owshen_v0.1.3_x86_64.AppImage
   ```
5. If this is the first time you are creating a wallet, initialize your wallet and ***KEEP YOUR 12-WORD MNEMONIC PHRASE IN A SAFE PLACE!***
    ```bash
    ./Owshen_v0.1.3_x86_64.AppImage init
    ```
    Otherwise, if you have previously participated in our airdrop and already have a wallet, re-initialize your wallet with your old 12-mnemonic phrase via this command:
    ```bash
    ./Owshen_v0.1.3_x86_64.AppImage init --mnemonic "[YOUR 12 WORD MNEMONIC-PHRASE]"
    ```
    In case you have problems reinitializing your wallet, try removing the old wallet files **(THIS WILL REMOVE YOUR WALLET FILE, MAKE SURE YOU HAVE WRITTEN DOWN YOUR 12-WORD MNEMONIC PHRASE SOMEWHERE!)**:
    ```bash
    rm -rf ~/.owshen-wallet
    rm -rf ~/.owshen-wallet-cache
    ```
    And then initialize again!
6. Run the Owshen wallet! You should be able to see your DIVE balance in case you have successfully participated on our Bermuda airdrop!
    ```
    ./Owshen_v0.1.3_x86_64.AppImage wallet
    ```
7. if you've forgotten to save your mnemonic but have the entropy file, you can convert your entropy to a mnemonic
    ```
    cd convert
    pip install -r requirements.txt
    python convert_entropy_to_mnemonic.py --entropy-json /path/to/your/.owshen-wallet.json
    ```
8. If you have problems running the wallet, let's discuss in our Discord server: https://discord.gg/owshen

 
Happy diving! :swimmer: 
