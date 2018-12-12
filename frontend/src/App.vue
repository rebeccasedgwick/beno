<template>
  <div id="app">
    <Login />
    <Tasks msg="Welcome to Beno"/>
  </div>
</template>

<script>
import Tasks from './components/Tasks.vue';
import Login from './components/Login.vue';

export default {
  name: 'app',
  components: {
    Tasks,
    Login,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
