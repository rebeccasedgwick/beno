<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link>
      <br>
      <router-link to="/login">Login</router-link>
      <br>
      <router-link to="/tasks">Tasks</router-link>
    </nav>
    <router-view/>
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
