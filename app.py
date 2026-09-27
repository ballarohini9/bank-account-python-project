import streamlit as st

if "bank_accounts" not in st.session_state:
    st.session_state.bank_accounts = {}

bank_accounts = st.session_state.bank_accounts

st.title("🏦 Bank Account Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Create Account", "Deposit", "Withdraw", "Check Balance"]
)

if menu == "Create Account":
    st.header("Create Account")

    acc_number = st.text_input("Enter Account Number")
    name = st.text_input("Enter Account Holder Name")

    if st.button("Create Account"):
        if not acc_number or not name:
            st.error("Please enter all details.")
        elif acc_number in bank_accounts:
            st.warning("Account already exists.")
        else:
            bank_accounts[acc_number] = {
                "name": name,
                "balance": 0
            }
            st.success(f"Account created for {name}")

elif menu == "Deposit":
    st.header("Deposit Amount")

    acc_number = st.text_input("Enter Account Number")
    amount = st.number_input("Enter Amount", min_value=0.0)

    if st.button("Deposit"):
        if acc_number not in bank_accounts:
            st.error("Account not found.")
        elif amount <= 0:
            st.error("Invalid deposit amount.")
        else:
            bank_accounts[acc_number]["balance"] += amount
            st.success(
                f"Deposited ₹{amount:.2f}. "
                f"Current Balance: ₹{bank_accounts[acc_number]['balance']:.2f}"
            )

elif menu == "Withdraw":
    st.header("Withdraw Amount")

    acc_number = st.text_input("Enter Account Number")
    amount = st.number_input("Enter Amount", min_value=0.0)

    if st.button("Withdraw"):
        if acc_number not in bank_accounts:
            st.error("Account not found.")
        elif amount <= 0:
            st.error("Invalid withdrawal amount.")
        elif amount > bank_accounts[acc_number]["balance"]:
            st.error("Insufficient funds.")
        else:
            bank_accounts[acc_number]["balance"] -= amount
            st.success(
                f"Withdrawn ₹{amount:.2f}. "
                f"Current Balance: ₹{bank_accounts[acc_number]['balance']:.2f}"
            )

elif menu == "Check Balance":
    st.header("Check Balance")

    acc_number = st.text_input("Enter Account Number")

    if st.button("Check Balance"):
        if acc_number in bank_accounts:
            st.info(
                f"Account Holder: {bank_accounts[acc_number]['name']}"
            )
            st.success(
                f"Account Balance: ₹{bank_accounts[acc_number]['balance']:.2f}"
            )
        else:
            st.error("Account not found.")
