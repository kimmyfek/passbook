<template>
<div>
  <b-row no-gutters align-h="start">
    <b-col>
      <b-dropdown id="ddown-sm"
        size="sm"
        :text="'Locations (' + locations.length + '): ' + formatNeighborhood(active, true)"
        class="m-2 loc-button"
      >
        <b-dropdown-item-button
          v-for="loc in locations"
          :key="busID + loc.loc_id"
          v-on:click="setActive(loc)"
        >
          {{ formatNeighborhood(loc, false) }}
        </b-dropdown-item-button>
      </b-dropdown>
    </b-col>
    <b-col></b-col>
  </b-row>

  <!-- Address -->
  <b-row no-gutters class="lj">
    <b-col cols="3">
      <b>Address: </b>
    </b-col>
    <b-col>
      {{ active.address }}
    </b-col>
  </b-row>

  <!-- Phone -->
  <b-row no-gutters class="lj" v-if="active.phone !== null">
    <b-col cols="3">
      <b>Phone: </b>
    </b-col>
    <b-col>
      {{ active.phone }}
    </b-col>
  </b-row>

  <b-row no-gutters class="lj"
    v-if="active.website !== null && active.website !== 'None'"
  >
    <b-col cols="3">
      <b>Website: </b>
    </b-col>
    <b-col>
      <a target="_blank" :href="active.website">{{ formatSite(active.website) }}</a>
    </b-col>
  </b-row>

  <b-row no-gutters class="lj">
    <b-col cols="3">
      <b>Rating: </b>
    </b-col>
    <b-col>
      {{ active.google_rating }} * <!-- TODO -->
    </b-col>
  </b-row>

    <!-- TODO {{ active.hours }} -->
</div>
</template>

<script>
export default {
  data () {
    return {
      active: null
    }
  },
  props: {
    locations: {
      type: Array,
      required: true
    },
    busID: Number
  },
  methods: {
    formatSite: function (ws) {
      var parsed = ws.replace(/^https?:\/\/(www\.)?/, '')
      parsed = parsed.replace(/\/.*/, '')
      return parsed
    },

    formatPhone: function (pn) {
      var s2 = ('' + pn).replace(/\D/g, '')
      var m = s2.match(/^(\d{3})(\d{3})(\d{4})$/)
      return (!m) ? null : '(' + m[1] + ') ' + m[2] + '-' + m[3]
    },

    formatNeighborhood: function (loc, inMenu) {
      var street = loc.address.split(',')[0]
      var formatted = loc.neighborhood + ' - ' + street
      if (inMenu) {
        if (formatted.length > 28) {
          formatted = formatted.substring(0, 25) + '...'
        }
      }
      return formatted
    },

    setActive: function (loc) {
      this.active = loc
    }
  },
  created: function () {
    this.active = this.locations[0] // TODO
  },
  updated: function () {
    this.active = this.locations[0] // TODO
  }
}
</script>

<style scoped>
.lj {
  text-align: left;
}

.loc-button {
  margin-left: 0px !important;
  margin-right: 0px !important;
}

#ddown-sm {
  float: left;
}

</style>
