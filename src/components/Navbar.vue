<template>
  <div class="top-nav">
  <b-navbar toggleable="md" type="light" variant="warning">

    <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

    <b-navbar-brand href="#">Denver Passbook</b-navbar-brand>

    <b-collapse is-nav id="nav_collapse">

    </b-collapse>
  </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style>
.top-nav {
  margin-bottom: 60px;
}
</style>
