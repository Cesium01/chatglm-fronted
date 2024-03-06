<template>
  <el-container class="main-container">
    <el-main class="chat-container" v-show="messages.length>0">
      <div class="chat-history" ref="chatHistory">
        <div v-for="message in messages" :key="message.id">
          <div v-if="message.sender === 'user'" class="message-line">
            <el-card  class="user-message" shadow="hover">{{ message.text }}</el-card>
            <el-avatar :size="50" src="ava.jpg" style="margin: 10px"/>
          </div>
          <div v-else class="message-line">
            <el-avatar :size="50" src="ava.jpg" style="margin: 10px"/>
            <el-card class="bot-message" shadow="hover">{{ message.text }}</el-card>
          </div>
        </div>
      </div>
      <div id="history-end"></div>
    </el-main>
    <div class="tip" v-if="messages.length===0">How can I help you?</div>
    <el-footer class="sendarea">
      <el-input class="textarea" type="textarea" :autosize="{ minRows: 1, maxRows: 4 }" v-model="userMessage" @keyup.enter="sendMessage" placeholder="Type your message..."></el-input>
      <el-button type="primary" @click="sendMessage">发送</el-button>
    </el-footer>
  </el-container>
</template>
  
  <script>
  //import axios from 'axios';
  
  export default {
    name: 'ChatGLM',
    data() {
      return {
        userMessage: '',
        messages: []
      };
    },
    methods: {
      async sendMessage() {
        if (this.userMessage.trim() === '') return;
        
        this.messages.push({ id: this.messages.length, sender: 'user', text: this.userMessage });
        //const response = await axios.post('http://localhost:5000/chat', { message: this.userMessage });
        const response = {data: 'this is a fake response.this is a fake response.this is a fake response.this is a fake response.this is a fake response.'};
        const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));
        
        this.userMessage = '';
        this.scrollToBottom();
        await sleep(3000);
        this.messages.push({ id: this.messages.length, sender: 'bot', text: response.data });
        this.scrollToBottom();
      },
      scrollToBottom() {
        setTimeout(() => {
          document.getElementById('history-end').scrollIntoView({ behavior: "smooth"});
        }, 100);
      }
    }
  };
  </script>
  
  <style scoped>
  .main-container {
    background-color:#b0c4de;
    width:100%;
    height:100%;
    position:fixed;
    background-size:100% 100%;
  }
  .chat-container {
    width: 800px;
    max-height: 80vh;
    margin: auto;
    /* border: 1px solid #ccc;
    border-radius: 10px; */
    padding: 10px;
    overflow-y:auto;
    background: rgba(255, 255, 255, 0.2);
    -webkit-backdrop-filter: blur(8px);
    backdrop-filter: blur(8px);
    border-radius: 25px;
    box-shadow:inset 0 0 6px rgba(255, 255, 255, 0.2);
    animation:fadenum 3s 1;
  }

  @keyframes fadenum{
   0%{opacity: 0;}
   100%{opacity: 1;}
  }

  .tip {
    width:100%;
    height:100%;
    font-weight: bold;
    font-size: larger;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .sendarea {
    width: 40%;
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .textarea {
    width:80%;
  }
  
  .message-line {
    display: flex;
    margin: 10px;
  }
  
  .user-message {
    background-color: #f0f0f0;
    padding: 5px 10px;
    border-radius: 5px;
    max-width: 75%;
    margin-left: auto;
    word-wrap:break-word;
    word-break:normal;
    animation:fadenum 2s 1;
  }
  
  .bot-message {
    background-color: #d9edf7;
    padding: 5px 10px;
    border-radius: 5px;
    max-width: 75%;
    margin-right: auto;
    word-wrap:break-word;
    word-break:normal;
    animation:fadenum 2s 1;
  }
  </style>