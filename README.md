# U_PdfToExcel

## PDF to Excel Converter

This project is a simple PDF to Excel converter that extracts both text and table data from PDF files and saves them into an Excel workbook with two separate sheets: one for text content and one for tables.

## YouTube 

I have also created a YouTube video explaining this project. You can watch the video through the link below:

[![Watch the video](https://img.youtube.com/vi/ekmzppcW3jc/0.jpg)](https://youtu.be/ekmzppcW3jc)

Click the image or the link to watch the video:  
[https://youtu.be/ekmzppcW3jc](https://youtu.be/ekmzppcW3jc)



## Features

- Extracts text content from each page of the PDF and stores it in a sheet named `U_TextContent`.
- Extracts tables from each page of the PDF and stores them in a sheet named `U_Tables`.
- Logs are automatically created in the specified directory with details of the process.

## Requirements

- Python 3.x
- `Flask`
- `pdfplumber`
- `pandas`
- `openpyxl`
- `logging`

### Install Required Packages

Run the following command to install the required Python packages:

```bash
pip install Flask pdfplumber pandas openpyxl
```

### How to Run the Project

Clone the repository:

```bash
git clone https://github.com/Uguryldz/U_PdfToExcel.git
cd U_PdfToExcel
```

Run the U_PdfToExcel app:

```bash
python  U_PdfToExcel.py
```

The app will be running on http://0.0.0.0:8089/.

Usage:

You can use an HTTP client like Postman or cURL to send a PDF file to the server.

- Endpoint: `/upload`.
- Method: `POST`.
- Form-data:
- `file` : The PDF file you want to convert.
- `output_path` : The file path where the Excel file will be saved.

### Example Request

Using cURL:

```bash
curl -X POST http://localhost:8089/upload \
    -F "file=@path_to_your_file.pdf" \
    -F "output_path=path_to_save_output.xlsx"
```
## Log Files

The application generates log files in the `C:\U_PdfToExcel\logs` directory. The logs include information about the PDF processing and any errors encountered.

## Error Handling

If there are any issues during PDF processing (such as unsupported formats), the app will log the error and return an appropriate HTTP status code.

## License

This project is licensed under the MIT License.


