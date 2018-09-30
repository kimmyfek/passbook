<template>
<div class="container border-top border-bottom border-secondary">
  <div class="row bus-data">

    <div v-if="shutdown" class="shutdown alert alert-danger">
      <span> {{ name }} is permanently closed. </span>
    </div>

    <div class="col-xs-6 col-md-4">

      <div class="row">
        <div class="col lj">
          <h3>{{ name }}</h3>
        </div>

      </div>

      <div class="row">
        <div class="col lj">
          <i>{{ desc }}</i>
        </div>
      </div>
    </div>

    <div class="col-xs-6 col-md-4">
      <locationsComp :busID=business_id :locations=locations></locationsComp>
    </div>

    <div class="col-xs-6 col-md-4 coup-cont">
      <div v-for="coup in coupons" :key="coup.coupon_id">
          <coupon v-bind=coup></coupon>
      </div>
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
    shutdown: {
      type: Boolean,
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
  margin-top: 2%;
  margin-bottom:2%;
  position:relative;
}

.lj {
  text-align: left;
}

.coup-cont {
  display: flex;
  flex-wrap: wrap;
  flex-direction: column;
  height: 200px;
}
.shutdown {
  position: absolute;
  z-index: 1;
  height:100%;
  width:100%;
  opacity: 0.95;
}

.shutdown span {
  position: relative;
  top: 50%;
  transform: translateY(-50%);
  text-transform: uppercase;
}

</style>
