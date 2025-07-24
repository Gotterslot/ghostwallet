# 👻 ghostwallet-scanner

**Поиск "призрачных" криптокошельков Ethereum — кошельков с нулевым балансом, которые ранее получали средства.**

---

## 🔍 Что делает эта утилита?

- Проверяет список адресов.
- Получает историю транзакций (через Etherscan API).
- Проверяет текущий баланс.
- Находит "призрачные" кошельки — те, у которых **был входящий перевод**, но баланс теперь **нулевой**.

---

## 📦 Установка

```bash
git clone https://github.com/yourusername/ghostwallet-scanner.git
cd ghostwallet-scanner
pip install -r requirements.txt
