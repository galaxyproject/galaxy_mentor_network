<template>
    <div class="layout">
        <header class="masthead">
            <b-navbar class="container justify-content-center" toggleable="lg">
                <b-navbar-brand href="#" class="align-middle">
                    <g-image src="~/images/logos/logo_wo_text.png" class="d-inline-block" width="50" alt="GMN Logo"/>
                  {{ $static.metadata.siteName }}
                </b-navbar-brand>
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav id="navbar-menu" class="ml-auto">
                        <b-nav-item href="/about/">About</b-nav-item>
                        <b-nav-item-dropdown text="Guides" right>
                            <b-dropdown-item href="/application/">Application Guidelines</b-dropdown-item>
                            <b-dropdown-item href="#">Mentorship Guidelines</b-dropdown-item>
                        </b-nav-item-dropdown>
                        <b-nav-item href="/faq/">FAQ</b-nav-item>
                        <b-nav-item-dropdown text="Network" right>
                            <b-dropdown-item href="#">Gmentees</b-dropdown-item>
                            <b-dropdown-item href="#">Gmentors</b-dropdown-item>
                            <b-dropdown-item href="#">Network Managers</b-dropdown-item>
                        </b-nav-item-dropdown>
                        <b-nav-item href="/blog/">Blog</b-nav-item>
                    </b-navbar-nav>
                </b-collapse>
            </b-navbar>
        </header>
        <main id="maincontainer" class="container">
            <slot />
        </main>
        <footer class="static-footer">
          <b-container>
             <h3>Help and Support</h3>
             <!--Grid row-->
             <b-row>
                  <!--Grid column-->
                  <b-col lg="6" md="6" sm="12">
                 <h6> Project Coordinators</h6>

                     <li><a href="https://matrix.to/#/@beatrizserrano:matrix.org">Beatriz Serrano-Solano</a></li>
                     <li><a href="https://matrix.to/#/@bebatut:matrix.org">Berenice Batut</a></li>
                     <li><a href="https:matrix.to/#/@assuntad23:matrix.org">Assunta DeSanto</a></li>

                 <h6> Contact Us</h6>
                 <p>
                     <i class="fas fa-envelop"></i><a href="mailto:galaxy.mentoring@gmail.com">galaxy.mentoring@gmail.com</a>
                     <br>
                     <i class="fab fa-github"></i><a href="https://github.com/bebatut/galaxy_mentor_network">Galaxy_Mentor_Network</a>
                   </p>
                  </b-col>

                   <!--Grid column-->
                  <b-col lg="6" md="6" sm="12">
                       <p>
                         The <a href="#">FAQ</a> section contains answers to most of the questions on your mind. Do you want to report a problem or suggest an improvement? We'll appreciate if you <a href="https://github.com/bebatut/galaxy_mentor_network/issues">open an issue</a> on our GitHub repository and we'll attend to it as quickly as possible.
                       </p>
                  </b-col>
                  <!--Grid column-->
              </b-row>
              <!--Grid row-->
          </b-container>
        </footer>
    </div>
</template>

<script>
export default {
  name: 'layout',
}
</script>

<static-query>
query {
  metadata {
    siteName
  }
}
</static-query>

<style lang=".scss" scoped>
  footer {
    background-color:"#ece9ef";
    padding: "20px"
  }
</style>

