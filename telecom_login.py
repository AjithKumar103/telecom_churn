import streamlit as st


def authenticate(username, password):
    # Your authentication logic here
    if username == 'admin' and password == 'password':
        return True
    else:
        return False


def main():
    # Custom CSS to add background design
    page_bg_img = '''
        <style>
        body {
            background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Ftelecommunication%2F&psig=AOvVaw1kLAbUvv0Cg3TJC2WBVLE5&ust=1683822152618000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCLiauryU6_4CFQAAAAAdAAAAABAE");
            background-size: cover;
        }
        </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Logged in as {}".format(username))
            # Add your logic for the authenticated user here
        else:
            st.error("Invalid username or password")


if __name__ == '__main__':
    main()
