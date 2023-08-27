ALL = [
    "brands",
    "categories",
    "customers",
    "order_items",
    "orders",
    "products",
    "staffs",
    "stocks",
    "stores",
]
QC = {
    "CheckDupes": ALL,
    "CheckNA": ALL,
    "CheckPrices": ["products", "order_items"],
    "CheckEmail": ["staffs", "customers"],
    "CheckDates": ["orders"],
}
