<template>
  <ChatGLM />
</template>

<script>
import ChatGLM from './components/chatglm.vue'

export default {
  name: 'App',
  components: {
    ChatGLM
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin:0;
  padding:0
}
</style>
