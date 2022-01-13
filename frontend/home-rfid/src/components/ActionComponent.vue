<template>
  <hr/>
  IN COMPONENT
  {{ moduleName }}
  <hr/>
</template>

<script>
export default {
  name: 'ActionComponent',
  props: [
    'moduleName',
  ],
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

      axios.get('http://127.0.0.1:8081/api/list_actions?configured=' + configured)
        .then(function (response) {
          console.log(response.data.actions)
          if (configured) {
            self.configuredActions = response.data.actions
          } else {
            self.allActions = response.data.actions
          }
        })
        .catch(function (error) {
          console.log(error);
        })
    },
    'populateConfiguredActions': function() {
      this.getActions()
    },
  }
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
