<template>
<div class="container border-top border-bottom border-secondary">
  <div class="row bus-data">

    <div class="col">

      <div class="row">
        <div class="col-5 title">
          <h3>{{ name }}</h3>
        </div>
        <div class="col">
        </div>
        <div class="col-3">

          <div class="col row">
            {{ locations[0].address }}
          </div>
          <div class="col row">
            {{ formatPhone(locations[0].phone) }}
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-1">
          <a role="button" class="btn btn-secondary" :href="website">Website</a>
        </div>
        <div class="hours col">
        </div>
        <div class="locations col">
          {{ desc }}
        </div>
      </div>

    </div>

    <div class="col col-2 coupons">
      <span v-for="coup in coupons" :key="coup.coupon_id">
        <coupon v-bind=coup></coupon>
      </span>
    </div>
  </div>
</div>
</template>

<script>
import Coupon from '@/components/Coupon'

export default {
  name: 'Business',
  props: {
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
    },
    phone: {
      type: String,
      required: true
    },
    website: {
      type: String,
      required: true
    }
  },
  methods: {
    formatPhone: function (pn) {
      var s2 = ('' + pn).replace(/\D/g, '')
      var m = s2.match(/^(\d{3})(\d{3})(\d{4})$/)
      return (!m) ? null : '(' + m[1] + ') ' + m[2] + '-' + m[3]
    }
  },
  components: {
    'coupon': Coupon
  }
}
</script>

<style>
.bus-data {
  padding: 15px 0px;
}

.title {
  text-align: left;
}
</style>
