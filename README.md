# 🔐 Secret Message Decoder Using Python

## 📌 Overview

This project is a Python-based **Secret Message Decoder** that retrieves a publicly accessible Google Docs document, extracts a table containing character coordinates, and reconstructs a hidden message using those coordinates.

The program uses `requests` to download the document and `pandas` to extract and process the table data. It then places each character at its corresponding `(x, y)` position in a two-dimensional grid to reveal the decoded message.

## ✨ Features

- 🌐 Fetches data from a public Google Docs URL.
- 📊 Extracts tabular data using Pandas.
- 🔍 Identifies X-coordinate, Y-coordinate, and character columns.
- 🧹 Handles extra spaces and invalid or missing data.
- 🧩 Reconstructs the secret message using a coordinate-based grid.
- ⚠️ Handles HTTP errors, missing tables, and invalid coordinate values.
- 🐍 Uses Python for data processing and message decoding.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Requests** — Downloads document content from a URL
- **Pandas** — Extracts and processes HTML tables
- **StringIO** — Allows HTML text to be parsed by Pandas

## 📂 Project Structure

```text
secret-message-decoder/
├── main.py
├── requirements.txt
└── README.md
```

- `main.py` — Contains the message-decoding logic.
- `requirements.txt` — Lists the required Python packages.
- `README.md` — Explains the project and how to run it.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/secret-message-decoder.git
```

Replace `YOUR-USERNAME` with your GitHub username and use your actual repository name.

### 2. Navigate to the project directory

```bash
cd secret-message-decoder
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On Linux or macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

Create a `requirements.txt` file containing:

```text
requests
pandas
lxml
```

Then install the packages:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the Python script:

```bash
python main.py
```

The script downloads the document, extracts the first HTML table, identifies the coordinate and character columns, and prints the reconstructed secret message in the terminal.

**Note:** The Google Docs document must be publicly accessible, and its first HTML table must contain recognizable coordinate and character columns.

## 🧠 How It Works

1. **Download the document:** Sends an HTTP GET request to the provided URL.
2. **Extract the table:** Uses `pandas.read_html()` to find HTML tables in the document.
3. **Identify columns:** Detects the X-coordinate, Y-coordinate, and character columns using their names.
4. **Validate the data:** Converts coordinates to integers and skips invalid entries.
5. **Create the grid:** Determines the minimum and maximum X and Y coordinates to calculate the grid dimensions.
6. **Place the characters:** Maps each character to its corresponding grid position.
7. **Decode the message:** Prints the completed grid row by row to reveal the hidden message.

### Coordinate Mapping

The script uses the following mapping:

```python
grid[max_y - y][x - min_x] = char
```

This adjusts the coordinates so that larger Y-values appear higher in the printed output, while the smallest X-coordinate begins at the left edge of the grid.

## 🛡️ Error Handling

The program includes basic error handling for:

- HTTP request failures and timeouts
- Documents without HTML tables
- Unexpected column names
- Invalid coordinate values
- Missing or invalid character entries

If the column names do not match the expected format, the program prints the detected column names and sample rows to help troubleshoot the issue.

## 🚀 Possible Improvements

- Support multiple HTML table formats.
- Add command-line arguments for custom document URLs.
- Export the decoded message to a text file.
- Add unit tests for coordinate mapping and malformed input.
- Improve duplicate-coordinate handling and Unicode character validation.

## 🎯 Learning Outcomes

This project demonstrates practical experience with:

- Python scripting and automation
- HTTP requests and web data extraction
- HTML table parsing
- Data cleaning and validation
- Two-dimensional arrays and coordinate mapping
- Exception handling and debugging

## 👩‍💻 Author

**Samriddhi Saxena**

- GitHub: [@samriddhi30gauri](https://github.com/samriddhi30gauri)
- LinkedIn: [Samriddhi Saxena](https://www.linkedin.com/in/samriddhi-saxena-148908339/)

---

⭐ If you find this project useful, consider giving the repository a star!
