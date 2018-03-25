<template>
<div :class="getCoupColorClass(coup_type)">
  <h5>
    {{ desc }}
  </h5>
  <h6 v-if="restrictions">({{ restrictions }})</h6>
</div>
</template>

<script>
export default {
  name: 'Coupon',
  props: {
    coup_type: String,
    desc: String,
    restrictions: String
  },
  methods: {
    getCoupColorClass: function (cType) {
      if (cType === 'Drink') {
        return 'p-3 bg-warning text-white'
      } else if (cType === 'Food') {
        return 'p-3 bg-primary text-white'
      }
    }
  }
}
</script>

<style>
</style>
