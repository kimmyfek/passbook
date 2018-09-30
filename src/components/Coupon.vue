<template>
<div class="coup" :class="getCoupColorClass(coup_type)">
  <h5>
    {{ desc }}
  </h5>
  <small><i v-if="restrictions">({{ restrictions }})</i></small>
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
      var base = 'coup'
      if (cType === 'Drink') {
        return base + ' p-3 bg-warning text-white'
      } else if (cType === 'Food') {
        return base + ' p-3 bg-primary text-white'
      }
    }
  }
}
</script>

<style scoped>
.coup {
  flex-grow: 1;
  height: 100px;
}
</style>
