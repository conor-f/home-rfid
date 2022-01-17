<template>
  <div>
    <span class="mb-2">
      <va-icon
        v-if="actionDetails.entityID.includes('light')"
        name="lightbulb"
        class="mr-1"/>
      {{ actionDetails.entityID }}: {{ actionDetails.action }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'HomeAssistantDisplayComponent',
  props: [
    'actionDetails'
  ],
  data: function() {
    return {

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
