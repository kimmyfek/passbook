<template>
<div class="container border-top border-bottom border-secondary">
  <div class="row bus-data">

    <div class="col-5">

      <div class="row">
        <div class="col lj">
          <h3>{{ name }}</h3>
        </div>
      </div>

      <div class="row">
        <div class="col-11 lj">
          <i>{{ desc }}</i>
        </div>
      </div>

    </div>

    <div class="col-4">
      <locationsComp :busID=business_id :locations=locations></locationsComp>
    </div>

    <div class="col col-3 coupons">
      <b-row no-gutters v-for="coup in coupons" :key="coup.coupon_id">
        <b-col>
          <coupon v-bind=coup></coupon>
        </b-col>
      </b-row>
    </div>

  </div>
</div>
</template>

<script>
import Coupon from '@/components/Coupon'
import Locations from '@/components/Locations'

export default {
  name: 'Business',
  props: {
    business_id: {
      type: Number,
      required: true
    },
    coupons: {
      type: Array,
      required: true
    },
    desc: {
      type: String,
      required: true
    },
    locations: {
      type: Array,
      required: true
    },
    name: {
      type: String,
      required: true
    }
  },
  components: {
    'coupon': Coupon,
    'locationsComp': Locations
  },
  methods: {
  }
}
</script>

<style scoped>
.bus-data {
  padding: 15px 0px;
}

.lj {
  text-align: left;
}

</style>
