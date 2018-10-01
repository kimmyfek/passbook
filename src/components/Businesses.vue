<template>
<div class="businesses">
  <div class="filter">
    <sidebarmenu :selectedNeighborhoods=selectedNeighborhoods></sidebarmenu>
  </div>

  <div v-if="filteredBusinesses.length === 0">
    <span v-for="biz in businesses" :key=biz.id>
      <business v-bind="biz"></business>
    </span>
  </div>

  <div v-else>
    <small> Filtering by Neighborhoods: {{ selectedNeighborhoods | stringifyArray }} </small>
    <span v-for="fBiz in filteredBusinesses" :key=fBiz.id>
      <business v-bind="fBiz"></business>
    </span>
  </div>
</div>
</template>

<script>
import { BusAPI } from '@/common/bus.api'
import Business from '@/components/Business'
import SidebarMenu from '@/components/SidebarMenu'

export default {
  name: 'Businesses',
  data () {
    return {
      businesses: [],
      selectedNeighborhoods: [],
      filteredBusinesses: []
    }
  },
  watch: {
    selectedNeighborhoods: function (newHood, oldHood) {
      this.filterBusinesses()
    }
  },
  created: function () {
    this.updateBusinesses()
  },
  methods: {
    updateBusinesses: function () {
      console.log('update business')
      BusAPI.getBusinesses()
        .then(resp => {
          this.businesses = resp.data
        })
      console.log(this.filteredBusinesses)
    },

    filterBusinesses: function () {
      console.log('filter business for ' + this.selectedNeighborhoods)

      this.filteredBusinesses = []
      console.log('Emptying filter')

      for (var biz in this.businesses) {
        for (var loc in this.businesses[biz].locations) {
          if (this.selectedNeighborhoods.includes(this.businesses[biz].locations[loc].neighborhood)) {
            console.log('yesss')
            this.filteredBusinesses.push(this.businesses[biz])
            break
          }
        }
      }

      console.log(this.filteredBusinesses)
    }
  },
  components: {
    'business': Business,
    'sidebarmenu': SidebarMenu
  }
}
</script>

<style>
.businesses {
  margin: 10%;
}

.filter {
  position: relative;
  top: -50px;
}

</style>
