---

# Cryptocurrency Price Prediction Tool

This tool is designed for users interested in analyzing and predicting the future prices of cryptocurrencies based on historical data. The tool leverages machine learning to make these predictions over user-specified time periods, using past data to forecast future trends.

## How It Works

### Overview
The **Cryptocurrency Price Prediction Tool** is built in Python and performs the following main functions:

1. **Data Retrieval**: It fetches historical price data from the CryptoCompare API.
2. **Model Training**: Uses a linear regression model to analyze the past price data and understand the trend.
3. **Prediction Generation**: Based on the trained model, it forecasts prices for the specified future period.
4. **Results Output**: Exports the predictions to an Excel spreadsheet for easy reference.

### Architecture and Flow

This tool follows a straightforward, modular architecture:
   
   1. **API Data Fetching Module**: Pulls historical cryptocurrency data from the CryptoCompare API.
   2. **Data Aggregation Module**: Processes and organizes data into a usable format for machine learning.
   3. **Machine Learning Model**: Trains the linear regression model on the processed data.
   4. **Excel Report Generator**: Exports predictions to an Excel file for further analysis.

Below is a high-level flow diagram:

```
+------------------------+
| Cryptocurrency API     |
|       Server           |
+------------------------+
         | HTTP Request  
         v
+------------------------+
| Data Aggregation       |
|   & Preprocessing      |
+------------------------+
         |
         | Cleaned Data
         v
+------------------------+
|  Machine Learning      |
|   Price Predictor      |
+------------------------+
         |
         | Price Predictions
         v
+------------------------+
|  Excel Report Export   |
+------------------------+
```

## Technical Components

The tool relies on the following libraries:
- **Requests**: Handles API requests to the CryptoCompare API for retrieving historical data.
- **Scikit-learn**: Provides the machine learning algorithm (linear regression) used to analyze and predict cryptocurrency prices.
- **OpenPyXL**: Creates Excel spreadsheets to store the predictions.
- **Colorama**: Adds colored console outputs, making the tool’s feedback more user-friendly.

## Setup and Usage

To set up the tool, follow these steps:

1. **Install dependencies**: Use the command `pip install requests openpyxl scikit-learn colorama` to install the required libraries.
2. **Run the tool**: Use `python main.py` to start the application.

## Workflow

1. **User Input**: The program begins by prompting the user to select a cryptocurrency and specify a time period for analysis (e.g., daily, weekly).
   
2. **Data Fetching**: Once a cryptocurrency and time period are chosen, the tool uses the CryptoCompare API to retrieve historical price data.

   - **API Endpoint**: The tool uses `https://min-api.cryptocompare.com/data/v2/histohour`.
   - **Parameters**: API parameters are dynamically set based on the user-selected cryptocurrency and time period to gather relevant data.

3. **Model Training**: With the historical price data, the tool utilizes **Scikit-learn** to train a linear regression model. The model uses the data to recognize price patterns over time.

4. **Price Prediction**: The trained model forecasts the cryptocurrency’s price for each unit of time within the specified future period.

5. **Output to Excel**: The predictions are saved in an Excel file in the `reports` folder. The file name includes the cryptocurrency, selected period, and timestamp.

6. **Console Output with Color**: For better readability, the tool displays green-colored success messages and red-colored error messages using **Colorama**.

## Example Output

The Excel report saved in the `reports` folder includes columns like:
- **Date**: Each predicted date for the selected period.
- **Predicted Price**: The forecasted price for each date.

**Example Filename**: The report filename follows the format `<Crypto>_<Period>_<Date>.xlsx`, e.g., `Bitcoin_7days_2024-01-01.xlsx`.

This comprehensive setup allows for efficient cryptocurrency price prediction, making it a valuable tool for those interested in market trend analysis.

--- 

This approach should capture the essential features of the tool while giving clear, structured explanations. Let me know if further adjustments are needed!