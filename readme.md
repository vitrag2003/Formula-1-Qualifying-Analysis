# F1 Track Dominance Analysis

This Streamlit application allows users to analyze F1 track dominance by visualizing the fastest drivers in different minisectors of a selected circuit during qualifying sessions.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/f1-track-dominance.git
    cd f1-track-dominance
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the app.

## Features

- **Year Selection**: Choose the year of the F1 season.
- **Circuit Selection**: Select from a list of F1 circuits.
- **Driver Selection**: Pick drivers who qualified for Q3.
- **Minisector Analysis**: Analyze the fastest drivers in different minisectors.
- **Dynamic Plot Customization**: Adjust line width and style for the plot.
- **Enhanced Annotations**: View detailed annotations for each driver.

## Dependencies

- [`streamlit`](command:_github.copilot.openSymbolFromReferences?%5B%22streamlit%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22d%3A%5C%5CFormula%201%5C%5CSector%5C%5Capp.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fd%253A%2FFormula%25201%2FSector%2Fapp.py%22%2C%22path%22%3A%22%2Fd%3A%2FFormula%201%2FSector%2Fapp.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%5D%5D "Go to definition")
- [`fastf1`](command:_github.copilot.openSymbolFromReferences?%5B%22fastf1%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22d%3A%5C%5CFormula%201%5C%5CSector%5C%5Capp.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fd%253A%2FFormula%25201%2FSector%2Fapp.py%22%2C%22path%22%3A%22%2Fd%3A%2FFormula%201%2FSector%2Fapp.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A1%2C%22character%22%3A7%7D%7D%5D%5D "Go to definition")
- [`numpy`](command:_github.copilot.openSymbolFromReferences?%5B%22numpy%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22d%3A%5C%5CFormula%201%5C%5CSector%5C%5Capp.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fd%253A%2FFormula%25201%2FSector%2Fapp.py%22%2C%22path%22%3A%22%2Fd%3A%2FFormula%201%2FSector%2Fapp.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A3%2C%22character%22%3A7%7D%7D%5D%5D "Go to definition")
- [`plotly`](command:_github.copilot.openSymbolFromReferences?%5B%22plotly%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22d%3A%5C%5CFormula%201%5C%5CSector%5C%5Capp.py%22%2C%22_sep%22%3A1%2C%22external%22%3A%22file%3A%2F%2F%2Fd%253A%2FFormula%25201%2FSector%2Fapp.py%22%2C%22path%22%3A%22%2Fd%3A%2FFormula%201%2FSector%2Fapp.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A7%7D%7D%5D%5D "Go to definition")

## License

This project is licensed under the MIT License. See the LICENSE file for details.