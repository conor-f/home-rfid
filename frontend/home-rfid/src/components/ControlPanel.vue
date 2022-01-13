<template>
    <button
      @click="badSubmitHandler"
      type="button">
      Submit this horror show
    </button>
    <va-input
      class="mb-4"
      v-model="badTextInput"
      type="textarea"
      label="Bad Input for Actions"
      autosize
    />
</template>

<script>
export default {
  name: 'ControlPanel',
  data: function() {
    return {
      'badTextInput': '[\n\
        {\n\
          "module": "homeassistant",\n\
          "action": "toggle",\n\
          "extra": {\n\
            "entity_id": "light.globe"\n\
          }\n\
        }\n\
      ]',
      'configuredActions': []
    }
  },
  methods: {
    'badSubmitHandler': function() {
      console.log(this.badTextInput)
      const axios = require('axios')
      let self = this

      axios.post(
        'http://127.0.0.1:8081/api/set_next_card',
        {
          data: self.badTextInput
        },
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        }
      )
        .then(function (response) {
          console.log(response)
        })
        .catch(function (error) {
          console.log(error);
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
