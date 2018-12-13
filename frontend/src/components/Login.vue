<template>
  <div class="login">
    <h1 class="title">Login</h1>

    <div class="columns">
      <div class="column">
        <h2 class="subtitle">Enter your account information</h2>

        <form class="login" method="post" v-on:submit.prevent="submitLogin">
          <input type="text" name="email" placeholder="Email" v-model="input.email">
          <input type="password" name="password" placeholder="Password" v-model="input.password">
          <button type="submit" name="Submit">Login</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Login',
  data() {
    return {
      input: {
        email: null,
        password: null,
      },
    };
  },
  methods: {
    submitLogin() {
      axios
        .post(`${process.env.VUE_APP_BACKEND_URL}/api/token/`, {
          email: this.input.email,
          password: this.input.password,
        })
        .then((response) => {
          localStorage.setItem('accessToken', response.data.access);
          localStorage.setItem('refreshToken', response.data.refresh);
        })
        .catch((error) => {
          console.error(error.response);
        });
    },
  },
};
</script>
