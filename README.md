# 👻 Ghost Wallet Scanner

Ghost Wallet Scanner — это утилита на Python, которая ищет "призрачные" кошельки в Ethereum — адреса, на которых хранятся средства, но которые не проявляли активности в течение длительного времени.

## 🚀 Возможности

- Подключение к Ethereum через RPC (Infura, Alchemy и т.д.)
- Фильтрация кошельков по:
  - Балансу (например, > 0.5 ETH)
  - Длительности неактивности (например, 1 год)

## 🔧 Установка

```bash
git clone https://github.com/varyadanilkinacrypto/ghost-wallet-scanner.git
cd ghost-wallet-scanner
pip install -r requirements.txt
