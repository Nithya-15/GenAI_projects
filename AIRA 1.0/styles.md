<!--Contributed by : Prasanth Bysani and Gayathri Tholeti-->

<style>
    .title {
        top: 60px;
        text-align: center;
        color: #4CAF50;
        font-size: 36px;
        font-weight: bold;
    }
    .subtitle {
        top: 120px;
        text-align: center;
        color: #4CAF50;
        font-size: 18px;
    }
    .box {
        background-color: #f9f9f9; 
        padding: 20px; 
        border-radius: 10px; 
        margin-bottom: 20px; 
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); 
        height: 200px; 
        display: flex; 
        flex-direction: column; 
        justify-content: center; 
        text-align: center;
    }
    .button {
        background-color: #4CAF50; 
        color: white; 
        padding: 10px 20px; 
        border: none; 
        border-radius: 5px; 
        font-size: 16px; 
        cursor: pointer;
        text-align: center;
    }
    .chat-container {
        margin-top: 240px;
        max-height: 60vh;
        overflow-y: auto;
        padding: 10px;
    }
    .chat-message {
        padding: 10px 15px;
        margin: 5px 0;
        border-radius: 10px;
        max-width: 100%;
    }
    .chat-message.user {
        color: #333;
        align-self: flex-end;
        border: none;
    }
    .chat-message.assistant {
       border: 1px solid #bbdefb;
       border:None
    }
    .stTextInput textarea {
        background-color: white;
        border-radius: 10px;
        padding: 12px;
        border: 2px solid #ccc;
        box-shadow: none;
    }
</style>
