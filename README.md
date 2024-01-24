# 🔺 The Bermuda Testnet 🔺

Owshen is an innovative privacy platform developed for EVM-based blockchains. Owshen's very first testnet, The Bermuda Testnet has launched! Excited to check it out? Just follow these steps!)

## Steps

1. Get yourself a GNU/Linux machine. (Ubuntu +22.04 preferred)
2. You have to get the latest Ubuntu updates using the following code
   ```bash
   sudo apt update
   sudo apt upgrade
   ```

5. Install `libfuse2`, `npm` and `snarkjs`:
    ```bash
    sudo apt install fuse libfuse2 npm -y
    sudo npm install -g snarkjs
    ```
6. Download the latest AppImage of the Owshen Wallet:
    ```bash
    wget https://github.com/OwshenNetwork/owshen/releases/download/v0.1.4/Owshen_v0.1.4_x86_64.AppImage
    ```
7. Make it executable:
   ```bash
    chmod +x Owshen_v0.1.4_x86_64.AppImage
   ```
8. If this is the first time you are creating a wallet, initialize your wallet and ***KEEP YOUR 12-WORD MNEMONIC PHRASE IN A SAFE PLACE!***
    ```bash
    ./Owshen_v0.1.4_x86_64.AppImage init
    ```
    Otherwise, if you have previously participated in our airdrop and already have a wallet, re-initialize your wallet with your old 12-mnemonic phrase via this command:
    ```bash
    ./Owshen_v0.1.4_x86_64.AppImage init --mnemonic "[YOUR 12 WORD MNEMONIC-PHRASE]"
    ```
    
    In case you have problems reinitializing your wallet, try removing the old wallet files **(THIS WILL REMOVE YOUR WALLET FILE, MAKE SURE YOU HAVE WRITTEN DOWN YOUR 12-WORD MNEMONIC PHRASE SOMEWHERE!)**:
    ```bash
    rm -rf ~/.owshen-wallet
    rm -rf ~/.owshen-wallet-cache
    ```
    And then initialize again!
   NB: You don't need to do 33-36 if you are able to initialize your wallet. 
10. Run the Owshen wallet! You should be able to see your DIVE balance in case you have successfully participated on our Bermuda airdrop!
    ```
    ./Owshen_v0.1.4_x86_64.AppImage wallet
    ```
    After running the app image on your browser, you connect your metamask wallet. you have to know that before connecting your metamask wallet, you have to add and set your wallet in the Sepolia test network, you also have to get Sepolia Eth from a Sepolia faucet. You can just easily search on Google for any faucet available. 
11. If you have problems running the wallet, let's discuss in our Discord server: https://discord.gg/owshen

 When you are having problems with seeing your whitelisted tokens on the wallet, you just have to connect your metamask wallet and refresh your webpage so as to start the GNU machine action of loading events on the blocks.... You'll then see a progress bar that will coincide with a progress bar that'll also be on your Owshen wallet on your browser. Upon completion of the progress to 100%, you'll see your 5 Dive tokens.
Follow the instructions of the form link posted on the Discord page to complete the testnet process.
Happy diving! :swimmer: 
