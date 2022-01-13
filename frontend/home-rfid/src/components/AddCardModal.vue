<template>
  <va-modal
    v-model="showAddModal"
    size="large"
    ok-text="Add Card"
    @ok="addCard"
    >
    <h1>Add Card</h1>

    <div class="mt-3 mr-5 ml-5" id="inputs">
      <va-input
        type="text"
        class="mb-5"
        id="name"
        label="Card Name"
        v-model="name"
        />

      <div
        v-for="action in actions"
        :key="action.id"
        class="mb-4"
        >
        <va-select
          :id="'action[' + action.id + ']_module'"
          class="mb-2"
          label="Module"
          :options="moduleOptions"
          v-model="actions[action.id].module"
          />
        <HomeAssistantInputComponent
          v-if="action.module == 'homeassistant'"
          :id="'action[' + action.id + ']_input'"
          :actionIndex="action.id"
          @updated="handleComponentUpdate"
          />
      </div>

      <va-button
        icon="add"
        @click="addAction"
        />

      {{ actions }}
    </div>
  </va-modal>
</template>


<script>
import HomeAssistantInputComponent from '@/components/integrations/homeassistant/input.vue'

export default {
  name: 'AddCardModal',
  components: {
    HomeAssistantInputComponent
  },
  data: function() {
    return {
      'showAddModal': true,
      'name': 'Sample Card Name',
      'actions': [
        {
          'id': 0,
          'module': 'homeassistant',
          'extra': {}
        }
      ],
      'moduleOptions': [
        'homeassistant',
        'spotify'
      ]
    }
  },
  methods: {
    handleComponentUpdate(event) {
      let actionIndex = event.actionIndex
      delete event.actionIndex

      this.actions[actionIndex].extra = event
    },
    addAction: function() {
      this.actions.push(
        {
          'id': (this.actions[this.actions.length - 1].id) + 1,
          'module': 'homeassistant',
          'extra': {}
        }
      )
    },
    addCard: function() {
      console.log(this.actions)
      const axios = require('axios')
      // let self = this

      axios.post(
        'http://127.0.0.1:8081/api/add_card',
        {
          'card_name': this.name,
          'actions': this.actions
        }
      ).then(function (response) {
        console.log(response)
      }).catch(function (error) {
        console.log(error);
      })
    }
  },
  created: function() {
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
