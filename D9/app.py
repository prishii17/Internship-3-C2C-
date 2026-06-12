import streamlit as st
import requests

st.title("🛒 Product Store")

# Fetch data from Fake Store API
url = "https://fakestoreapi.com/products"
response = requests.get(url)

if response.status_code == 200:
    products = response.json()

    for product in products:
        st.subheader(product["title"])

        st.image(product["image"], width=150)

        st.write("💲 Price:", product["price"])
        st.write("⭐ Rating:", product["rating"]["rate"])
        st.write("📦 Category:", product["category"])

        with st.expander("Description"):
            st.write(product["description"])

        st.markdown("---")

else:
    st.error("Failed to fetch products.")
