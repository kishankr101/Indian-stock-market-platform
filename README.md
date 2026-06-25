# Indian Stock Market Platform

> A professional, feature-rich Indian stock market web application built with Streamlit

## 🌟 Features

- 📊 **Dashboard**: Real-time market overview and portfolio summary
- 🏠 **Market**: Explore stocks, indices, and market data
- ⭐ **Watchlist**: Create and manage multiple watchlists
- 💼 **Portfolio**: Track and analyze your investments
- 📈 **Paper Trading**: Practice trading with virtual money
- 🔍 **Technical Analysis**: Advanced charting and technical indicators
- 📰 **News & Research**: Latest financial news and market insights
- 💰 **Wallet**: Manage account balance and transactions
- 👤 **Profile**: User profile management
- ⚙️ **Settings**: Customizable application preferences

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python)
- **Backend**: Python
- **Database**: PostgreSQL (SQLite for local development)
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib, Seaborn
- **Financial Data**: yfinance, pandas-ta
- **Authentication**: Passlib, JWT

## 📁 Project Structure

```
app/
├── pages/                      # Streamlit multipage navigation
│   ├── dashboard.py
│   ├── market.py
│   ├── watchlist.py
│   ├── portfolio.py
│   ├── paper_trading.py
│   ├── technical_analysis.py
│   ├── news.py
│   ├── wallet.py
│   ├── profile.py
│   └── settings.py
├── components/                 # Reusable UI components
│   ├── sidebar.py
│   ├── navbar.py
│   ├── charts.py
│   ├── tables.py
│   └── cards.py
├── services/                   # Business logic layer
│   ├── market_service.py
│   ├── portfolio_service.py
│   ├── watchlist_service.py
│   ├── news_service.py
│   └── auth_service.py
├── database/                   # Database layer
│   ├── models.py
│   ├── connection.py
│   └── migrations/
├── utils/                      # Utility functions
│   ├── constants.py
│   ├── helpers.py
│   ├── validators.py
│   └── logger.py
├── assets/                     # Static assets (images, icons)
├── config.py                   # Application configuration
├── main.py                     # Main application entry point
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
└── README.md                  # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- PostgreSQL (optional, SQLite used by default)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kishankr101/Indian-stock-market-platform.git
   cd Indian-stock-market-platform
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your configuration
   ```

5. **Create necessary directories**
   ```bash
   mkdir -p data logs assets
   ```

### Running the Application

```bash
streamlit run main.py
```

The application will be available at `http://localhost:8501`

### Running with Custom Host/Port

```bash
streamlit run main.py --server.address 0.0.0.0 --server.port 8000
```

## 📚 Development

### Code Style

- Follow PEP 8 style guide
- Use 4 spaces for indentation
- Add docstrings to all functions and classes
- Use type hints where possible

### Running Tests

```bash
pytest tests/ -v --cov=.
```

### Linting & Formatting

```bash
# Format code with Black
black .

# Check linting with Flake8
flake8 .

# Check with Pylint
pylint **/*.py
```

## 📖 Documentation

- [Configuration Guide](docs/CONFIGURATION.md)
- [API Reference](docs/API.md)
- [Database Schema](docs/DATABASE.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## 🔐 Security

- Never commit `.env` file with real credentials
- Use environment variables for sensitive data
- Always use HTTPS in production
- Implement proper authentication and authorization
- Validate all user inputs

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📧 Support

For support, email support@example.com or open an issue on GitHub.

## ⚠️ Disclaimer

This is a demo platform for educational purposes. Always consult a financial advisor before making investment decisions. Past performance is not indicative of future results.

---

**Built with ❤️ using Streamlit**
