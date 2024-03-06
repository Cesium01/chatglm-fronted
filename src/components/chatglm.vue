<template>
  <div class="flex flex-col h-screen">
    <!-- 标题栏 -->
    <div class="bg-gray-800 text-white flex justify-center items-center py-4 px-6 fixed top-0 left-0 right-0 z-50 h-16">
      <h1 class="text-lg font-semibold">聊天界面</h1>
    </div>
    
    <div class="container mx-auto px-4 py-4 h-full flex flex-col pt-16">
      <div class="flex-grow overflow-hidden">
        <div class="chat-area bg-white shadow-md rounded-lg flex flex-col h-full">
          <div class="chat-container flex-grow overflow-y-auto">
            <div class="chat-history p-4 space-y-4" ref="chatHistory">
              <div v-for="message in messages" :key="message.id" class="flex items-end" :class="{'justify-end': message.sender === 'user', 'justify-start': message.sender !== 'user'}">
                <!-- 头像显示 -->
                <div v-if="message.sender !== 'user'" class="flex-none w-12 h-12 mr-2">
                  <img class="w-full h-full rounded-full object-cover" :src="message.avatar || 'default-bot-avatar-url'" alt="Avatar">
                </div>
                <!-- 消息气泡 -->
                <div :class="{'bg-blue-500 text-white': message.sender === 'user', 'bg-green-500 text-white': message.sender !== 'user'}" class="message p-3 rounded-lg shadow">
                  {{ message.text }}
                </div>
                <!-- 头像显示 -->
                <div v-if="message.sender === 'user'" class="flex-none w-12 h-12 ml-2">
                  <img class="w-full h-full rounded-full object-cover" :src="message.avatar || 'default-user-avatar-url'" alt="Avatar">
                </div>
              </div>
            </div>
            <div id="history-end" class="clear-both"></div>
          </div>
        </div>
      </div>
      <div class="sendarea bg-gray-100 p-4 rounded-lg shadow mt-4">
        <div class="flex items-center space-x-4">
          <input type="text" class="flex-1 form-input border-gray-300 rounded-md shadow-sm" v-model="userMessage" @keyup.enter="sendMessage" placeholder="请输入消息..." />
          <button type="button" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition ease-in-out duration-150" @click="sendMessage">
            发送
          </button>
        </div>
      </div>
    </div>
  </div>
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
      
      this.messages.push({ id: this.messages.length, sender: 'user', text: this.userMessage ,avatar:"./face.png"});
      //const response = await axios.post('http://localhost:5000/chat', { message: this.userMessage });
      const response = {data: 'this is a fake response.this is a fake response.this is a fake response.this is a fake response.this is a fake response.'};
      const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));
      
      this.userMessage = '';
      this.scrollToBottom();
      await sleep(500);
      this.messages.push({ id: this.messages.length, sender: 'bot', text: response.data ,avatar:"./face.png"});
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

</style>
