import streamlit as st
import random
from datetime import datetime

# Configure the page
st.set_page_config(
    page_title="Finacle Demo - Loan Processing",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .demo-banner {
        background-color: #ff4444;
        color: white;
        text-align: center;
        padding: 10px;
        font-weight: bold;
        margin-bottom: 20px;
        border-radius: 5px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    .login-box {
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .disclaimer {
        background-color: #fff3cd;
        border-left: 5px solid #ffeaa7;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 20px;
        font-size: 12px;
    }
    .btn {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
        border: none;
        color: white;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .btn-primary {
        background-color: #3498db;
    }
    .btn-approve {
        background-color: #27ae60;
    }
    .btn-reject {
        background-color: #e74c3c;
    }
    .btn-logout {
        background-color: #95a5a6;
    }
</style>
""", unsafe_allow_html=True)

# Demo credentials
VALID_USERNAME = "loanbot_01"
VALID_PASSWORD = "JesusCares4Me"

def login_page():
    st.markdown('<div class="demo-banner">⚠️ DEMO WEBSITE - NOT REAL - FOR DEMONSTRATION PURPOSES ONLY ⚠️</div>', unsafe_allow_html=True)
    
    with st.container():
        col1, col2, col3 = st.columns([1,3,1])
        with col2:
            with st.container():
                st.markdown('<div class="login-box">', unsafe_allow_html=True)
                
                st.markdown("""
                <div style="text-align: center; margin-bottom: 20px;">
                    <h2>Finacle Demo Portal</h2>
                    <p>Loan Processing System</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('<div class="disclaimer">This is a mockup demonstration only. No real data is processed.</div>', unsafe_allow_html=True)
                
                with st.form("login_form"):
                    username = st.text_input("Username", key="username")
                    password = st.text_input("Password", type="password", key="password")
                    
                    if st.form_submit_button("Login", type="primary"):
                        if username == VALID_USERNAME and password == VALID_PASSWORD:
                            st.session_state.logged_in = True
                            st.rerun()
                        else:
                            st.error("Invalid credentials. Please use:\nUsername: loanbot_01\nPassword: JesusCares4Me")
                
                st.markdown("""
                <div style="font-size: 12px; text-align: center; margin-top: 20px;">
                    <strong>Demo Credentials:</strong><br>
                    Username: loanbot_01<br>
                    Password: JesusCares4Me
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown('</div>', unsafe_allow_html=True)

def dashboard():
    st.markdown('<div class="demo-banner">⚠️ DEMO WEBSITE - NOT REAL - FOR DEMONSTRATION PURPOSES ONLY ⚠️</div>', unsafe_allow_html=True)
    
    st.title("Loan Application Processing")
    st.markdown('<div class="disclaimer">All data is simulated. No real financial decisions are made.</div>', unsafe_allow_html=True)
    
    with st.form("loan_form"):
        st.subheader("Applicant Information")
        
        # SSN input with format hint
        ssn = st.text_input(
            "Social Security Number (SSN)", 
            placeholder="XXX-XX-XXXX",
            help="Enter in format XXX-XX-XXXX",
            key="ssn"
        )
        
        # Loan amount input
        loan_amount = st.number_input(
            "Loan Amount ($)", 
            min_value=1000, 
            max_value=100000, 
            step=500,
            key="loan_amount"
        )
        
        # Decision buttons
        col1, col2 = st.columns(2)
        with col1:
            approve = st.form_submit_button("Approve", type="primary", use_container_width=True)
        with col2:
            reject = st.form_submit_button("Reject", type="secondary", use_container_width=True)
        
        if approve or reject:
            if not ssn or not loan_amount:
                st.error("Please complete all fields")
            else:
                # Validate SSN format
                if not (len(ssn) == 11 and ssn.count('-') == 2 and ssn.replace('-','').isdigit()):
                    st.error("Please enter SSN in XXX-XX-XXXX format")
                else:
                    decision = "APPROVED" if approve else "REJECTED"
                    masked_ssn = f"XXX-XX-{ssn[-4:]}"  # Mask for display
                    
                    st.success(f"""
                    **Demo Application {decision}**
                    - SSN: {masked_ssn}
                    - Amount: ${loan_amount:,}
                    """)
                    
                    # Store in session history
                    if 'history' not in st.session_state:
                        st.session_state.history = []
                    
                    st.session_state.history.append({
                        "ssn": masked_ssn,
                        "amount": loan_amount,
                        "decision": decision,
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
    
    # Logout button
    if st.button("Logout", type="secondary"):
        st.session_state.logged_in = False
        st.rerun()

# Main app logic
def main():
    if not hasattr(st.session_state, 'logged_in'):
        st.session_state.logged_in = False
    
    if st.session_state.logged_in:
        dashboard()
    else:
        login_page()

if __name__ == "__main__":
    main()