import random
import time
import matplotlib.pyplot as plt

# --- Configuration Initiale ---
amount = 1000
portfolio = {
    "AAPL": 0,
    "TSLA": 0,
    "BTC": 0
}
money_end = amount
transaction_cost = 0.0075


total_value_history = []

stocks = {
    "AAPL": {"price": 150.0, "history": [150.0]},
    "TSLA": {"price": 700.0, "history": [700.0]},
    "BTC": {"price": 45000.0, "history": [45000.0]}
}


# --- Fonctions ---
def buy(symbol, quantity):
    global money_end
    price = stocks[symbol]["price"]
    cost = quantity * price
    fees = cost * transaction_cost

    if money_end >= (cost + fees):
        money_end -= (cost + fees)
        portfolio[symbol] += quantity
    else:
        pass


def update_market():
    for symbol in stocks:
        volatility = 0.02
        change = stocks[symbol]["price"] * random.uniform(-volatility, volatility)
        stocks[symbol]["price"] += change
        stocks[symbol]["history"].append(stocks[symbol]["price"])


def calculate_net_worth():
    current_assets_value = 0
    for symbol in stocks:
        current_assets_value += portfolio[symbol] * stocks[symbol]["price"]
    return money_end + current_assets_value


# --- Moteur de Simulation ---
plt.ion()
fig, ax = plt.subplots()

buy("AAPL", 2)
buy("BTC", 0.01)

print("Simulation lancée... Fermez la fenêtre du graphique pour arrêter.")

for i in range(100):
    update_market()

    # Calcul et stockage de la richesse
    net_worth = calculate_net_worth()
    total_value_history.append(net_worth)

    # Mise à jour visuelle
    ax.clear()
    ax.plot(total_value_history, label="Net Worth ($)", color='blue')
    ax.set_title(f"Temps: {i} | Richesse: {net_worth:.2f}")
    ax.legend()
    ax.grid(True)

    plt.pause(0.1)  # Ralentissement pour l'effet visuel

plt.ioff()
plt.show()