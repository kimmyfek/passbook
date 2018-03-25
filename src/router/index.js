import Vue from 'vue'
import Router from 'vue-router'
import Businesses from '@/components/Businesses'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Businesses',
      component: Businesses
    }
  ]
})
