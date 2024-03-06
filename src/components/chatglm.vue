<template>
  <el-container>
    <el-main class="chat-container" v-show="messages.length>0">
      <div class="chat-history" ref="chatHistory">
        <div v-for="message in messages" :key="message.id" class="message">
          <el-card v-if="message.sender === 'user'" class="user-message" shadow="hover">{{ message.text }}</el-card>
          <el-card v-else class="bot-message" shadow="hover">{{ message.text }}</el-card>
        </div>
      </div>
      <div id="history-end"></div>
    </el-main>
    <div class="tip" style="text-align:center;" v-if="messages.length===0">How can I help you?</div>
    <el-footer class="sendarea">
      <el-input class="textarea" type="textarea" :autosize="{ minRows: 2, maxRows: 4 }" v-model="userMessage" @keyup.enter="sendMessage" placeholder="Type your message..."></el-input>
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
  .chat-container {
    width: 500px;
    max-height: 85vh;
    margin: auto;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 10px;
    overflow-y:auto;
  }

  .tip {
    font-weight: bold;
    font-size: larger;
  }

  .sendarea {
    width: 500px;
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .textarea {
    width:80%;
  }
  
  .message {
    margin-bottom: 10px;
  }
  
  .user-message {
    background-color: #f0f0f0;
    padding: 5px 10px;
    border-radius: 5px;
  }
  
  .bot-message {
    background-color: #d9edf7;
    padding: 5px 10px;
    border-radius: 5px;
  }
  </style>