<template>
  <div id="menu">
  <Slide right noOverlay menuLabel="Filter">
    <b-form-group label="Neighborhood(s)">
      <b-form-checkbox-group
        stacked
        v-model="selectedNeighborhoods"
        :options="neighborhoods"
        @input="checkboxToggle">
      </b-form-checkbox-group>
    </b-form-group>
  </Slide>
  </div>
</template>

<script>
import { Slide } from 'vue-burger-menu'
export default {
  name: 'SidebarMenu',
  components: {
    Slide
  },
  methods: {
    checkboxToggle () {
      console.log('clicked')
      this.$parent.selectedNeighborhoods = this.selectedNeighborhoods
      console.log(this.$parent.selectedNeighborhoods)
    }
  },
  data () {
    return {
      // TODO: move to backend API
      selectedNeighborhoods: [],
      neighborhoods: [
        {text: 'Ballpark', value: 'Ballpark'},
        {text: 'Cap Hill', value: 'Cap Hill'},
        {text: 'Cherry Creek', value: 'Cherry Creek'},
        {text: 'City Park', value: 'City Park'},
        {text: 'Downtown', value: 'Downtown'},
        {text: 'DTC', value: 'DTC'},
        {text: 'East Denver', value: 'East Denver'},
        {text: 'Glendale', value: 'Glendale'},
        {text: 'Golden Triangle', value: 'Golden Triangle'},
        {text: 'Govs Park', value: 'Govs Park'},
        {text: 'Highlands', value: 'Highlands'},
        {text: 'Hilltop', value: 'Hilltop'},
        {text: 'Lakewood', value: 'Lakewood'},
        {text: 'Littleton', value: 'Littleton'},
        {text: 'Lodo', value: 'Lodo'},
        {text: 'North Denver', value: 'North Denver'},
        {text: 'Platt Park', value: 'Platt Park'},
        {text: 'RiNo', value: 'RiNo'},
        {text: 'Sloans Lake', value: 'Sloans Lake'},
        {text: 'South Broadway', value: 'South Broadway'},
        {text: 'South Denver', value: 'South Denver'},
        {text: 'Stapleton', value: 'Stapleton'},
        {text: 'Virginia Village', value: 'Virginia Village'},
        {text: 'Wash Park', value: 'Wash Park'},
        {text: 'West Denver', value: 'West Denver'}
      ]
    }
  }
}
</script>

<style>
  .bm-burger-button {
    width: auto;
    top: auto;
  }
  .bm-burger-bars {
  }
  .bm-menu {
    text-align: left;
  }
  .label {
    font-size: xx-large;
  }
</style>
