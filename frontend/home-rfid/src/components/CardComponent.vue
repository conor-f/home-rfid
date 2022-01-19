<template>
  <div class="flex md6 lg4">
    <va-card square outline>
      <va-card-title>
        {{ card.name }}
      </va-card-title>

      <va-card-content>
        <div v-if="!expanded">
          {{ card.actions.length }} Actions
        </div>

        <div v-if="expanded">
          <div
            v-for="(action, actionID) in card.actions"
            :key="actionID"
            >
            <HomeAssistantDisplayComponent
              v-if="action.module == 'homeassistant'"
              :actionDetails="action.extra"
              />
          </div>
        </div>

        <div id="icons" class="mt-5 mr-4">
          <va-button
            v-if="expanded"
            icon-right="create"
            @click="showTodoModal = true">
            Edit
          </va-button>
          <va-button
            v-if="!expanded"
            icon-right="expand_more"
            @click="toggleCardExpanded"/>
          <va-button
            v-if="expanded"
            icon-right="expand_less"
            @click="toggleCardExpanded"/>
        </div>
      </va-card-content>
    </va-card>
  </div>

  <va-modal
    v-model="showTodoModal"
    size="small"
    message="This feature is WIP!"
    />
</template>

<script>
import HomeAssistantDisplayComponent from '@/components/integrations/homeassistant/display.vue'

export default {
  name: 'CardComponent',
  components: {
    HomeAssistantDisplayComponent
  },
  props: [
    'card_id',
    'card'
  ],
  data: function() {
    return {
      'showTodoModal': false,
      'expanded': false
    }
  },
  methods: {
    toggleCardExpanded: function() {
      this.expanded = !this.expanded
    }
  },
  created: function() {
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
