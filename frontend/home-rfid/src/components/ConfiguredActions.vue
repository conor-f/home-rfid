<template>
  <ul
    v-for="module in configuredActions"
    :key="module"
    >
    <ActionComponent
      :moduleName="module.module"
      />
    <li>
      <ul
        v-for="action in module.actions"
        :key="action"
        >
        <li>
          {{ action }}
        </li>
      </ul>
    </li>
  </ul>
</template>

<script>
import ActionComponent from '@/components/ActionComponent.vue'

export default {
  name: 'ConfiguredActions',
  components: {
    ActionComponent
  },
  data: function() {
    return {
      'configuredActions': [],  // A list of already configured actions.
      'allActions': []  // A list of all possible actions.
    }
  },
  methods: {
    'getActions': function(configured=true) {
      const axios = require('axios')
      let self = this

      axios.get(
        'http://127.0.0.1:8081/api/list_actions?configured=' + configured
      )
      .then(function (response) {
        console.log(response.data.actions)
        if (configured) {
          self.configuredActions = response.data.actions
        } else {
          self.allActions = response.data.actions
          self.configuredActions = response.data.actions
        }
      })
      .catch(function (error) {
        console.log(error);
      })
    },
    'populateConfiguredActions': function() {
      this.getActions()
    },
  },
  created: function() {
    this.populateConfiguredActions()
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
