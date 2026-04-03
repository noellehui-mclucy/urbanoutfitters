from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV once when the app starts
df = pd.read_csv('product.csv')


@app.route('/')
def home():
    # Clean up the data a bit (optional but recommended)
    df_clean = df.copy()
    # Remove the weird "Sale price:\n" text if any
    df_clean['price'] = df_clean['price'].astype(str).str.replace('Sale price:\n', '').str.strip()

    products = []
    for _, row in df_clean.iterrows():
        products.append({
            'name': str(row['product name']).strip(),
            'price': str(row['price']).strip(),
            # For now we use placeholder images. You can add real image URLs later.
            'img': f"https://picsum.photos/id/{100 + _ % 100}/400/550"  # different image for each item
        })

    return render_template('index.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)