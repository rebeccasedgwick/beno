<template>
  <div class="tasks">
    <h1 class="title">Beno</h1>

    <div class="columns">
      <div class="column is-half">
        <h2 class="subtitle">Task</h2>

        <div class="task">
          <div class="card" v-for="task in tasks">
            <div class="card-content">
              <div class="content">
                {{ task.description }}
              </div>
            </div>

            <footer class="card-footer">
              <a class="card-footer-item">Done</a>
            </footer>
          </div>
        </div>
      </div>

      <div class="column is-half">
        <h2 class="subtitle">High priority</h2>

        <div class="high-priority">
          <div class="card" v-for="task in tasks" v-if="task.priority == 1">
            <div class="card-content">
              <div class="content">
                <ul>
                  <li>{{ task.description }}</li>
                  <li>{{ task.due_by }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Tasks',
  data () {
    return {
      tasks: []
    }
  },
  mounted () {
    this.getTasks();
  },
  methods: {
    getTasks() {
        axios({
            method:'GET',
            url: 'https://5c07feb5646dca0013f87eba.mockapi.io/task',
        }).then(response => this.tasks = response.data);
    }
  }
}
</script>

<style scoped>
.select, select {
  width: 100%;
}

.card {
  margin-bottom: 25px;
}

.done {
  opacity: 0.3;
}
</style>
