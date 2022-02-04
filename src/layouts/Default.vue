<template>
  <b-navbar variant="dark" type="dark">
    <b-navbar-brand href="#">
      <img src="assets/images/logos/colour_text.png" class="d-inline-block align-top" alt="GMN Logo">
      Galaxy Mentor Network
    <b-nav-item>About</b-nav-item>

    <b-nav-item-dropdown text="GMN Guides" right>
        <b-dropdown-item href="#">Application Guidelines</b-dropdown-item>
        <b-dropdown-item href="#">Mentroship Guidelines</b-dropdown-item>
      </b-nav-item-dropdown>
    <b-nav-item>FAQ</b-nav-item>
    <b-nav-item disabled>Project & Participants</b-nav-item>
    <b-nav-item>Blog</b-nav-item>
  </b-nav>
    <slot/>
  </div>
</template>

<static-query>
query {
  metadata {
    siteName
  }
}
</static-query>

<style>
body {
  font-family: -apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
  margin:0;
  padding:0;
  line-height: 1.5;
}

.layout {
  max-width: 760px;
  margin: 0 auto;
  padding-left: 20px;
  padding-right: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  height: 80px;
}

.nav__link {
  margin-left: 20px;
}
</style>
