import streamlit as st

# Title of the page
st.title("Our Website")

# Top navigation bar using radio buttons
option = st.radio("Navigate to:", ("About Us", "Product", "Contact Us"), horizontal=True)

# Display section based on the user choice
if option == "About Us":
    st.header("About Us")
    st.write("""
        Welcome to our website! We are a company committed to delivering exceptional products and services to our customers.
        Our team is passionate about innovation and customer satisfaction.
        We have been in the industry for over 10 years and pride ourselves on our high-quality products.
    """)

elif option == "Product":
    st.header("Our Product")
    st.write("""
        We offer a range of high-quality products designed to meet the needs of our customers. 
        Our flagship product is the SuperWidget, which helps you achieve efficiency and productivity in your daily tasks.
        Whether you're a business or an individual, we have something tailored just for you.
    """)

elif option == "Contact Us":
    st.header("Contact Us")
    st.write("""
        We'd love to hear from you! Whether you have questions, comments, or feedback, feel free to reach out.
        - Email: contact@ourcompany.com
        - Phone: +1 234 567 890
        - Address: 123 Business St, City, Country
    """)

    # Optional: Include a form or additional elements (such as buttons, images, etc.)
    st.text_input("Name")
    st.text_input("Email")
    st.text_area("Message")
    st.button("Submit")
