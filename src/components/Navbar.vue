<template>
  <div class="top-nav">
  <b-navbar toggleable="md" type="dark" variant="info">

    <b-navbar-brand href="#">Denver Passbook</b-navbar-brand>
    <sidebarmenu></sidebarmenu>

  </b-navbar>
  </div>
</template>

<script>
import SidebarMenu from '@/components/SidebarMenu'
export default {
  name: 'Navbar',
  components: {
    'sidebarmenu': SidebarMenu
  }
}
</script>

<style>
.top-nav {
  margin-bottom: 60px;
}
</style>
