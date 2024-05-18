# Stock Prediction and Analysis

This is a Streamlit application for stock prediction and analysis. The app allows users to select a stock, view historical data, and predict future stock prices using the Prophet model.

## Features

- View historical stock data
- Predict future stock prices
- Interactive plots using Plotly
- Custom stock symbol input

## Installation

To run this application, you need to have Python 3.11.5 installed. Follow the steps below to set up and run the app.

### Clone the Repository

```bash
git clone https://github.com/punithvt/stockprediction.git
cd stockprediction
Create a Virtual Environment
Its recommended to use a virtual environment to manage dependencies.

Install Dependencies
Install the required Python packages.
pip install -r requirements.txt
If requirements.txt is not present, you can install the packages manually:

pip install streamlit plotly yfinance prophet
Run the Application

streamlit run stockPred.py
This will start the Streamlit application, and you can interact with it through your web browser.

Usage
Select a Stock: Choose a stock from the predefined list or enter a custom stock symbol.
View Historical Data: The app will display the historical data for the selected stock.
Predict Future Prices: Use the slider to select the number of years for prediction, and the app will use the Prophet model to forecast future stock prices.
Interactive Plots: View interactive plots of the stocks historical and predicted prices.

Project Structure
'stockPred.py': The main script for running the Streamlit app.
'requirements.txt': List of Python packages required to run the app.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
