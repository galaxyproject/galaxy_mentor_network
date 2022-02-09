<template>
    <div class="layout">
        <header class="masthead">
            <b-navbar class="container justify-content-center" toggleable="lg">
                <b-navbar-brand href="/" class="align-middle">
                    <g-image src="~/images/logos/logo_white_wo_text.png" class="d-inline-block" width="50" alt="GMN Logo"/>
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
        <main class="container maincontainer">
            <slot />
        </main>
        <footer class="footer">
            <b-container class="footer-container">
                <b-row>
                    <b-col>
                        <h3>Get in touch</h3>
                        <p>
                            <i class="fab fa-gitter"></i>
                            Discuss with us on <a href="#">Matrix</a>
                            <br>
                            <i class="fab fa-envelope"></i>
                            Email us at <a href="mailto:galaxy.mentoring@gmail.com">galaxy.mentoring@gmail.com</a>
                            <br>
                            <i class="fab fa-github"></i>
                            Check our <a href="https://github.com/bebatut/galaxy_mentor_network">GitHub repository</a>
                        </p>
                    </b-col>
                    <b-col>
                        <p>The <a href="/faq/">FAQ</a> section contains answers to most of the questions on your mind.</p>

                        <p>Do you want to report a problem or suggest an improvement? We'll appreciate if you <a href="https://github.com/bebatut/galaxy_mentor_network/issues">open an issue</a> on our GitHub repository and we'll attend to it as quickly as possible.</p>

                        <p>This website content is licensed <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY SA 4.0</a></p>
                    </b-col>
                </b-row>
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

