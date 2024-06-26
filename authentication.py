import streamlit as st
from supabase_helpers import sign_up_user, login_user, add_idea


def authentication_page():
    st.title("Login")

    tabs = st.tabs(["Login", "Sign Up"])

    with tabs[0]:
        st.subheader("Login")
        login_email = st.text_input("Email", key="login_email")
        login_password = st.text_input(
            "Password", type="password", key="login_password"
        )

        if st.button("Login"):
            print(login_email, login_password)
            if user := login_user(login_email, login_password):
                st.success(f"Successfully logged in.")
                st.session_state.user_id = user.user.id
                st.rerun()
            else:
                st.error(
                    f"Login failed. Please make sure you have confirmed your email."
                )

    with tabs[1]:
        st.subheader("Sign Up")
        signup_email = st.text_input("Email", key="signup_email")
        signup_password = st.text_input(
            "Password", key="signup_password", type="password"
        )
        signup_password_confirm = st.text_input(
            "Confirm Password", key="signup_password_confirm", type="password"
        )

        if st.button("Sign Up"):
            print(signup_email, signup_password, signup_password_confirm)
            if signup_password == signup_password_confirm:
                if user := sign_up_user(signup_email, signup_password):
                    st.success(f"Confirmation email sent to {signup_email}")
                else:
                    st.error("Sign Up Failed.")
