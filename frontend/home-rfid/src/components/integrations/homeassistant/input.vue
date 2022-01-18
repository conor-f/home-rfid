<template>
  <div>
    <va-select
      id="entity_id"
      class="mb-2"
      label="Entity:"
      :options="entityOptions"
      v-model="selectedEntityName"
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
    'inputIndex'
  ],
  data: function() {
    return {
      /*
        Stores all available entities as a list of dicts e.g:
        [
          {
            "entity_id": "light.cube",
            "entity_name": "Cube",
            "actions": [
              "turn_on",
              "turn_off",
              "toggle"
            ]
          },
          ..
        ]
      */
      'availableEntities': [],
      'localSelectedEntityID': '',
      'localSelectedEntityName': '',
      'localSelectedAction': '',
    }
  },
  emits: [
    'updated',
  ],
  computed: {
    'selectedEntityName': {
      get() {
        return this.localSelectedEntityName
      },
      set(value) {
        for (let e of this.availableEntities) {
          if (e.entity_name == value) {
            this.localSelectedEntityID = e.entity_id
          }
        }

        this.localSelectedEntityName = value
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
      if (this.availableEntities == undefined) {
        return []
      }

      let entityIDs = []

      for (let entity of this.availableEntities) {
        entityIDs.push(entity.entity_name)
      }

      return entityIDs
    },
    'actionsOptions': function() {
      if (this.availableEntities == undefined || this.localSelectedEntityID == undefined) {
        return []
      }

      for (let entity of this.availableEntities) {
        if (entity.entity_id == this.localSelectedEntityID) {
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
          inputIndex: this.inputIndex,
          entityID: this.localSelectedEntityID,
          entityName: this.localSelectedEntityName,
          action: this.localSelectedAction
        }
      )
    },
    'getAvailableEntities': function() {
      const axios = require('axios')
      let self = this

      axios.get(
        'http://127.0.0.1:8081/api/list_actions'
      )
      .then(function (response) {
        for (let module of response.data.actions) {
          if (module.module == "homeassistant") {
            self.availableEntities = module.actions
          }
        }
      })
      .catch(function (error) {
        console.log(error);
      })
    },
  },
  created: function() {
    this.getAvailableEntities()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
