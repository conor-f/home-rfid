<template>
  <div>
    <va-select
      id="entity_id"
      class="mb-2"
      label="Entity:"
      :options="entityOptions"
      v-model="selectedEntity"
      />
    <va-select
      id="entity_action"
      class="mb-2"
      label="Action:"
      :options="actionsOptions"
      v-model="selectedAction"
      />
  </div>
</template>

<script>
export default {
  name: 'HomeAssistantInputComponent',
  props: [
    'actionIndex'
  ],
  data: function() {
    return {
      'localSelectedEntity': '',
      'localSelectedAction': '',
      'availableOptions': [],
    }
  },
  emits: [
    'updated',
  ],
  computed: {
    'selectedEntity': {
      get() {
        return this.localSelectedEntity
      },
      set(value) {
        this.localSelectedEntity = value
        this.emitUpdate()
      }
    },
    'selectedAction': {
      get() {
        return this.localSelectedAction
      },
      set(value) {
        this.localSelectedAction = value
        this.emitUpdate()
      }
    },
    'entityOptions': function() {
      let entity_ids = []

      if (this.availableOptions == undefined) {
        return []
      }

      for (let entity of this.availableOptions) {
        entity_ids.push(entity.entity_id)
      }

      return entity_ids
    },
    'actionsOptions': function() {
      for (let entity of this.availableOptions) {
        if (entity.entity_id == this.selectedEntity) {
          return entity.actions
        }
      }
      
      return []
    }
  },
  methods: {
    'emitUpdate': function() {
      this.$emit(
        'updated',
        {
          actionIndex: this.actionIndex,
          entityID: this.localSelectedEntity,
          action: this.localSelectedAction
        }
      )
    },
    'getAvailableOptions': function() {
      const axios = require('axios')
      let self = this

      axios.get(
        'http://127.0.0.1:8081/api/list_actions'
      )
      .then(function (response) {
        for (let module of response.data.actions) {
          if (module.module == "homeassistant") {
            for (let option of module.actions) {
              self.availableOptions.push(option)
            }
          }
        }
      })
      .catch(function (error) {
        console.log(error);
      })
    },
  },
  created: function() {
    this.getAvailableOptions()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
