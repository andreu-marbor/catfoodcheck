# CatFoodCheck

CatFoodCheck is a simple FastAPI backend that allows you to scan the barcode (EAN) of cat food products and quickly determine whether the product's brand complies with the WSAVA (World Small Animal Veterinary Association) guidelines.

This project is designed as a minimal viable product (MVP) for integration with a mobile app, providing a fast and reliable API for cat owners to check the suitability of cat food products.

## Features

- Scan cat food barcodes and identify the product
- Check if the product’s brand complies with WSAVA guidelines
- Lightweight FastAPI backend with no external database required for MVP
- Easily deployable on free hosting services like Render.com

## Getting Started

### Prerequisites

- Python 3.9+
- pip
- Git (for deployment and version control)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/catfoodcheck.git
cd catfoodcheck

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

3. Install dependencies:

```bash
pip install -r requirements.txt

### Running Locally

Start the FastAPI server:

```bash
uvicorn main:app --reload

Open your browser at http://127.0.0.1:8000/docs to see the interactive API documentation.

### Deployment

You can deploy this API on free hosting services like Render or Railway.

For Render:

1.Create a new Web Service and connect your GitHub repository.
2.Set the start command to:

```bash
uvicorn main:app --host 0.0.0.0 --port 10000

3.Render will provide a public URL which your mobile app can use.

### Usage

Send a GET request to /scan/{ean} where {ean} is the barcode number of the cat food product:

```bash
GET https://your-app.onrender.com/scan/5411188112345

Example JSON response:

```json
{
  "product": "Sterilised 37",
  "brand": "Royal Canin",
  "wsava": true
}

### WSAVA Compliance

The backend checks if the brand is in a predefined list of WSAVA-compliant brands:
- Royal Canin
- Hill's
- Purina
- Virbac
- Specific

If the brand is in this list, wsava will return true; otherwise, it returns false.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
