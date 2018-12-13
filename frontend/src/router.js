import Vue from 'vue';
import Router from 'vue-router';
import Tasks from './components/Tasks.vue';
import Login from '@/components/Login.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/tasks',
      component: Tasks,
    },
    {
      path: '/login',
      component: Login,
    },
  ],
});
