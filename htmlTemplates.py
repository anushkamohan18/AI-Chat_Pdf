css = """
<style>
/* Main styling */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #333;
}

/* Chat container styling */
.chat-container {
    max-height: 600px;
    overflow-y: auto;
    padding: 10px;
    border-radius: 12px;
    background-color: #f9f9fc;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    margin-top: 20px;
}

/* Message styling */
.chat-message {
    padding: 12px 16px;
    border-radius: 18px;
    margin-bottom: 16px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03);
    max-width: 85%;
    position: relative;
    line-height: 1.5;
    animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

.user {
    background-color: #E1F5FE;
    background: linear-gradient(135deg, #E1F5FE 0%, #B3E5FC 100%);
    text-align: right;
    margin-left: auto;
    border-bottom-right-radius: 6px;
    color: #01579B;
}

.bot {
    background-color: #FFFFFF;
    text-align: left;
    margin-right: auto;
    border-bottom-left-radius: 6px;
    color: #37474F;
    border-left: 4px solid #2979FF;
}

/* Header styling */
h1, h2, h3 {
    font-weight: 600;
    color: #263238;
}

/* Button styling */
.stButton > button {
    background-color: #2979FF;
    color: white;
    border-radius: 8px;
    border: none;
    padding: 8px 16px;
    transition: all 0.3s ease;
    font-weight: 500;
}

.stButton > button:hover {
    background-color: #1565C0;
    box-shadow: 0 4px 8px rgba(41, 121, 255, 0.2);
    transform: translateY(-2px);
}

/* File uploader styling */
.uploadedFile {
    border-radius: 10px;
    border: 2px dashed #2979FF;
    padding: 20px;
    background-color: rgba(41, 121, 255, 0.05);
    text-align: center;
}

/* Input box styling */
.stTextInput > div > div > input {
    border-radius: 20px;
    border: 1px solid #E0E0E0;
    padding: 10px 15px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.stTextInput > div > div > input:focus {
    border-color: #2979FF;
    box-shadow: 0 2px 10px rgba(41, 121, 255, 0.15);
}

/* Sidebar styling */
.css-1d391kg {
    background-color: #F5F7FA;
    border-right: 1px solid #E0E0E0;
}

/* Custom document tag */
.document-tag {
    display: inline-block;
    background-color: #E3F2FD;
    color: #1565C0;
    padding: 4px 10px;
    border-radius: 12px;
    font-size: 0.8em;
    margin-right: 5px;
    margin-bottom: 5px;
}

/* Separator styling */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #E0E0E0, transparent);
    margin: 15px 0;
}

/* PDF icon styling */
.pdf-icon {
    display: inline-block;
    margin-right: 5px;
    color: #F44336;
}

/* Message timestamp */
.message-time {
    font-size: 0.7em;
    opacity: 0.7;
    margin-top: 5px;
}

/* Loading animation */
.loading {
    display: flex;
    width: 20px;
    height: 20px;
    border: 3px solid rgba(41, 121, 255, 0.3);
    border-radius: 50%;
    border-top-color: #2979FF;
    animation: spin 1s ease-in-out infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

/* How it works box styling - Updated with less bright background and black text */
.how-it-works-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #f0f0f5;
    margin-bottom: 20px;
    color: #000000;
    border: 1px solid #e0e0e0;
}

.how-it-works-box p {
    color: #000000;
    margin-bottom: 5px;
}

.how-it-works-box ol {
    color: #000000;
    margin-left: 15px;
    padding-left: 0px;
}

.how-it-works-box li {
    color: #000000;
}

/* Tip box styling */
.tip-box {
    background-color: #f0f0f5;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
    color: #000000;
    border: 1px solid #e0e0e0;
}

/* Welcome box styling */
.welcome-box {
    text-align: center;
    padding: 40px 20px;
    background-color: #f0f0f5;
    border-radius: 10px;
    margin-top: 20px;
    color: #000000;
    border: 1px solid #e0e0e0;
}
</style>
"""

user_template = """
<div class="chat-message user">
    <strong>You:</strong> {{MSG}}
    <div class="message-time">Just now</div>
</div>
"""

bot_template = """
<div class="chat-message bot">
    <strong>AI:</strong> {{MSG}}
    <div class="message-time">Just now</div>
</div>
"""