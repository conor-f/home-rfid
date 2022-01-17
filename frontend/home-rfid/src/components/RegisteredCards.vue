<template>
  <div id="cardFlexbox">
    <div
      v-for="(card, card_id) in configuredCards"
      :key="card_id"
      class="cardFlexboxItem"
      >
      <CardComponent
        :card_id="card_id"
        :card="card"
        />
    </div>
  </div>

  <va-button
    class="float-right"
    icon="add"
    @click="showAddModal = true"
    />

  <AddCardModal
    v-if="showAddModal"
    />
</template>

<script>
import AddCardModal from '@/components/AddCardModal.vue'
import CardComponent from '@/components/CardComponent.vue'

export default {
  name: 'RegisteredCards',
  components: {
    AddCardModal,
    CardComponent,
  },
  data: function() {
    return {
      'configuredCards': [],
      'showAddModal': false,
      'cardDetails': {}
    }
  },
  methods: {
    getConfiguredCards: function() {
      const axios = require('axios')
      let self = this

      axios.get('http://127.0.0.1:8081/api/list_cards')
        .then(function (response) {
          self.configuredCards = response.data.cards
          console.log(response.data.cards)
        })
        .catch(function (error) {
          console.log(error);
        })
    },
  },
  created: function() {
    this.getConfiguredCards()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#cardFlexbox {
  display: flex;
  justify-content: space-around;
  flex-flow: row wrap;
  align-content: center;
  width: 100%;
}

#cardFlexbox > .cardFlexboxItem {
  margin-bottom: 40px;
  width: 800px;
}
</style>
