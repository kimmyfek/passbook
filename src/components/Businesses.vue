<template>
<div class="businesses">
  <span v-for="business in businesses" :key=business.id>
    <business v-bind="business"></business>
  </span>
</div>
</template>

<script>
import { BusAPI } from '@/common/bus.api'
import Business from '@/components/Business'

export default {
  name: 'Businesses',
  data () {
    return {
      businesses: []
    }
  },
  created: function () {
    this.updateBusinesses()
  },
  methods: {
    updateBusinesses: function () {
      BusAPI.getBusinesses()
        .then(resp => {
          this.businesses = resp.data
        })
    }
  },
  components: {
    'business': Business
  }
}
</script>

<style>
.businesses {
  margin: 10%;
}
</style>
