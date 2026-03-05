from fastapi import FastAPI
import requests

app = FastAPI()

WSAVA_BRANDS = [
    "royal canin",
    "hill's",
    "purina",
    "virbac",
    "specific"
]

@app.get("/scan/{ean}")
def scan_product(ean: str):

    url = f"https://world.openpetfoodfacts.org/api/v0/product/{ean}.json"
    r = requests.get(url)
    data = r.json()

    if data["status"] == 0:
        return {"error": "Producto no encontrado"}

    product = data["product"]
    brand = product.get("brands", "Unknown")

    wsava = any(b in brand.lower() for b in WSAVA_BRANDS)

    return {
        "product": product.get("product_name"),
        "brand": brand,
        "wsava": wsava
    }