# Coal/Iron Ore Price Analysis

## Business Problem
The challenge lies in effectively analyzing the fluctuating prices of coal and iron ore to inform strategic decision-making for stakeholders in the mining, manufacturing, and energy sectors.

## Business Objectives and Constraints
### Objective
- Maximize profitability.

### Constraints
- Minimize costs through informed decision-making based on the analysis of coal and iron ore prices.


## Data Collection
The type of data collection for the Coal Ore Dataset is secondary data collection.

## Exploratory Data Analysis
- The Coal Ore Dataset has a shape of (262, 10), indicating 262 rows and 10 columns.
- The dataset includes columns: 'Date', 'Open', 'High', 'Low', 'Close', 'Trend Supertrend (7,3)', 'MACD (12,26,9)', 'Signal MACD (12,26,9)', 'MACD (12,26,9)_hist', 'Volume'.
- Descriptive statistics for numeric columns provide insights into distribution and variability.

## Data Pre-processing
- Type casting: Convert the 'Date' column from object data type to date data type.
- Duplication handling: No duplicated records found.
- Missing value handling: No missing values found.
- Outlier treatment: Outliers in numerical columns replaced using the Winsorizer IQR method.
- Zero-variance columns: No zero-variance columns found.

## Data Visualization
- Cards presenting average prices (open, close, low, high) over the years.
- Price trends and volatility analysis using line plots and ribbon charts.
- MACD, Signal MACD, and MACD_hist trends to identify bullish and bearish signals.
- Sum of volume trends to analyze market activity and demand/supply.
- Trend Supertrend analysis for identifying upward and downward momentum.

## Challenges
- Volatility: Periods of high price fluctuations and uncertain market conditions.
- Regulatory Environment: Changes in regulatory policies related to coal ore mining, transportation, or environmental regulations.
- Technological Disruption: Advancements in renewable energy technologies and alternative energy sources.

## Future Scopes
- Continued Growth: Overall upward trends suggest a positive outlook for the coal ore market.
- Market Expansion: Potential for market expansion and attracting new investors and stakeholders.
- Opportunities for Investment: Projected growth trajectory presents opportunities for investors to capitalize on rising market trends.

## Usage
To run the analysis, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/coal-iron-ore-price-analysis.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the analysis script: `python main.py`

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).
